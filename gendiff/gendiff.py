import json
import os

import yaml
from gendiff.comparator import build_diff_tree
from gendiff.formatters import get_format


def generate_diff(file_path1, file_path2, format_name="stylish"):

    dct1 = get_content(file_path1)
    dct2 = get_content(file_path2)

    diff_dict = build_diff_tree(dct1, dct2)
    report = get_format(diff_dict, format_name)

    return report


def get_content(file_path):
    assert os.path.isfile(file_path), f"{file_path} is not a file"
    assert os.path.splitext(file_path)[1] in (".json", ".yml", ".yaml"), \
        "Only JSON, YML, YAML files allowed"

    if os.path.splitext(file_path)[1] == ".json":
        file_format = "json"
    else:
        file_format = "yaml"

    with open(file_path) as file:
        return parse(file, file_format)


def parse(file_content, file_format):
    if file_format == "json":
        return json.load(file_content)
    elif file_format == "yaml":
        return yaml.safe_load(file_content)
    else:
        raise ValueError("Only YAML or JSON files recognized")
