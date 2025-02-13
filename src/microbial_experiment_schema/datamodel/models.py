from __future__ import annotations 
from datetime import (
    datetime,
    date,
    time
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    ClassVar,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)
metamodel_version = "None"
version = "2024.09.04"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'microbial_experiment_schema',
     'default_range': 'string',
     'description': 'Metadata schemas for validation of ELN data entries as part '
                    'of the Microbial LIMS project',
     'id': 'https://w3id.org/usnistgov/microbial-experiment-schema',
     'imports': ['linkml:types'],
     'license': 'NIST Public License',
     'name': 'microbial-experiment-schema',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'microbial_experiment_schema': {'prefix_prefix': 'microbial_experiment_schema',
                                                  'prefix_reference': 'https://w3id.org/usnistgov/microbial-experiment-schema/'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/schema/qudt/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://mml-lims.***REMOVED***.nist.gov/microbial-experiment-schema'],
     'source_file': 'src/microbial_experiment_schema/schema/microbial_experiment_schema.yaml',
     'title': 'Microbial Experiment Schema'} )

class ELabItemType(str, Enum):
    """
    Allowed record type value for an ELabFTW item/resource
    """
    # An ELabFTW item/resource record
    items = "items"


class ELabExperimentType(str, Enum):
    """
    Allowed record type value for an ELabFTW experiment
    """
    # An ELabFTW experiment record
    experiments = "experiments"


class DurationUnitEnum(str, Enum):
    """
    Allowed time duration unit type values
    """
    # seconds
    sec = "sec"
    # hours
    hr = "hr"
    # minutes
    min = "min"


class VolumeUnitEnum(str, Enum):
    """
    Allowed volume unit type values
    """
    # milliliters
    mL = "mL"
    # microliters
    µL = "µL"


class LengthUnitEnum(str, Enum):
    """
    Allowed linear length unit type values
    """
    # micrometers
    µm = "µm"


class CountUnitEnum(str, Enum):
    """
    Allowed count unit type values
    """
    # event count
    events = "events"


class FlowRateUnitEnum(str, Enum):
    """
    Allowed flow rate unit type values
    """
    # microliters per minute
    µLSOLIDUSmin = "µL/min"


class CFUMethodEnum(str, Enum):
    """
    Allowed colony forming unit count method values
    """
    # a plate spread
    Plate_spread = "Plate spread"
    # a drip plate
    Drip_plate = "Drip plate"
    # a spiral plater
    Spiral_plater = "Spiral plater"
    # a droplet
    Droplet = "Droplet"
    # all other CFU methods
    Other = "Other"


class FCInjectionModeEnum(str, Enum):
    """
    Allowed flow cytometry injection mode values
    """
    # plate
    Plate = "Plate"
    # tube
    Tube = "Tube"
    # not applicable
    NA = "NA"


class FixationMethodEnum(str, Enum):
    """
    Allowed fixation method values
    """
    # formaldehyde fixation
    Formaldehyde = "Formaldehyde"
    # heat fixation
    Heat = "Heat"
    # ethanol fixation
    Ethanol = "Ethanol"
    # no fixation performed
    No_Fixation = "None"


class AgitationEnum(str, Enum):
    """
    Allowed agitation speed unit type values
    """
    # revolutions per minute
    rpm = "rpm"
    # x g
    x_g = "x g"


class IncubationAtmosphereEnum(str, Enum):
    """
    Allowed cell incubation atmosphere values
    """
    # atmospheric conditions
    Atmospheric = "Atmospheric"
    # atmospheric conditions with 5% carbon dioxide
    Atmospheric_PLUS_SIGN_5PERCENT_SIGN_CO2 = "Atmospheric + 5% CO2"
    # anaerobic conditions
    Anaerobic = "Anaerobic"


class TemperatureUnitEnum(str, Enum):
    """
    Allowed temperature unit type values
    """
    # degrees celsius
    DEGREE_SIGNC = "oC"
    # degrees fahrenheit
    DEGREE_SIGNF = "oF"


class MicroscopyModalitiesEnum(str, Enum):
    """
    Allowed microscopy modality values
    """
    # Digital image correlation
    DIC = "DIC"
    # Bright field imaging
    Brightfield = "Brightfield"
    # Phase contrast imaging
    Phase_Contrast = "Phase Contrast"


class NucleicAcidTypeEnum(str, Enum):
    """
    Allowed nucleic acid type values
    """
    # Ribonucleic acid
    RNA = "RNA"
    # Deoxyribonucleic acid
    DNA = "DNA"


class ObjectivesEnum(str, Enum):
    """
    Allowed microscopy objective values
    """
    # 4 times magnification
    number_4X = "4X"
    # 10 times magnification
    number_10X = "10X"
    # 20 times magnification
    number_20X = "20X"
    # 40 times magnification with oil immersion
    number_40X_oil = "40X oil"
    # 60 times magnification with oil immersion
    number_60X_oil = "60X oil"
    # 60 times magnification with water immersion
    number_60X_water = "60X water"
    # 100 times magnification with oil immersion
    number_100X_oil = "100X oil"


class UnitlessEnum(str, Enum):
    """
    Allowed value for "unitless" numerical values
    """
    # An explicitly unitless value
    Unitless = "Unitless"


class SamplePurposeCodeEnum(str, Enum):
    """
    Allowed sample purpose code values
    """
    # Positive control
    Positive_control = "Positive control"
    # Negative control
    Negative_control = "Negative control"
    # Reference cell
    Reference_cell = "Reference cell"
    # Reference for fluorescence
    Reference_fluorescence = "Reference fluorescence"
    # Reference for scattering
    Reference_scattering = "Reference scattering"
    # Reference for size
    Reference_size = "Reference size"
    # Reference for concentration
    Reference_concentration = "Reference concentration"
    # Quality control
    Quality_control = "Quality control"
    # Compensation control
    Compensation_control = "Compensation control"
    # A test sample
    Test = "Test"
    # All other sample purposes
    Other = "Other"


class ImageTypeEnum(str, Enum):
    """
    Allowed microscopy image type values
    """
    # Time lapse imagery
    Time_lapse = "Time lapse"
    # A scan of an area
    Area_scan = "Area scan"
    # Z (focal) stack
    z_stack = "z stack"
    # Not applicable
    NA = "NA"


class TransmissionModeEnum(str, Enum):
    """
    Allowed microscopy transmission mode values
    """
    # Digital Image Correlation
    DIC = "DIC"
    # Brightfield imaging
    Brightfield = "Brightfield"
    # Phase contrast imaging
    Phase_Contrast = "Phase Contrast"



