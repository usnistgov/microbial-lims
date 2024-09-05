import os
import json
import logging
import importlib
import re
from pathlib import Path
from urllib.parse import urljoin
from typing import Optional

import click
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import track

from linkml_runtime import SchemaView
from linkml_runtime.linkml_model.meta import ClassDefinition, SlotDefinition
from pydantic.alias_generators import to_snake
from pydantic import ValidationError

from microbial_experiment import (
    ELabExperiment,
    ELabItem,
    ELabItemValue,
    ConfiguredBaseModel,
    ArrayValue
)
from elabapi import ELabApi

# TODO: handle radio type (experiment 136 - CytoFLEX_VolumeCalibrations)

c = Console()
yaml_path = Path(__file__).resolve().parent.parent / "microbial_experiment.yaml"
sv = SchemaView(yaml_path)
logging.basicConfig(
    level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)
logger = logging.getLogger(__name__)

for lg in [logging.getLogger(name) for name in logging.root.manager.loggerDict]:
    lg.setLevel(logging.WARNING)

# create an instance of the API with URL and credentials
e = ELabApi(
    api_base_url=os.environ.get("ELAB_URL"),
    api_key=os.environ.get("ELAB_API_KEY"),
)


class ParsingError(ValueError):
    """An Exception to raise if the parser cannot interpret a value"""

    pass


def get_schema_class_for_name(class_name: str):
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module("microbial_experiment")
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c


def get_classdef_by_name_or_title(name_or_title: str) -> Optional[ClassDefinition]:
    cls = sv.get_class(name_or_title)
    if cls is None:
        return get_classdef_by_title(name_or_title)
    return cls


def get_classdef_by_title(title: str) -> Optional[ClassDefinition]:
    for cls_k, cls_v in sv.all_classes().items():
        if title == cls_v["title"]:
            return sv.all_classes()[cls_k]
    return None


def get_slot_by_name_or_title(name_or_title: str) -> Optional[SlotDefinition]:
    # slots are snake case, so use to_snake:
    slot = sv.get_slot(to_snake(name_or_title))
    if slot is None:
        return get_slot_by_title(name_or_title)
    return slot


def get_slot_by_title(title: str) -> Optional[SlotDefinition]:
    for slot_k, slot_v in sv.all_slots().items():
        if title == slot_v["title"]:
            return sv.all_slots()[slot_k]
    return None


def parse_experiment_link(experiment_id: int) -> ELabExperiment:
    elab_response = e.get_experiment(experiment_id)
    exp = ELabExperiment(
        id=elab_response["id"],
        elabid=elab_response["elabid"],
        url=elab_response["sharelink"],
        api_url=urljoin(e.api_base_url, f"experiments/{experiment_id}"),
        type=elab_response["type"],
        title=elab_response["title"],
        category_title=elab_response["category_title"],
        status_title=elab_response["status_title"],
    )
    return exp


def parse_item_link(item_id: int) -> ELabItem:
    elab_response = e.get_item(item_id)
    item = ELabItem(
        id=elab_response["id"],
        elabid=elab_response["elabid"],
        url=elab_response["sharelink"],
        api_url=urljoin(e.api_base_url, f"items/{item_id}"),
        type=elab_response["type"],
        title=elab_response["title"],
        category_title=elab_response["category_title"],
        status_title=elab_response["status_title"],
    )
    return item


def parse_elab_item_value(item_id: int, item_class: str) -> ELabItemValue:
    return get_schema_class_for_name(item_class)(value=parse_item_link(item_id))


