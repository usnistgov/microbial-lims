"""
Modification of https://github.com/biolink/biolink-model/blob/master/src/biolink_model/scripts/generate_json.py
to generate a JSON structure of classes and their slots that can be used in a D3 
interactive visualization
"""
from collections import defaultdict
import json
from typing import Any, List, Union
from linkml_runtime.utils.schemaview import SchemaView

file_path = 'src/microbial_experiment_schema/schema/microbial_experiment_schema.yaml'

# Read the file content
with open(file_path, 'r') as file:
    file_content_str = file.read()

# Parse the YAML content
sv = SchemaView(file_content_str)


def get_tree_class_recursive(root_node: dict, parent_to_child_map: dict) -> dict:
    """
    Recursively get the tree node.

    :param root_node: The root node of the tree.
    :type root_node: dict
    :param parent_to_child_map: A dictionary mapping parent nodes to child nodes.
    :type parent_to_child_map: dict
    :return: The tree node.
    :rtype: dict

    """
    root_name = root_node["name"]
    children_names = parent_to_child_map.get(root_name, [])
    if children_names:
        children = []
        for child_name in children_names:
            # omit GenericTemplate from diagram
            if child_name == "GenericTemplate": 
                continue
            child_node = {"name": child_name, "parent": root_name}
            child_node = get_tree_class_recursive(child_node, parent_to_child_map)
            children.append(child_node)
        root_node["children"] = sorted(children, key=lambda x: x["name"])

    return root_node

def load_category_tree_data(return_parent_to_child_dict: bool = False) -> tuple:
    """
    Load the category tree data from the model.

    :param return_parent_to_child_dict: Whether to return the parent to child dictionary.
    :type return_parent_to_child_dict: bool
    :return: The category tree data.
    :rtype: tuple
    """
    parent_to_child_dict = defaultdict(set)
    category_tree = {}
    for class_name in sv.all_classes(imports=True):
        cls = sv.get_class(class_name)
        if cls.deprecated:
            continue
        class_name = convert_predicate_to_trapi_format(class_name)
        if cls.is_a:
            parent_name_english = cls.is_a
            if parent_name_english:
                parent_name = convert_predicate_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(class_name)
                root_node = {"name": "Experiment", "parent": None}
                category_tree = get_tree_class_recursive(root_node, parent_to_child_dict)
                parent_name = convert_category_to_trapi_format(parent_name_english)
                parent_to_child_dict[parent_name].add(class_name)

    # parse category_tree to add slots to leaf nodes
    parse_category_tree_recursive(category_tree)
    return ([category_tree], parent_to_child_dict) if return_parent_to_child_dict else ([category_tree])


def parse_category_tree_recursive(category_tree):
    if isinstance(category_tree, list):
        # this is a list of children
        for c in category_tree:
            parse_category_tree_recursive(c)
    elif 'children' not in category_tree:
        # this is a leaf node, so get slots
        category_tree['children'] = get_slot_children(category_tree['name'], category_tree['name'])
        # print(f"{category_tree['parent']} --> {category_tree['name']} : {category_tree['children']}")
    else:
        parse_category_tree_recursive(category_tree['children'])


def get_slot_children(class_name: str, parent_name: str) -> List[dict]:
    """Return a list of dictionaries with keys "name" and "parent" """
    slots = get_slots_for_class(class_name)
    children_list = []
    for s in slots:
        slot_dict = {'name': s[1], 'parent': parent_name}
        if s[0] != parent_name:
            slot_dict['name'] += f" ({s[0]})"
        children_list.append(slot_dict)        
    return children_list


def get_slots_for_class(class_name: str) -> List[tuple]:
    """Returns a list of tuples of (Source Class, slot_name) for a given class"""
    all_slots = []
    slot_sources = [(i, sv.get_class(i).slots) for i in sv.class_ancestors(class_name)]
    for source, slots in slot_sources:
        for s in slots:
            all_slots.append((source, s))
    return all_slots

def process_class_dict_list(class_dict_list: list) -> dict:
    for d in class_dict_list:
        for k, v in d.items():
            if isinstance(v, dict) or k == 'children':
                process_class_dict_list(v)
            else:
                if k == 'name':
                    print(v, ":", [{i: sv.get_class(i).slots} for i in sv.class_ancestors(v)])

def convert_predicate_to_trapi_format(english_predicate: str) -> str:
    # Converts a string like "treated by" to "treated_by"
    return english_predicate.replace(' ', '_')


def convert_category_to_trapi_format(english_category: str) -> str:
    # Converts a string like "named thing" to "NamedThing"
    return "".join([f"{word[0].upper()}{word[1:]}" for word in english_category.split(" ")])

def generate_viz_json():

    # Generate the d3 viz data
    cat_data = load_category_tree_data()

    with open('src/docs/schema_visualization.json', 'w') as json_file:
        json.dump(cat_data, json_file, indent=4)

if __name__ == "__main__":
    generate_viz_json()