class Experiment(ConfiguredBaseModel):
    """
    Holds information about a specific type of Microbial Strain experiment. The specific metadata for each type of experiment is controlled by \"template data classes\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'Experiment',
         'tree_root': True})

    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: StringValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class ExperimentWithData(Experiment):
    """
    Holds information about a specific type of Microbial Strain experiment that results in the collection of data. The specific metadata for each type of experiment is controlled by \"template data classes\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'Experiment with Data'})

    core_data_path: UriValue = Field(..., title="CoreDataPath", description="""Portion of the data pathway that will not change as the template is used to generate experimental records (should be network-resolvable)""", json_schema_extra = { "linkml_meta": {'alias': 'core_data_path', 'domain_of': ['ExperimentWithData']} })
    specific_data_path: UriValue = Field(..., title="SpecificDataPath", description="""Portion of the data pathway specific to data from a given experimental record (should be a sub-path of the location specified by `CoreDataPath`)""", json_schema_extra = { "linkml_meta": {'alias': 'specific_data_path', 'domain_of': ['ExperimentWithData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: StringValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class ExperimentWithInstrument(ExperimentWithData):
    """
    Holds information about a specific type of Microbial Strain experiment that uses an instrument. The specific metadata for each type of experiment is controlled by \"template data classes\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'Experiment with Instrument'})

    instrument_id: Optional[ELabItemValue] = Field(None, title="InstrumentID", description="""The instrument used to acquire the data in an experiment (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['ExperimentWithInstrument', 'ExperimentWithInstrumentNoData']} })
    core_data_path: UriValue = Field(..., title="CoreDataPath", description="""Portion of the data pathway that will not change as the template is used to generate experimental records (should be network-resolvable)""", json_schema_extra = { "linkml_meta": {'alias': 'core_data_path', 'domain_of': ['ExperimentWithData']} })
    specific_data_path: UriValue = Field(..., title="SpecificDataPath", description="""Portion of the data pathway specific to data from a given experimental record (should be a sub-path of the location specified by `CoreDataPath`)""", json_schema_extra = { "linkml_meta": {'alias': 'specific_data_path', 'domain_of': ['ExperimentWithData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: StringValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class ExperimentWithInstrumentNoData(Experiment):
    """
    Holds information about a specific type of Microbial Strain experiment that uses an instrument but does not collect data. The specific metadata for each type of experiment is controlled by \"template data classes\"
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'Experiment with Instrument and No Data'})

    instrument_id: Optional[ELabItemValue] = Field(None, title="InstrumentID", description="""The instrument used to acquire the data in an experiment (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['ExperimentWithInstrument', 'ExperimentWithInstrumentNoData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: StringValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class CytoFLEXAcquisition(ExperimentWithInstrument):
    """
    Metadata describing a data acquisition using the CytoFLEX instrument
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'CytoFLEXAcquisitionTemplateNameValue'}},
         'title': 'CytoFLEX_Acquisition'})

    fc_acquisition_threshold_channel: Optional[StringValue] = Field(None, title="FCAcquisitionThresholdChannel", description="""Which channel as named by the manufacturer was used to threshold the data acquisition""", json_schema_extra = { "linkml_meta": {'alias': 'fc_acquisition_threshold_channel',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fc_acquisition_threshold_value: Optional[NumberValue] = Field(None, title="FCAcquisitionThresholdValue", description="""Threshold value in arbitrary units that defines the lower limit of data acquisition in flow cytometry""", json_schema_extra = { "linkml_meta": {'alias': 'fc_acquisition_threshold_value',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fc_flow_rate_setting: Optional[FlowRateValue] = Field(None, title="FCFlowRateSetting", description="""Set flow rate of data acquisition on flow cytometer""", json_schema_extra = { "linkml_meta": {'alias': 'fc_flow_rate_setting',
         'domain_of': ['CytoFLEXAcquisition',
                       'CytoFLEXVolumeCalibration',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fc_injection_mode: Optional[FCInjectionModeValue] = Field(None, title="FCInjectionMode", description="""Sample acquisition format in flow cytometer""", json_schema_extra = { "linkml_meta": {'alias': 'fc_injection_mode',
         'domain_of': ['CytoFLEXAcquisition',
                       'CytoFLEXVolumeCalibration',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fixation_method: Optional[FixationMethodValue] = Field(None, title="FixationMethod", description="""Specific treatment applied to cells to prevent future changes""", json_schema_extra = { "linkml_meta": {'alias': 'fixation_method',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU']} })
    fluorescent_probe: Optional[FluorescentProbeValue] = Field(None, title="FluorescentProbe", description="""Fluorescent probe(s) used in the experiment as (linked item(s) from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'fluorescent_probe',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'MicroscopyAcquisition',
                       'GenericTemplate']} })
    incubation_agitation: Optional[AgitationValue] = Field(None, title="IncubationAgitation", description="""Speed of agitation that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_agitation',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_atmosphere: Optional[IncubationAtmosphereValue] = Field(None, title="IncubationAtmosphere", description="""Atmosphere that cells were incubated in to encourage growth""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_atmosphere',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_duration: Optional[DurationValue] = Field(None, title="IncubationDuration", description="""Length of time that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_duration',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_temperature: Optional[TemperatureValue] = Field(None, title="IncubationTemperature", description="""Temperature at which cells were incubated during an experiment or culture""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_temperature',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    instrument_id: Optional[ELabItemValue] = Field(None, title="InstrumentID", description="""The instrument used to acquire the data in an experiment (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['ExperimentWithInstrument', 'ExperimentWithInstrumentNoData']} })
    core_data_path: UriValue = Field(..., title="CoreDataPath", description="""Portion of the data pathway that will not change as the template is used to generate experimental records (should be network-resolvable)""", json_schema_extra = { "linkml_meta": {'alias': 'core_data_path', 'domain_of': ['ExperimentWithData']} })
    specific_data_path: UriValue = Field(..., title="SpecificDataPath", description="""Portion of the data pathway specific to data from a given experimental record (should be a sub-path of the location specified by `CoreDataPath`)""", json_schema_extra = { "linkml_meta": {'alias': 'specific_data_path', 'domain_of': ['ExperimentWithData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: CytoFLEXAcquisitionTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class NucleicAcidExtraction(ExperimentWithInstrument):
    """
    Metadata describing a nucleic acid extraction experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'NucleicAcidExtractionTemplateNameValue'}},
         'title': 'NucleicAcidExtraction'})

    kit_lot_number: Optional[ELabItemValue] = Field(None, title="KitLotNumber", description="""The lot number of any relevant kits (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'kit_lot_number',
         'domain_of': ['NucleicAcidExtraction',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    nucleic_acid_type: Optional[NucleicAcidTypeValue] = Field(None, title="NucleicAcidType", description="""The type of nucleic acid used in an extraction experiment""", json_schema_extra = { "linkml_meta": {'alias': 'nucleic_acid_type',
         'domain_of': ['NucleicAcidExtraction',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    instrument_id: Optional[ELabItemValue] = Field(None, title="InstrumentID", description="""The instrument used to acquire the data in an experiment (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['ExperimentWithInstrument', 'ExperimentWithInstrumentNoData']} })
    core_data_path: UriValue = Field(..., title="CoreDataPath", description="""Portion of the data pathway that will not change as the template is used to generate experimental records (should be network-resolvable)""", json_schema_extra = { "linkml_meta": {'alias': 'core_data_path', 'domain_of': ['ExperimentWithData']} })
    specific_data_path: UriValue = Field(..., title="SpecificDataPath", description="""Portion of the data pathway specific to data from a given experimental record (should be a sub-path of the location specified by `CoreDataPath`)""", json_schema_extra = { "linkml_meta": {'alias': 'specific_data_path', 'domain_of': ['ExperimentWithData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: NucleicAcidExtractionTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class CellCultureInBroth(Experiment):
    """
    Metadata describing a cell culture experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'CellCultureInBrothTemplateNameValue'}},
         'title': 'Cell Culture in Broth'})

    growth_media_name: Optional[ELabItemValue] = Field(None, title="GrowthMediaName", description="""Name of media used to culture cells (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'growth_media_name',
         'domain_of': ['CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_agitation: Optional[AgitationValue] = Field(None, title="IncubationAgitation", description="""Speed of agitation that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_agitation',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_atmosphere: Optional[IncubationAtmosphereValue] = Field(None, title="IncubationAtmosphere", description="""Atmosphere that cells were incubated in to encourage growth""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_atmosphere',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_duration: Optional[DurationValue] = Field(None, title="IncubationDuration", description="""Length of time that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_duration',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_temperature: Optional[TemperatureValue] = Field(None, title="IncubationTemperature", description="""Temperature at which cells were incubated during an experiment or culture""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_temperature',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: CellCultureInBrothTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class CytoFLEXVolumeCalibration(ExperimentWithInstrumentNoData):
    """
    Metadata describing a volume calibration using the CytoFLEX instrument
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'CytoFLEXVolumeCalibrationTemplateNameValue'}},
         'title': 'CytoFLEX_VolumeCalibration'})

    fc_flow_rate_setting: Optional[FlowRateValue] = Field(None, title="FCFlowRateSetting", description="""Set flow rate of data acquisition on flow cytometer""", json_schema_extra = { "linkml_meta": {'alias': 'fc_flow_rate_setting',
         'domain_of': ['CytoFLEXAcquisition',
                       'CytoFLEXVolumeCalibration',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fc_injection_mode: Optional[FCInjectionModeValue] = Field(None, title="FCInjectionMode", description="""Sample acquisition format in flow cytometer""", json_schema_extra = { "linkml_meta": {'alias': 'fc_injection_mode',
         'domain_of': ['CytoFLEXAcquisition',
                       'CytoFLEXVolumeCalibration',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    passed_volume_calibration: Optional[BooleanValue] = Field(None, title="PassedVolumeCalibration", description="""(?) The volume that is passed during a volume calibration""", json_schema_extra = { "linkml_meta": {'alias': 'passed_volume_calibration',
         'domain_of': ['CytoFLEXVolumeCalibration', 'GenericTemplate'],
         'todos': ['double check description']} })
    percent_volume_deviation: Optional[UnitlessValue] = Field(None, title="PercentVolumeDeviation", description="""The volume deviation (measured volume divided by target volume) from a calibration experiment""", json_schema_extra = { "linkml_meta": {'alias': 'percent_volume_deviation',
         'domain_of': ['CytoFLEXVolumeCalibration', 'GenericTemplate']} })
    instrument_id: Optional[ELabItemValue] = Field(None, title="InstrumentID", description="""The instrument used to acquire the data in an experiment (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['ExperimentWithInstrument', 'ExperimentWithInstrumentNoData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: CytoFLEXVolumeCalibrationTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class GenericTemplateDeprecated(ExperimentWithInstrument):
    """
    A retired version of a generic experiment template used to create other templates
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'deprecated': '(2024 June) this is no longer used, use GenericTemplate '
                       'instead',
         'deprecated_element_has_exact_replacement': 'GenericTemplate',
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'GenericTemplate_Deprecated'})

    acquisition_time: Optional[DurationValue] = Field(None, title="AcquisitionTime", description="""Data acquisition time as set by instrument""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_time',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    acquisition_volume: Optional[VolumeValue] = Field(None, title="AcquisitionVolume", description="""Data acquisition volume as set by instrument""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_volume',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    bead_lot_number_concentration_qc: Optional[StringValue] = Field(None, title="BeadLotNumber_ConcentrationQC", description="""Lot number of beads used for quality control of concentration measurements""", json_schema_extra = { "linkml_meta": {'alias': 'bead_lot_number_concentration_qc',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    bead_lot_number_size_qc: Optional[StringValue] = Field(None, title="BeadLotNumber_SizeQC", description="""Lot number of beads used for quality control of size measurements""", json_schema_extra = { "linkml_meta": {'alias': 'bead_lot_number_size_qc',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    cell_volume: Optional[VolumeValue] = Field(None, title="CellVolume", description="""Volume of cell stock added to acquisition vessel""", json_schema_extra = { "linkml_meta": {'alias': 'cell_volume',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    cfu_method: Optional[CFUMethodValue] = Field(None, title="CFUMethod", description="""Describes deposition format of cells on agar plate""", json_schema_extra = { "linkml_meta": {'alias': 'cfu_method',
         'domain_of': ['GenericTemplateDeprecated', 'GenericTemplate', 'CFU']} })
    coulter_aperture_size: Optional[LengthValue] = Field(None, title="CoulterApertureSize", description="""Aperture installed on Coulter counter during measurement""", json_schema_extra = { "linkml_meta": {'alias': 'coulter_aperture_size',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    diluent_name: Optional[ELabItemValue] = Field(None, title="DiluentName", description="""Which diluent was used to suspend cells for acquisition (linked item)""", json_schema_extra = { "linkml_meta": {'alias': 'diluent_name',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    diluent_volume: Optional[VolumeValue] = Field(None, title="DiluentVolume", description="""Volume of diluent added to acquisition vessel""", json_schema_extra = { "linkml_meta": {'alias': 'diluent_volume',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    error_flag: Optional[BooleanValue] = Field(None, title="ErrorFlag", description="""Indicates if a known error appears in the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'error_flag',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    fc_acquisition_count_target: Optional[CountValue] = Field(None, title="FCAcquisitionCountTarget", description="""Set number of events to acquire in a particular gate on flow cytometer""", json_schema_extra = { "linkml_meta": {'alias': 'fc_acquisition_count_target',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    fc_acquisition_threshold_channel: Optional[StringValue] = Field(None, title="FCAcquisitionThresholdChannel", description="""Which channel as named by the manufacturer was used to threshold the data acquisition""", json_schema_extra = { "linkml_meta": {'alias': 'fc_acquisition_threshold_channel',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fc_acquisition_threshold_value: Optional[NumberValue] = Field(None, title="FCAcquisitionThresholdValue", description="""Threshold value in arbitrary units that defines the lower limit of data acquisition in flow cytometry""", json_schema_extra = { "linkml_meta": {'alias': 'fc_acquisition_threshold_value',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fc_flow_rate_setting: Optional[FlowRateValue] = Field(None, title="FCFlowRateSetting", description="""Set flow rate of data acquisition on flow cytometer""", json_schema_extra = { "linkml_meta": {'alias': 'fc_flow_rate_setting',
         'domain_of': ['CytoFLEXAcquisition',
                       'CytoFLEXVolumeCalibration',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fc_fluorescent_channels: Optional[StringValue] = Field(None, title="FCFluorescentChannels", description="""List of fluorescent channels acquired during a flow cytometry experiment as named by the manufacturer (separated by semicolons)""", json_schema_extra = { "linkml_meta": {'alias': 'fc_fluorescent_channels',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    fc_injection_mode: Optional[FCInjectionModeValue] = Field(None, title="FCInjectionMode", description="""Sample acquisition format in flow cytometer""", json_schema_extra = { "linkml_meta": {'alias': 'fc_injection_mode',
         'domain_of': ['CytoFLEXAcquisition',
                       'CytoFLEXVolumeCalibration',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fixation_method: Optional[FixationMethodValue] = Field(None, title="FixationMethod", description="""Specific treatment applied to cells to prevent future changes""", json_schema_extra = { "linkml_meta": {'alias': 'fixation_method',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU']} })
    fluorescent_probe: Optional[FluorescentProbeValue] = Field(None, title="FluorescentProbe", description="""Fluorescent probe(s) used in the experiment as (linked item(s) from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'fluorescent_probe',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'MicroscopyAcquisition',
                       'GenericTemplate']} })
    growth_duration: Optional[DurationValue] = Field(None, title="GrowthDuration", description="""Time that cells were incubated to encourage growth""", json_schema_extra = { "linkml_meta": {'alias': 'growth_duration',
         'deprecated': '(2024 June) unnecessary and unused',
         'domain_of': ['GenericTemplateDeprecated']} })
    growth_media_name: Optional[ELabItemValue] = Field(None, title="GrowthMediaName", description="""Name of media used to culture cells (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'growth_media_name',
         'domain_of': ['CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_agitation: Optional[AgitationValue] = Field(None, title="IncubationAgitation", description="""Speed of agitation that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_agitation',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_atmosphere: Optional[IncubationAtmosphereValue] = Field(None, title="IncubationAtmosphere", description="""Atmosphere that cells were incubated in to encourage growth""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_atmosphere',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_duration: Optional[DurationValue] = Field(None, title="IncubationDuration", description="""Length of time that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_duration',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_temperature: Optional[TemperatureValue] = Field(None, title="IncubationTemperature", description="""Temperature at which cells were incubated during an experiment or culture""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_temperature',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    kit_lot_number: Optional[ELabItemValue] = Field(None, title="KitLotNumber", description="""The lot number of any relevant kits (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'kit_lot_number',
         'domain_of': ['NucleicAcidExtraction',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    labcas_data_acquisition_date: Optional[DateValue] = Field(None, title="LabCAS-DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'labcas_data_acquisition_date',
         'deprecated': '(2024 June) this is too specific, use data_acquisition_date '
                       'instead',
         'deprecated_element_has_exact_replacement': 'data_acquisition_date',
         'domain_of': ['GenericTemplateDeprecated']} })
    labcas_instrument: Optional[LabCASInstrumentValue] = Field(None, title="LabCAS-Instrument", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'labcas_instrument',
         'deprecated': '(2024 June) this is too specific, use instrument_id instead',
         'deprecated_element_has_exact_replacement': 'instrument_id',
         'domain_of': ['GenericTemplateDeprecated']} })
    labcas_microbial_material_id: Optional[LabCASMicrobialMaterialIDValue] = Field(None, title="LabCAS-MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'labcas_microbial_material_id',
         'deprecated': '(2024 June) this is too specific, use microbial_material_id '
                       'instead',
         'deprecated_element_has_exact_replacement': 'microbial_material_id',
         'domain_of': ['GenericTemplateDeprecated']} })
    labcas_operator: Optional[LabCASOperatorValue] = Field(None, title="LabCAS-Operator", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'labcas_operator',
         'deprecated': '(2024 June) this is too specific, use operator_id instead',
         'deprecated_element_has_exact_replacement': 'operator_id',
         'domain_of': ['GenericTemplateDeprecated']} })
    labcas_project: Optional[LabCASProjectValue] = Field(None, title="LabCAS-Project", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'labcas_project',
         'deprecated': '(2024 June) this is too specific, use project_id instead',
         'deprecated_element_has_exact_replacement': 'project_id',
         'domain_of': ['GenericTemplateDeprecated']} })
    library_prep: Optional[StringValue] = Field(None, title="LibraryPrep", description="""The name of a specific kit used for sequencing preparation steps""", json_schema_extra = { "linkml_meta": {'alias': 'library_prep',
         'domain_of': ['GenericTemplateDeprecated', 'GenericTemplate']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    nucleic_acid_type: Optional[NucleicAcidTypeValue] = Field(None, title="NucleicAcidType", description="""The type of nucleic acid used in an extraction experiment""", json_schema_extra = { "linkml_meta": {'alias': 'nucleic_acid_type',
         'domain_of': ['NucleicAcidExtraction',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    objective: Optional[ObjectivesValue] = Field(None, title="Objective", description="""The microscope objectives used in a microscopy acquisition experiment""", json_schema_extra = { "linkml_meta": {'alias': 'objective',
         'domain_of': ['GenericTemplateDeprecated',
                       'MicroscopyAcquisition',
                       'GenericTemplate']} })
    qc_reagent_lot_number: Optional[StringValue] = Field(None, title="QCReagentLotNumber", description="""The lot number for a QC reagent (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'qc_reagent_lot_number',
         'deprecated': '(2024 June) this metadata term was determined to be unneeded, '
                       'do not use',
         'domain_of': ['GenericTemplateDeprecated']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    transmission_mode: Optional[TransmissionModeValue] = Field(None, title="TransmissionMode", description="""The type (modality) of a microscopy acquisition experiment""", json_schema_extra = { "linkml_meta": {'alias': 'transmission_mode',
         'deprecated': '(2024 June) this is too specific, use modalities instead',
         'deprecated_element_has_exact_replacement': 'modalities',
         'domain_of': ['GenericTemplateDeprecated']} })
    instrument_id: Optional[ELabItemValue] = Field(None, title="InstrumentID", description="""The instrument used to acquire the data in an experiment (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['ExperimentWithInstrument', 'ExperimentWithInstrumentNoData']} })
    core_data_path: UriValue = Field(..., title="CoreDataPath", description="""Portion of the data pathway that will not change as the template is used to generate experimental records (should be network-resolvable)""", json_schema_extra = { "linkml_meta": {'alias': 'core_data_path', 'domain_of': ['ExperimentWithData']} })
    specific_data_path: UriValue = Field(..., title="SpecificDataPath", description="""Portion of the data pathway specific to data from a given experimental record (should be a sub-path of the location specified by `CoreDataPath`)""", json_schema_extra = { "linkml_meta": {'alias': 'specific_data_path', 'domain_of': ['ExperimentWithData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: StringValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class FormaldehydeFixation(Experiment):
    """
    Metadata describing a formaldehyde fixation experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'FormaldehydeFixationTemplateNameValue'}},
         'title': 'FormaldehydeFixation'})

    fixation_method: Optional[FixationMethodValue] = Field(None, title="FixationMethod", description="""Specific treatment applied to cells to prevent future changes""", json_schema_extra = { "linkml_meta": {'alias': 'fixation_method',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU']} })
    incubation_agitation: Optional[AgitationValue] = Field(None, title="IncubationAgitation", description="""Speed of agitation that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_agitation',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_atmosphere: Optional[IncubationAtmosphereValue] = Field(None, title="IncubationAtmosphere", description="""Atmosphere that cells were incubated in to encourage growth""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_atmosphere',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_duration: Optional[DurationValue] = Field(None, title="IncubationDuration", description="""Length of time that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_duration',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_temperature: Optional[TemperatureValue] = Field(None, title="IncubationTemperature", description="""Temperature at which cells were incubated during an experiment or culture""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_temperature',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: FormaldehydeFixationTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class MicroscopyAcquisition(ExperimentWithInstrument):
    """
    Metadata describing a microscopy acquisition experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'MicroscopyAcquisitionTemplateNameValue'}},
         'title': 'Microscopy_Acquisition'})

    fixation_method: Optional[FixationMethodValue] = Field(None, title="FixationMethod", description="""Specific treatment applied to cells to prevent future changes""", json_schema_extra = { "linkml_meta": {'alias': 'fixation_method',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU']} })
    fluorescent_probe: Optional[FluorescentProbeValue] = Field(None, title="FluorescentProbe", description="""Fluorescent probe(s) used in the experiment as (linked item(s) from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'fluorescent_probe',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'MicroscopyAcquisition',
                       'GenericTemplate']} })
    incubation_agitation: Optional[AgitationValue] = Field(None, title="IncubationAgitation", description="""Speed of agitation that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_agitation',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_atmosphere: Optional[IncubationAtmosphereValue] = Field(None, title="IncubationAtmosphere", description="""Atmosphere that cells were incubated in to encourage growth""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_atmosphere',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_duration: Optional[DurationValue] = Field(None, title="IncubationDuration", description="""Length of time that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_duration',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_temperature: Optional[TemperatureValue] = Field(None, title="IncubationTemperature", description="""Temperature at which cells were incubated during an experiment or culture""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_temperature',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    modalities: Optional[ModalitiesValue] = Field(None, title="Modalities", description="""The type (modality) of a microscopy acquisition experiment""", json_schema_extra = { "linkml_meta": {'alias': 'modalities',
         'domain_of': ['MicroscopyAcquisition', 'GenericTemplate']} })
    objective: Optional[ObjectivesValue] = Field(None, title="Objective", description="""The microscope objectives used in a microscopy acquisition experiment""", json_schema_extra = { "linkml_meta": {'alias': 'objective',
         'domain_of': ['GenericTemplateDeprecated',
                       'MicroscopyAcquisition',
                       'GenericTemplate']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    series_image_types: Optional[SeriesImageTypesValue] = Field(None, title="SeriesImageTypes", description="""The types of series images acquired in an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'series_image_types',
         'domain_of': ['MicroscopyAcquisition', 'GenericTemplate']} })
    series_images: Optional[BooleanValue] = Field(None, title="SeriesImages", description="""Whether series images were acquired in an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'series_images',
         'domain_of': ['MicroscopyAcquisition', 'GenericTemplate']} })
    single_images: Optional[BooleanValue] = Field(None, title="SingleImages", description="""Whether single images were acquired in an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'single_images',
         'domain_of': ['MicroscopyAcquisition', 'GenericTemplate']} })
    instrument_id: Optional[ELabItemValue] = Field(None, title="InstrumentID", description="""The instrument used to acquire the data in an experiment (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['ExperimentWithInstrument', 'ExperimentWithInstrumentNoData']} })
    core_data_path: UriValue = Field(..., title="CoreDataPath", description="""Portion of the data pathway that will not change as the template is used to generate experimental records (should be network-resolvable)""", json_schema_extra = { "linkml_meta": {'alias': 'core_data_path', 'domain_of': ['ExperimentWithData']} })
    specific_data_path: UriValue = Field(..., title="SpecificDataPath", description="""Portion of the data pathway specific to data from a given experimental record (should be a sub-path of the location specified by `CoreDataPath`)""", json_schema_extra = { "linkml_meta": {'alias': 'specific_data_path', 'domain_of': ['ExperimentWithData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: MicroscopyAcquisitionTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class GenericTemplate(ExperimentWithInstrument):
    """
    A generic experiment template used to help create more specific experiment templates. This template should not be used directly.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'GenericTemplate'})

    cfu_method: Optional[CFUMethodValue] = Field(None, title="CFUMethod", description="""Describes deposition format of cells on agar plate""", json_schema_extra = { "linkml_meta": {'alias': 'cfu_method',
         'domain_of': ['GenericTemplateDeprecated', 'GenericTemplate', 'CFU']} })
    fc_acquisition_threshold_channel: Optional[StringValue] = Field(None, title="FCAcquisitionThresholdChannel", description="""Which channel as named by the manufacturer was used to threshold the data acquisition""", json_schema_extra = { "linkml_meta": {'alias': 'fc_acquisition_threshold_channel',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fc_acquisition_threshold_value: Optional[NumberValue] = Field(None, title="FCAcquisitionThresholdValue", description="""Threshold value in arbitrary units that defines the lower limit of data acquisition in flow cytometry""", json_schema_extra = { "linkml_meta": {'alias': 'fc_acquisition_threshold_value',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fc_flow_rate_setting: Optional[FlowRateValue] = Field(None, title="FCFlowRateSetting", description="""Set flow rate of data acquisition on flow cytometer""", json_schema_extra = { "linkml_meta": {'alias': 'fc_flow_rate_setting',
         'domain_of': ['CytoFLEXAcquisition',
                       'CytoFLEXVolumeCalibration',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fc_injection_mode: Optional[FCInjectionModeValue] = Field(None, title="FCInjectionMode", description="""Sample acquisition format in flow cytometer""", json_schema_extra = { "linkml_meta": {'alias': 'fc_injection_mode',
         'domain_of': ['CytoFLEXAcquisition',
                       'CytoFLEXVolumeCalibration',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    fixation_method: Optional[FixationMethodValue] = Field(None, title="FixationMethod", description="""Specific treatment applied to cells to prevent future changes""", json_schema_extra = { "linkml_meta": {'alias': 'fixation_method',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU']} })
    fluorescent_probe: Optional[FluorescentProbeValue] = Field(None, title="FluorescentProbe", description="""Fluorescent probe(s) used in the experiment as (linked item(s) from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'fluorescent_probe',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'MicroscopyAcquisition',
                       'GenericTemplate']} })
    growth_media_name: Optional[ELabItemValue] = Field(None, title="GrowthMediaName", description="""Name of media used to culture cells (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'growth_media_name',
         'domain_of': ['CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_agitation: Optional[AgitationValue] = Field(None, title="IncubationAgitation", description="""Speed of agitation that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_agitation',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_atmosphere: Optional[IncubationAtmosphereValue] = Field(None, title="IncubationAtmosphere", description="""Atmosphere that cells were incubated in to encourage growth""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_atmosphere',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_duration: Optional[DurationValue] = Field(None, title="IncubationDuration", description="""Length of time that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_duration',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_temperature: Optional[TemperatureValue] = Field(None, title="IncubationTemperature", description="""Temperature at which cells were incubated during an experiment or culture""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_temperature',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    kit_lot_number: Optional[ELabItemValue] = Field(None, title="KitLotNumber", description="""The lot number of any relevant kits (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'kit_lot_number',
         'domain_of': ['NucleicAcidExtraction',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    library_prep: Optional[StringValue] = Field(None, title="LibraryPrep", description="""The name of a specific kit used for sequencing preparation steps""", json_schema_extra = { "linkml_meta": {'alias': 'library_prep',
         'domain_of': ['GenericTemplateDeprecated', 'GenericTemplate']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    modalities: Optional[ModalitiesValue] = Field(None, title="Modalities", description="""The type (modality) of a microscopy acquisition experiment""", json_schema_extra = { "linkml_meta": {'alias': 'modalities',
         'domain_of': ['MicroscopyAcquisition', 'GenericTemplate']} })
    nucleic_acid_type: Optional[NucleicAcidTypeValue] = Field(None, title="NucleicAcidType", description="""The type of nucleic acid used in an extraction experiment""", json_schema_extra = { "linkml_meta": {'alias': 'nucleic_acid_type',
         'domain_of': ['NucleicAcidExtraction',
                       'GenericTemplateDeprecated',
                       'GenericTemplate']} })
    objective: Optional[ObjectivesValue] = Field(None, title="Objective", description="""The microscope objectives used in a microscopy acquisition experiment""", json_schema_extra = { "linkml_meta": {'alias': 'objective',
         'domain_of': ['GenericTemplateDeprecated',
                       'MicroscopyAcquisition',
                       'GenericTemplate']} })
    passed_volume_calibration: Optional[BooleanValue] = Field(None, title="PassedVolumeCalibration", description="""(?) The volume that is passed during a volume calibration""", json_schema_extra = { "linkml_meta": {'alias': 'passed_volume_calibration',
         'domain_of': ['CytoFLEXVolumeCalibration', 'GenericTemplate'],
         'todos': ['double check description']} })
    percent_volume_deviation: Optional[UnitlessValue] = Field(None, title="PercentVolumeDeviation", description="""The volume deviation (measured volume divided by target volume) from a calibration experiment""", json_schema_extra = { "linkml_meta": {'alias': 'percent_volume_deviation',
         'domain_of': ['CytoFLEXVolumeCalibration', 'GenericTemplate']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    series_image_types: Optional[SeriesImageTypesValue] = Field(None, title="SeriesImageTypes", description="""The types of series images acquired in an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'series_image_types',
         'domain_of': ['MicroscopyAcquisition', 'GenericTemplate']} })
    series_images: Optional[BooleanValue] = Field(None, title="SeriesImages", description="""Whether series images were acquired in an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'series_images',
         'domain_of': ['MicroscopyAcquisition', 'GenericTemplate']} })
    single_images: Optional[BooleanValue] = Field(None, title="SingleImages", description="""Whether single images were acquired in an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'single_images',
         'domain_of': ['MicroscopyAcquisition', 'GenericTemplate']} })
    instrument_id: Optional[ELabItemValue] = Field(None, title="InstrumentID", description="""The instrument used to acquire the data in an experiment (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['ExperimentWithInstrument', 'ExperimentWithInstrumentNoData']} })
    core_data_path: UriValue = Field(..., title="CoreDataPath", description="""Portion of the data pathway that will not change as the template is used to generate experimental records (should be network-resolvable)""", json_schema_extra = { "linkml_meta": {'alias': 'core_data_path', 'domain_of': ['ExperimentWithData']} })
    specific_data_path: UriValue = Field(..., title="SpecificDataPath", description="""Portion of the data pathway specific to data from a given experimental record (should be a sub-path of the location specified by `CoreDataPath`)""", json_schema_extra = { "linkml_meta": {'alias': 'specific_data_path', 'domain_of': ['ExperimentWithData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: StringValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class CoulterAcquisition(ExperimentWithInstrument):
    """
    Metadata describing a Coulter counter acquisition experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'CoulterAcquisitionTemplateNameValue'}},
         'title': 'Coulter_Acquisition'})

    fixation_method: Optional[FixationMethodValue] = Field(None, title="FixationMethod", description="""Specific treatment applied to cells to prevent future changes""", json_schema_extra = { "linkml_meta": {'alias': 'fixation_method',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    instrument_id: Optional[ELabItemValue] = Field(None, title="InstrumentID", description="""The instrument used to acquire the data in an experiment (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['ExperimentWithInstrument', 'ExperimentWithInstrumentNoData']} })
    core_data_path: UriValue = Field(..., title="CoreDataPath", description="""Portion of the data pathway that will not change as the template is used to generate experimental records (should be network-resolvable)""", json_schema_extra = { "linkml_meta": {'alias': 'core_data_path', 'domain_of': ['ExperimentWithData']} })
    specific_data_path: UriValue = Field(..., title="SpecificDataPath", description="""Portion of the data pathway specific to data from a given experimental record (should be a sub-path of the location specified by `CoreDataPath`)""", json_schema_extra = { "linkml_meta": {'alias': 'specific_data_path', 'domain_of': ['ExperimentWithData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: CoulterAcquisitionTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class BactoBoxAcquisition(ExperimentWithInstrument):
    """
    Metadata describing a data acquisition experiment using the BactoBox
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'BactoBoxAcquisitionTemplateNameValue'}},
         'title': 'BactoBox_Acquisition'})

    fixation_method: Optional[FixationMethodValue] = Field(None, title="FixationMethod", description="""Specific treatment applied to cells to prevent future changes""", json_schema_extra = { "linkml_meta": {'alias': 'fixation_method',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    instrument_id: Optional[ELabItemValue] = Field(None, title="InstrumentID", description="""The instrument used to acquire the data in an experiment (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_id',
         'domain_of': ['ExperimentWithInstrument', 'ExperimentWithInstrumentNoData']} })
    core_data_path: UriValue = Field(..., title="CoreDataPath", description="""Portion of the data pathway that will not change as the template is used to generate experimental records (should be network-resolvable)""", json_schema_extra = { "linkml_meta": {'alias': 'core_data_path', 'domain_of': ['ExperimentWithData']} })
    specific_data_path: UriValue = Field(..., title="SpecificDataPath", description="""Portion of the data pathway specific to data from a given experimental record (should be a sub-path of the location specified by `CoreDataPath`)""", json_schema_extra = { "linkml_meta": {'alias': 'specific_data_path', 'domain_of': ['ExperimentWithData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: BactoBoxAcquisitionTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class LogCOMETSamplePrep(Experiment):
    """
    Metadata describing a sample preparation process for a LOGComet experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'LogCOMETSamplePrepTemplateNameValue'}},
         'title': 'LogCOMET_SamplePrep'})

    fixation_method: Optional[FixationMethodValue] = Field(None, title="FixationMethod", description="""Specific treatment applied to cells to prevent future changes""", json_schema_extra = { "linkml_meta": {'alias': 'fixation_method',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: LogCOMETSamplePrepTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class CFU(ExperimentWithData):
    """
    Metadata describing a colony forming unit counting experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'CFUTemplateNameValue'}},
         'title': 'CFU'})

    cfu_method: Optional[CFUMethodValue] = Field(None, title="CFUMethod", description="""Describes deposition format of cells on agar plate""", json_schema_extra = { "linkml_meta": {'alias': 'cfu_method',
         'domain_of': ['GenericTemplateDeprecated', 'GenericTemplate', 'CFU']} })
    fixation_method: Optional[FixationMethodValue] = Field(None, title="FixationMethod", description="""Specific treatment applied to cells to prevent future changes""", json_schema_extra = { "linkml_meta": {'alias': 'fixation_method',
         'domain_of': ['CytoFLEXAcquisition',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU']} })
    growth_media_name: Optional[ELabItemValue] = Field(None, title="GrowthMediaName", description="""Name of media used to culture cells (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'growth_media_name',
         'domain_of': ['CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_atmosphere: Optional[IncubationAtmosphereValue] = Field(None, title="IncubationAtmosphere", description="""Atmosphere that cells were incubated in to encourage growth""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_atmosphere',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_duration: Optional[DurationValue] = Field(None, title="IncubationDuration", description="""Length of time that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_duration',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_temperature: Optional[TemperatureValue] = Field(None, title="IncubationTemperature", description="""Temperature at which cells were incubated during an experiment or culture""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_temperature',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    core_data_path: UriValue = Field(..., title="CoreDataPath", description="""Portion of the data pathway that will not change as the template is used to generate experimental records (should be network-resolvable)""", json_schema_extra = { "linkml_meta": {'alias': 'core_data_path', 'domain_of': ['ExperimentWithData']} })
    specific_data_path: UriValue = Field(..., title="SpecificDataPath", description="""Portion of the data pathway specific to data from a given experimental record (should be a sub-path of the location specified by `CoreDataPath`)""", json_schema_extra = { "linkml_meta": {'alias': 'specific_data_path', 'domain_of': ['ExperimentWithData']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: CFUTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class DifcoAmendedSporulationAgarProtocol(Experiment):
    """
    Metadata describing the preparation process for amended sporulation agar
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'DifcoAmendedSporulationAgarProtocolTemplateNameValue'}},
         'title': 'Difco Amended Sporulation Agar (ASA) Protocol'})

    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: DifcoAmendedSporulationAgarProtocolTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class InitiateGrowthOfBSpizizenii(Experiment):
    """
    Metadata describing an initiate growth experiment of B. spizizenii
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'InitiateGrowthOfBSpizizeniiTemplateNameValue'}},
         'title': 'Initiate Growth of B. spizizenii'})

    growth_media_name: Optional[ELabItemValue] = Field(None, title="GrowthMediaName", description="""Name of media used to culture cells (linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'growth_media_name',
         'domain_of': ['CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_agitation: Optional[AgitationValue] = Field(None, title="IncubationAgitation", description="""Speed of agitation that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_agitation',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_atmosphere: Optional[IncubationAtmosphereValue] = Field(None, title="IncubationAtmosphere", description="""Atmosphere that cells were incubated in to encourage growth""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_atmosphere',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_duration: Optional[DurationValue] = Field(None, title="IncubationDuration", description="""Length of time that cells were incubated during an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_duration',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    incubation_temperature: Optional[TemperatureValue] = Field(None, title="IncubationTemperature", description="""Temperature at which cells were incubated during an experiment or culture""", json_schema_extra = { "linkml_meta": {'alias': 'incubation_temperature',
         'domain_of': ['CytoFLEXAcquisition',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    microbial_material_id: Optional[MicrobialMaterialIDValue] = Field(None, title="MicrobialMaterialID", description="""Cell material(s) used in experiment as named in the eLabFTW database (linked items)""", json_schema_extra = { "linkml_meta": {'alias': 'microbial_material_id',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    sample_purpose_codes: Optional[SamplePurposeCodesValue] = Field(None, title="SamplePurposeCodes", description="""The types of samples acquired in an experiment (from a controlled list)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_purpose_codes',
         'domain_of': ['CytoFLEXAcquisition',
                       'NucleicAcidExtraction',
                       'CellCultureInBroth',
                       'GenericTemplateDeprecated',
                       'FormaldehydeFixation',
                       'MicroscopyAcquisition',
                       'GenericTemplate',
                       'CoulterAcquisition',
                       'BactoBoxAcquisition',
                       'LogCOMETSamplePrep',
                       'CFU',
                       'InitiateGrowthOfBSpizizenii']} })
    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: InitiateGrowthOfBSpizizeniiTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class SlideCleaning(Experiment):
    """
    Metadata describing an experiment preparing microscopy slides for microbial work
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'template_name': {'name': 'template_name',
                                          'range': 'SlideCleaningTemplateNameValue'}},
         'title': 'SlideCleaning'})

    data_acquisition_date: DateValue = Field(..., title="DataAcquisitionDate", description="""Date on which data were acquired according to eLabFTW record""", json_schema_extra = { "linkml_meta": {'alias': 'data_acquisition_date', 'domain_of': ['Experiment']} })
    elab_experiment: ELabExperiment = Field(..., title="ELabFTW Experiment", description="""A self-reference to this experiment record""", json_schema_extra = { "linkml_meta": {'alias': 'elab_experiment', 'domain_of': ['Experiment']} })
    operator_id: OperatorIDValue = Field(..., title="OperatorID", description="""Instrument operator during an experiment (a linked item from ELabFTW)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['Experiment']} })
    project_id: ELabItemValue = Field(..., title="ProjectID", description="""The project that an experiment supports (link to an ELabFTW item)""", json_schema_extra = { "linkml_meta": {'alias': 'project_id', 'domain_of': ['Experiment']} })
    template_name: SlideCleaningTemplateNameValue = Field(..., title="TemplateName", description="""The name of the template used to collect metadata for an experiment in ELabFTW. This value controls what specific metadata fields are allowed.""", json_schema_extra = { "linkml_meta": {'alias': 'template_name', 'domain_of': ['Experiment']} })


class BooleanValue(ConfiguredBaseModel):
    """
    A class to hold a boolean value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value', 'range': 'boolean'}},
         'title': 'Boolean Value'})

    value: bool = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class NumberValue(ConfiguredBaseModel):
    """
    A class to hold a numerical value with a free-text string as a unit
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'unit': {'name': 'unit', 'range': 'string', 'required': False},
                        'value': {'name': 'value', 'range': 'decimal'}},
         'title': 'Number Value'})

    value: Decimal = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })
    unit: Optional[str] = Field(None, title="unit", description="""The unit corresponding to a metadata value""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['NumberValue']} })


class StringValue(ConfiguredBaseModel):
    """
    A class to hold a string value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value', 'range': 'string'}},
         'title': 'String Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class UriValue(ConfiguredBaseModel):
    """
    A class to hold a string value that is a URI
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value', 'range': 'uri'}},
         'title': 'Uri Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class DateValue(ConfiguredBaseModel):
    """
    A class to hold a date value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value', 'range': 'date'}},
         'title': 'Date Value'})

    value: date = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class ArrayValue(ConfiguredBaseModel):
    """
    A class to hold an array of values
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'inlined': False,
                                  'multivalued': True,
                                  'name': 'value'}},
         'title': 'Array Value'})

    value: List[str] = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class ELabItemValue(ConfiguredBaseModel):
    """
    A class to hold a reference to an item record in ELabFTW
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'inlined': True,
                                  'name': 'value',
                                  'range': 'ELabItem'}},
         'title': 'ELabFTW Item Value'})

    value: ELabItem = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class VolumeValue(NumberValue):
    """
    A class to hold a numerical value representing a volumetric measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'unit': {'description': 'The volume unit corresponding to a '
                                                'metadata value',
                                 'name': 'unit',
                                 'range': 'VolumeUnitEnum',
                                 'required': True}},
         'title': 'Volume Value'})

    value: Decimal = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })
    unit: VolumeUnitEnum = Field(..., title="unit", description="""The volume unit corresponding to a metadata value""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['NumberValue']} })


class LengthValue(NumberValue):
    """
    A class to hold a numerical value representing a linear measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'unit': {'description': 'The length unit corresponding to a '
                                                'metadata value',
                                 'name': 'unit',
                                 'range': 'LengthUnitEnum',
                                 'required': True}},
         'title': 'Length Value'})

    value: Decimal = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })
    unit: LengthUnitEnum = Field(..., title="unit", description="""The length unit corresponding to a metadata value""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['NumberValue']} })


class DurationValue(NumberValue):
    """
    A class to hold a numerical value representing a time duration measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'unit': {'description': 'The time duration unit corresponding '
                                                'to a metadata value',
                                 'name': 'unit',
                                 'range': 'DurationUnitEnum',
                                 'required': True}},
         'title': 'Duration Value'})

    value: Decimal = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })
    unit: DurationUnitEnum = Field(..., title="unit", description="""The time duration unit corresponding to a metadata value""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['NumberValue']} })


class TemperatureValue(NumberValue):
    """
    A class to hold a numerical value representing a temperature measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'unit': {'description': 'The temperature unit corresponding to '
                                                'a metadata value',
                                 'name': 'unit',
                                 'range': 'TemperatureUnitEnum',
                                 'required': True}},
         'title': 'Temperature Value'})

    value: Decimal = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })
    unit: TemperatureUnitEnum = Field(..., title="unit", description="""The temperature unit corresponding to a metadata value""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['NumberValue']} })


class CountValue(NumberValue):
    """
    A class to hold a numerical value representing a counting measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'unit': {'description': 'The count unit corresponding to a '
                                                'metadata value',
                                 'name': 'unit',
                                 'range': 'CountUnitEnum',
                                 'required': True}},
         'title': 'Count Value'})

    value: Decimal = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })
    unit: CountUnitEnum = Field(..., title="unit", description="""The count unit corresponding to a metadata value""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['NumberValue']} })


class FlowRateValue(NumberValue):
    """
    A class to hold a numerical value representing a flow rate measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'unit': {'description': 'The flow rate unit corresponding to a '
                                                'metadata value',
                                 'name': 'unit',
                                 'range': 'FlowRateUnitEnum',
                                 'required': True}},
         'title': 'Flow Rate Value'})

    value: Decimal = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })
    unit: FlowRateUnitEnum = Field(..., title="unit", description="""The flow rate unit corresponding to a metadata value""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['NumberValue']} })


class AgitationValue(NumberValue):
    """
    A class to hold a numerical value representing an agitation speed
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'unit': {'description': 'The agitation speed unit '
                                                'corresponding to a metadata value',
                                 'name': 'unit',
                                 'range': 'AgitationEnum',
                                 'required': True}},
         'title': 'Agitation Value'})

    value: Decimal = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })
    unit: AgitationEnum = Field(..., title="unit", description="""The agitation speed unit corresponding to a metadata value""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['NumberValue']} })


class UnitlessValue(NumberValue):
    """
    A class to hold an explicitly unitless numerical value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'unit': {'description': 'The word "Unitless" corresponding to '
                                                'a unitless metadata value',
                                 'name': 'unit',
                                 'range': 'UnitlessEnum',
                                 'required': True}},
         'title': 'Unitless Value'})

    value: Decimal = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })
    unit: UnitlessEnum = Field(..., title="unit", description="""The word \"Unitless\" corresponding to a unitless metadata value""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['NumberValue']} })


class ELabRecord(ConfiguredBaseModel):
    """
    An abstract data type representing a link to an record (experiment or resource/item) in an eLabFTW instance. Use one of the ELabItem or ELabRecord classes that implement this one rather than using it directly.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'ELabFTW Record'})

    status_title: str = Field(..., title="StatusTitle", description="""The status title of an ELabFTW resource""", json_schema_extra = { "linkml_meta": {'alias': 'status_title', 'domain_of': ['ELabRecord']} })
    id: int = Field(..., title="id", description="""The integer identifier for this item used by this eLabFTW instance""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['ELabRecord']} })
    elabid: str = Field(..., title="eLabID", description="""The unique \"eLabID\" for this item""", json_schema_extra = { "linkml_meta": {'alias': 'elabid', 'domain_of': ['ELabRecord']} })
    url: str = Field(..., title="url", description="""A (resolvable) URL for accessing this item via a web browser""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['ELabRecord']} })
    api_url: str = Field(..., title="API url", description="""A URL for accessing this item via the eLabFTW API""", json_schema_extra = { "linkml_meta": {'alias': 'api_url', 'domain_of': ['ELabRecord']} })
    title: str = Field(..., title="Title", description="""A short description of this item""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['ELabRecord']} })
    category_title: str = Field(..., title="Category Title", description="""The name of the category for this item (called an \"item type\") in eLabFTW""", json_schema_extra = { "linkml_meta": {'alias': 'category_title', 'domain_of': ['ELabRecord']} })


class ELabItem(ELabRecord):
    """
    A class to hold metadata sufficient to reference a resource (database item) record in an ELabFTW instance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'status_title': {'name': 'status_title', 'required': False}},
         'title': 'ELabFTW Item'})

    type: ELabItemType = Field(..., title="Type", description="""Whether this item is a resource (database item) or an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['ELabItem', 'ELabExperiment']} })
    status_title: Optional[str] = Field(None, title="StatusTitle", description="""The status title of an ELabFTW resource""", json_schema_extra = { "linkml_meta": {'alias': 'status_title', 'domain_of': ['ELabRecord']} })
    id: int = Field(..., title="id", description="""The integer identifier for this item used by this eLabFTW instance""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['ELabRecord']} })
    elabid: str = Field(..., title="eLabID", description="""The unique \"eLabID\" for this item""", json_schema_extra = { "linkml_meta": {'alias': 'elabid', 'domain_of': ['ELabRecord']} })
    url: str = Field(..., title="url", description="""A (resolvable) URL for accessing this item via a web browser""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['ELabRecord']} })
    api_url: str = Field(..., title="API url", description="""A URL for accessing this item via the eLabFTW API""", json_schema_extra = { "linkml_meta": {'alias': 'api_url', 'domain_of': ['ELabRecord']} })
    title: str = Field(..., title="Title", description="""A short description of this item""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['ELabRecord']} })
    category_title: str = Field(..., title="Category Title", description="""The name of the category for this item (called an \"item type\") in eLabFTW""", json_schema_extra = { "linkml_meta": {'alias': 'category_title', 'domain_of': ['ELabRecord']} })


class ELabExperiment(ELabRecord):
    """
    A class to hold metadata sufficient to reference an experiment record in an ELabFTW instance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'ELabFTW Experiment'})

    type: ELabExperimentType = Field(..., title="Type", description="""Whether this item is a resource (database item) or an experiment""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['ELabItem', 'ELabExperiment']} })
    status_title: str = Field(..., title="StatusTitle", description="""The status title of an ELabFTW resource""", json_schema_extra = { "linkml_meta": {'alias': 'status_title', 'domain_of': ['ELabRecord']} })
    id: int = Field(..., title="id", description="""The integer identifier for this item used by this eLabFTW instance""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['ELabRecord']} })
    elabid: str = Field(..., title="eLabID", description="""The unique \"eLabID\" for this item""", json_schema_extra = { "linkml_meta": {'alias': 'elabid', 'domain_of': ['ELabRecord']} })
    url: str = Field(..., title="url", description="""A (resolvable) URL for accessing this item via a web browser""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['ELabRecord']} })
    api_url: str = Field(..., title="API url", description="""A URL for accessing this item via the eLabFTW API""", json_schema_extra = { "linkml_meta": {'alias': 'api_url', 'domain_of': ['ELabRecord']} })
    title: str = Field(..., title="Title", description="""A short description of this item""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['ELabRecord']} })
    category_title: str = Field(..., title="Category Title", description="""The name of the category for this item (called an \"item type\") in eLabFTW""", json_schema_extra = { "linkml_meta": {'alias': 'category_title', 'domain_of': ['ELabRecord']} })