def gather_underscored_keys(extra_fields: dict) -> dict:
    """
    Group metadata terms that end in "underscore-digit" pattern into lists.

    The Microbial Strain templates represent lists of metadata terms (which are not
    supported directly in eLabFTW) as ``Field_1``, ``Field_2``, ``Field_3``, etc.
    In order to process these values into lists/arrays, this method gathers
    keys with the same base into lists, and removes the constituent keys from
    the provided metadata. For example, if ``extra_fields`` contained the following
    keys and values:::

        FieldOne: ValueOne
        FieldTwo: ValueTwo
        FieldThree_1: ValueThree
        FieldFour_1: ValueFour.1
        FieldFour_2: ValueFour.2
        FieldFour_3: ValueFour.3

    This method will change the metadata dictionary to contain the following:::

        FieldOne: ValueOne
        FieldTwo: ValueTwo
        FieldThree: [ValueThree]
        FieldFour: [ValueFour.1, ValueFour.2, ValueFour.3]

    It will also remove any metadata keys that do not have a "value" item contained
    within, which prevents problems like MicrobialMaterialID, where the _1 or _2 keys
    might have a value, but later ones might not.

    Parameters
    ----------
    extra_fields:
        A dictionary, but more specifically this method is intended for a dictionary
        containing the `"extra_fields"` portion of an ELabFTW experiment/item's metadata

    Returns
    -------
    dict
        The metadata dictionary edited as described above
    """
    # match keys that are "<text>_<digits>"
    keys = list(extra_fields.keys())
    regex = re.compile(r"^(.*)_(\d+)$")
    matching_keys = [i for i in keys if regex.match(i)]
    # pull out and deduplicate the base (the "<text>" part from above)
    # of the underscored terms
    base_parts = list(set([regex.match(i).groups()[0] for i in matching_keys]))
    # for each base_part, gather the related extra_keys metadata into a list
    # and drop the underscored parts
    for b in base_parts:
        these_keys = sorted([i for i in matching_keys if b in i])
        extra_fields[b] = [
            extra_fields[i] for i in these_keys if 'value' in extra_fields[i]
        ]
    for k in matching_keys:
        del extra_fields[k]
    return extra_fields


def parse_single_node(
    node_def: SlotDefinition, 
    meta: dict, 
    wrap_item: bool = True,
) -> ConfiguredBaseModel:
    """
    Translate a single metadata dictionary (``meta``) into a Pydantic
    model instance from the ``microbial_experiment`` schema.

    Parameters
    ----------
    node_def
        A SlotDefinition using LinkML's ``SchemaView`` used to get the correct
        model class for the metadata
    meta
        A metadata node from the ELabFTW API response. Should contain keys:
        ``type``, ``value`` ``description``, ``unit`` (`optional`), etc.
    wrap_item
        Whether to "wrap" an ELabItem as an ELabItemValue. This should be ``True`` for
        individual item links, but should be ``False`` if processing a list of items
        (where the "value" is the list of items)

    Returns
    -------
    ConfiguredBaseModel
        A subclass of :py:class:`ConfiguredBaseModel` representing a slot in the
        ``microbial_experiment`` LinkML data model
    """
    this_node_name = node_def["name"]
    if meta["type"] == "items":
        # raise an error if the "value" key is missing from an item link
        if "value" not in meta:
            # if this is an ArrayValue node, it's possible the _2, _3, etc. terms
            # are empty and that's okay
            if not issubclass(get_schema_class_for_name(node_def["range"]), ArrayValue):
                raise ParsingError(
                    f'"items" metadata value did not have expected "value" key: {meta};'
                    f' node was "{this_node_name}"'
                )
            # TODO: need to handle case like MicrobialMaterialID, where _1 or _2 might
            #       have a value, but later ones do not. Maybe parse this 
            #       in gather_underscored_keys
        if not isinstance(meta["value"], int):
            raise ParsingError(
                '"items" metadata node did not have a valid integer value; '
                f'value was "{meta["value"]}"; node was "{this_node_name}"'
            )
        if wrap_item:
            this_node = parse_elab_item_value(meta["value"], node_def["range"])
        else:
            this_node = parse_item_link(meta["value"])
    elif meta["type"] in ["text", "select", "number", "date", "radio", "checkbox"]:
        # get a python class definition for the type of this item
        cls = get_schema_class_for_name(node_def["range"])

        # workaround for allow_multi_value selects with a single value rather than list
        if issubclass(cls, ArrayValue) and not isinstance(meta["value"], list):
            logger.warning(
                "Found an ArrayValue returned as single value, wrapping as list"
            )
            meta["value"] = [meta["value"]]

        # TODO: remove temporary workaround for FixationMethod
        if this_node_name == "fixation_method" and "None" in meta["value"]:
            meta["value"].remove("None")
            meta["value"].append("NoFixation")

        # dynamically build up the arguments to instantiate the class
        args = {"value": meta["value"]}
        if "unit" in meta and meta["unit"]:
            # TODO: remove temporary workaround for IncubationDuration time unit
            if meta["unit"] == "hour":
                meta["unit"] = "hr"

            args["unit"] = meta["unit"]

        # explicitly cast a BooleanValue to boolean:
        if node_def["range"] == "BooleanValue":
            if meta["value"].lower() in ["true", "1", "t", "y", "yes", "on"]:
                args["value"] = True
            elif meta["value"].lower() in ["false", "0", "f", "n", "no", "off"]:
                args["value"] = False
            else:
                raise ParsingError(
                    f'Could not cast value "{meta["value"]}" to BooleanValue; '
                    f'node was "{this_node_name}"'
                )

        # create the instance (StringValue, UriValue, DurationValue, etc.)
        this_node = cls(**args)

    return this_node


