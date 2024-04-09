import json
import os

import yaml
from gendiff.comparator import build_diff_tree
from gendiff.formatters import apply_formatter


def generate_diff(file_path1, file_path2, format_name="stylish"):

    dct1 = get_content(file_path1)
    dct2 = get_content(file_path2)

    diff_dict = build_diff_tree(dct1, dct2)
    report = apply_formatter(diff_dict, format_name)

    return report


def get_content(file_path):
    assert os.path.isfile(file_path), f"{file_path} is not a file"
    assert os.path.splitext(file_path)[1] in (".json", ".yml", ".yaml"), \
        "Only JSON, YML, YAML files allowed"

    file_format = os.path.splitext(file_path)[1][1:]

    with open(file_path) as file:
        return parse(file, file_format)


def parse(content, format_name):
    if format_name == "json":
        return json.load(content)
    elif format_name in ("yaml", "yml"):
        return yaml.safe_load(content)
    else:
        raise ValueError("Only YAML or JSON files recognized")