class ELabUser(ConfiguredBaseModel):
    """
    A data type representing a link to a user in an eLabFTW instance
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'ELabFTW User'})

    userid: int = Field(..., title="User ID", description="""The \"local\" identifier number for this user in the eLabFTW instance""", json_schema_extra = { "linkml_meta": {'alias': 'userid', 'domain_of': ['ELabUser']} })
    first_name: str = Field(..., title="First Name", description="""The user's first (given) name""", json_schema_extra = { "linkml_meta": {'alias': 'first_name', 'domain_of': ['ELabUser']} })
    last_name: str = Field(..., title="Last Name", description="""The user's last name (surname)""", json_schema_extra = { "linkml_meta": {'alias': 'last_name', 'domain_of': ['ELabUser']} })
    email: str = Field(..., title="Email", description="""The user's email address""", json_schema_extra = { "linkml_meta": {'alias': 'email', 'domain_of': ['ELabUser']} })
    base_url: str = Field(..., title="ELabFTW Base URL", description="""The URL of the ELabFTW instance in which the user is registered""", json_schema_extra = { "linkml_meta": {'alias': 'base_url', 'domain_of': ['ELabUser']} })
    orcid: Optional[str] = Field(None, title="ORCID", description="""The user's ORCID (if defined)""", json_schema_extra = { "linkml_meta": {'alias': 'orcid', 'domain_of': ['ELabUser']} })

    @field_validator('email')
    def pattern_email(cls, v):
        pattern=re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid email format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid email format: {v}")
        return v

    @field_validator('orcid')
    def pattern_orcid(cls, v):
        pattern=re.compile(r"^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid orcid format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid orcid format: {v}")
        return v