def parse_record_metadata(experiment: dict):
    """

    Parameters
    ----------
    experiment
        The JSON response from the ELabFTW API for an experiment or item
    """
    parsed_metadata = {}
    if experiment["metadata"] is None:
        raise ParsingError(f"No metadata present in experiment {experiment['id']}")
    metadata = json.loads(experiment["metadata"])
    experiment_class = None
    elab_experiment = parse_experiment_link(experiment["id"])
    parsed_metadata["elab_experiment"] = elab_experiment
    if "extra_fields" not in metadata:
        raise ParsingError(
            f"extra_fields not found in metadata for experiment {experiment['id']}"
        )
    if "TemplateName" not in metadata['extra_fields']:
        raise ParsingError(
            '"TemplateName" field not found in extra_fields; cannot process experiment'
        )
    metadata["extra_fields"] = gather_underscored_keys(metadata["extra_fields"])
    for k, v in metadata["extra_fields"].items():
        logger.debug(f"{k} -- {v}")
        this_node_def = get_slot_by_name_or_title(k)
        if this_node_def is None:
            raise ParsingError(f"Did not find schema definition for {k}; "
                               f"metadata key was \"{k}\"; value: \"{v}\"")
        if this_node_def["name"] == "template_name":
            # special case for template name value
            this_node_classdef = get_classdef_by_name_or_title(v["value"])
            if this_node_classdef["title"] is None:
                raise ParsingError(
                    f'Template class {this_node_classdef.name} is missing "title"'
                )
            experiment_class = get_schema_class_for_name(this_node_classdef["name"])
            templ_class_name = this_node_classdef["slot_usage"]["template_name"][
                "range"
            ]
            template_name_class = get_schema_class_for_name(templ_class_name)
            this_node = template_name_class(value=this_node_classdef["title"])
        elif isinstance(v, list):
            # parse list of items (came from an underscored term)
            elab_item_list = [
                parse_single_node(this_node_def, i, wrap_item=False) for i in v
            ]
            cls = get_schema_class_for_name(this_node_def["range"])
            this_node = cls(value=elab_item_list)
        else:
            this_node = parse_single_node(this_node_def, v)
        parsed_metadata[this_node_def["name"]] = this_node

    experiment_pyd = experiment_class(**parsed_metadata)
    return experiment_pyd


# experiments = e.get_experiments_by_category("Ready for export")
with open("experiments.json", "r") as f:
    experiments = json.load(f)

i = 0
for exp in track(experiments):
    try:
        experiment_model = parse_record_metadata(exp)
        i += 1
        logger.info(experiment_model)
    except (ParsingError, ValidationError) as exception:
        logger.error(f"Could not validate experiment {exp['id']}")
        logger.error(exception)

c.print(f"Validated {i} out of {len(experiments)} experiments")