class CFUMethodValue(ArrayValue):
    """
    An override of ArrayValue allowing only values from the CFUMethodEnum enum
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'description': 'Describes deposition format of cells '
                                                 'on agar plate',
                                  'name': 'value',
                                  'range': 'CFUMethodEnum'}},
         'title': 'CFU Method Value'})

    value: List[CFUMethodEnum] = Field(..., title="value", description="""Describes deposition format of cells on agar plate""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class FCInjectionModeValue(StringValue):
    """
    An override of StringValue allowing only values from the FCInjectionModeEnum enum
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'Flow Cytometry Injection Mode Value'})

    value: Optional[str] = Field(None, description="""The value attribute for FCInjectionMode""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class FixationMethodValue(ArrayValue):
    """
    An override of ArrayValue allowing only values from the FixationMethodEnum enum
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'description': 'The value attribute for '
                                                 'FixationMethod',
                                  'name': 'value',
                                  'range': 'FixationMethodEnum'}},
         'title': 'Fixation Method Value'})

    value: List[FixationMethodEnum] = Field(..., title="value", description="""The value attribute for FixationMethod""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class FluorescentProbeValue(ArrayValue):
    """
    An override of ArrayValue allowing only ELabItem values
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'description': 'The value attribute for '
                                                 'FluorescentProbe',
                                  'inlined': True,
                                  'inlined_as_list': True,
                                  'name': 'value',
                                  'range': 'ELabItem'}},
         'title': 'Fluorescent Probe Value'})

    value: List[ELabItem] = Field(..., title="value", description="""The value attribute for FluorescentProbe""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class IncubationAtmosphereValue(StringValue):
    """
    An override of StringValue allowing only values from the IncubationAtmosphereEnum enum
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'Incubation Atmosphere Value'})

    value: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class InstrumentIDValue(ELabItemValue):
    """
    A named sub-class of ELabItemValue to hold an instrument identifier value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'Instrument ID Value'})

    value: ELabItem = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class LabCASInstrumentValue(ELabItemValue):
    """
    A named sub-class of ELabItemValue to hold the instrument identifier
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'deprecated': '(2024 June) this is too specific, use InstrumentIDValue '
                       'instead',
         'deprecated_element_has_exact_replacement': 'InstrumentIDValue',
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'LabCAS-InstrumentValue'})

    value: ELabItem = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class LabCASMicrobialMaterialIDValue(ArrayValue):
    """
    A named sub-class of ArrayValue to hold a list of microbial material links
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'deprecated': '(2024 June) this is too specific, use MicrobialMaterialIDValue '
                       'instead',
         'deprecated_element_has_exact_replacement': 'MicrobialMaterialIDValue',
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'inlined': True,
                                  'inlined_as_list': True,
                                  'name': 'value',
                                  'range': 'ELabItem'}},
         'title': 'LabCAS-MicrobialMaterialIDValue'})

    value: List[ELabItem] = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class LabCASOperatorValue(ELabItemValue):
    """
    A named sub-class of ELabItemValue to hold the operator identifier
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'deprecated': '(2024 June) this is too specific, use OperatorIDValue instead',
         'deprecated_element_has_exact_replacement': 'OperatorIDValue',
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'LabCAS-OperatorValue'})

    value: ELabItem = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class LabCASProjectValue(ELabItemValue):
    """
    A named sub-class of ELabItemValue to hold the project identifier
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'deprecated': '(2024 June) this is too specific, use ProjectIDValue instead',
         'deprecated_element_has_exact_replacement': 'ProjectIDValue',
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'LabCAS-ProjectValue'})

    value: ELabItem = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class MicrobialMaterialIDValue(ArrayValue):
    """
    A named sub-class of ArrayValue to hold a list of microbial material links
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'inlined': True,
                                  'inlined_as_list': True,
                                  'name': 'value',
                                  'range': 'ELabItem'}},
         'title': 'Microbial Material ID Value'})

    value: List[ELabItem] = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class ModalitiesValue(ArrayValue):
    """
    A named sub-class of ArrayValue to hold a list of modality types
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'range': 'MicroscopyModalitiesEnum'}},
         'title': 'Modalities Value'})

    value: List[MicroscopyModalitiesEnum] = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class NucleicAcidTypeValue(StringValue):
    """
    An override of StringValue allowing only a value from the NucleicAcidTypeEnum enum
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value', 'range': 'NucleicAcidTypeEnum'}},
         'title': 'Nucleic Acid Type Value'})

    value: NucleicAcidTypeEnum = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class ObjectivesValue(ArrayValue):
    """
    An override of ArrayValue allowing only values from the ObjectivesEnum enum
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value', 'range': 'ObjectivesEnum'}},
         'title': 'Objectives Value'})

    value: List[ObjectivesEnum] = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class OperatorIDValue(ELabItemValue):
    """
    A named sub-class of ELabItemValue to hold an operator identifier value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'Operator ID Value'})

    value: ELabItem = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class ProjectIDValue(ELabItemValue):
    """
    A named sub-class of ELabItemValue to hold a project identifier value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'title': 'Project ID Value'})

    value: ELabItem = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class SamplePurposeCodesValue(ArrayValue):
    """
    An override of ArrayValue allowing only values from the SamplePurposeCodeEnum enum
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value', 'range': 'SamplePurposeCodeEnum'}},
         'title': 'Sample Purpose Codes Value'})

    value: List[SamplePurposeCodeEnum] = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class SeriesImageTypesValue(ArrayValue):
    """
    An override of ArrayValue allowing only values from the ImageTypeEnum enum
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value', 'range': 'ImageTypeEnum'}},
         'title': 'Series Image Types Value'})

    value: List[ImageTypeEnum] = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


class CytoFLEXAcquisitionTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a CytoFLEX_Acquisition experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^CytoFLEX_Acquisition$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'CytoFLEX Acquisition Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^CytoFLEX_Acquisition$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class NucleicAcidExtractionTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a Nucleic Acid Extraction experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^Nucleic Acid Extraction$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'Nucleic Acid Extraction Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^Nucleic Acid Extraction$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class CellCultureInBrothTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a Cell Culture in Broth experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^Cell Culture in Broth$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'Cell Culture In Broth Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^Cell Culture in Broth$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class CytoFLEXVolumeCalibrationTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a CytoFLEX_VolumeCalibration experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^CytoFLEX_VolumeCalibration$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'CytoFLEX Volume Calibration Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^CytoFLEX_VolumeCalibration$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class FormaldehydeFixationTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a FormaldehydeFixation experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^FormaldehydeFixation$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'Formaldehyde Fixation Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^FormaldehydeFixation$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class MicroscopyAcquisitionTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a Microscopy_Acquisition experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^Microscopy_Acquisition$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'Microscopy Acquisition Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^Microscopy_Acquisition$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class CoulterAcquisitionTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a Coulter_Acquisition experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^Coulter_Acquisition$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'Coulter Acquisition Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^Coulter_Acquisition$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class BactoBoxAcquisitionTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a BactoBox_Acquisition experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': 'BactoBox_Acquisition$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'BactoBox Acquisition Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"BactoBox_Acquisition$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class LogCOMETSamplePrepTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a LogCOMET_SamplePrep experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^LogCOMET_SamplePrep$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'LogCOMET Sample Prep Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^LogCOMET_SamplePrep$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class CFUTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a CFU experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^CFU$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'CFU Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^CFU$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class DifcoAmendedSporulationAgarProtocolTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a Difco Amended Sporulation Agar Protocol experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^Difco Amended Sporulation Agar '
                                             'Protocol$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'Difco Amended Sporulation Agar Protocol Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^Difco Amended Sporulation Agar Protocol$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class InitiateGrowthOfBSpizizeniiTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a Initiate Growth of B spizizenii experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^Initiate Growth of B spizizenii$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'Initiate Growth of B spizizenii Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^Initiate Growth of B spizizenii$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class SlideCleaningTemplateNameValue(StringValue):
    """
    An override of StringValue specified an allowed value for the template_name for a SlideCleaning experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value',
                                  'pattern': '^SlideCleaning$',
                                  'range': 'string',
                                  'required': True}},
         'title': 'Slide Cleaning Template Name Value'})

    value: str = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^SlideCleaning$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid value format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid value format: {v}")
        return v


class TransmissionModeValue(ArrayValue):
    """
    An override of ArrayValue allowing only values from the TransmissionModeEnum enum
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'deprecated': '(2024 June) this is too specific, use ModalitiesValue instead',
         'deprecated_element_has_exact_replacement': 'ModalitiesValue',
         'from_schema': 'https://w3id.org/usnistgov/microbial-experiment-schema',
         'slot_usage': {'value': {'name': 'value', 'range': 'TransmissionModeEnum'}},
         'title': 'Transmission Mode Value'})

    value: List[TransmissionModeEnum] = Field(..., title="value", description="""The actual metadata value for an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['BooleanValue',
                       'NumberValue',
                       'StringValue',
                       'UriValue',
                       'DateValue',
                       'ArrayValue',
                       'ELabItemValue',
                       'FCInjectionModeValue',
                       'IncubationAtmosphereValue']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Experiment.model_rebuild()
ExperimentWithData.model_rebuild()
ExperimentWithInstrument.model_rebuild()
ExperimentWithInstrumentNoData.model_rebuild()
CytoFLEXAcquisition.model_rebuild()
NucleicAcidExtraction.model_rebuild()
CellCultureInBroth.model_rebuild()
CytoFLEXVolumeCalibration.model_rebuild()
GenericTemplateDeprecated.model_rebuild()
FormaldehydeFixation.model_rebuild()
MicroscopyAcquisition.model_rebuild()
GenericTemplate.model_rebuild()
CoulterAcquisition.model_rebuild()
BactoBoxAcquisition.model_rebuild()
LogCOMETSamplePrep.model_rebuild()
CFU.model_rebuild()
DifcoAmendedSporulationAgarProtocol.model_rebuild()
InitiateGrowthOfBSpizizenii.model_rebuild()
SlideCleaning.model_rebuild()
BooleanValue.model_rebuild()
NumberValue.model_rebuild()
StringValue.model_rebuild()
UriValue.model_rebuild()
DateValue.model_rebuild()
ArrayValue.model_rebuild()
ELabItemValue.model_rebuild()
VolumeValue.model_rebuild()
LengthValue.model_rebuild()
DurationValue.model_rebuild()
TemperatureValue.model_rebuild()
CountValue.model_rebuild()
FlowRateValue.model_rebuild()
AgitationValue.model_rebuild()
UnitlessValue.model_rebuild()
ELabRecord.model_rebuild()
ELabItem.model_rebuild()
ELabExperiment.model_rebuild()
ELabUser.model_rebuild()
CFUMethodValue.model_rebuild()
FCInjectionModeValue.model_rebuild()
FixationMethodValue.model_rebuild()
FluorescentProbeValue.model_rebuild()
IncubationAtmosphereValue.model_rebuild()
InstrumentIDValue.model_rebuild()
LabCASInstrumentValue.model_rebuild()
LabCASMicrobialMaterialIDValue.model_rebuild()
LabCASOperatorValue.model_rebuild()
LabCASProjectValue.model_rebuild()
MicrobialMaterialIDValue.model_rebuild()
ModalitiesValue.model_rebuild()
NucleicAcidTypeValue.model_rebuild()
ObjectivesValue.model_rebuild()
OperatorIDValue.model_rebuild()
ProjectIDValue.model_rebuild()
SamplePurposeCodesValue.model_rebuild()
SeriesImageTypesValue.model_rebuild()
CytoFLEXAcquisitionTemplateNameValue.model_rebuild()
NucleicAcidExtractionTemplateNameValue.model_rebuild()
CellCultureInBrothTemplateNameValue.model_rebuild()
CytoFLEXVolumeCalibrationTemplateNameValue.model_rebuild()
FormaldehydeFixationTemplateNameValue.model_rebuild()
MicroscopyAcquisitionTemplateNameValue.model_rebuild()
CoulterAcquisitionTemplateNameValue.model_rebuild()
BactoBoxAcquisitionTemplateNameValue.model_rebuild()
LogCOMETSamplePrepTemplateNameValue.model_rebuild()
CFUTemplateNameValue.model_rebuild()
DifcoAmendedSporulationAgarProtocolTemplateNameValue.model_rebuild()
InitiateGrowthOfBSpizizeniiTemplateNameValue.model_rebuild()
SlideCleaningTemplateNameValue.model_rebuild()
TransmissionModeValue.model_rebuild()

