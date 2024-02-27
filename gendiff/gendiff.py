import json
import yaml
from gendiff.compare import compare_dictionaries
from gendiff.report import get_report


def generate_diff(file_path1, file_path2, format_name):
    assert isinstance(file_path1, str)
    assert isinstance(file_path2, str)

    dct1 = {}
    dct2 = {}
    if file_path1.endswith(".json") and file_path2.endswith(".json"):
        dct1 = generate_dict_json(file_path1)
        dct2 = generate_dict_json(file_path2)
    elif (file_path1.endswith(".yml") or file_path1.endswith(".yaml")) and (
            file_path2.endswith(".yml") or file_path2.endswith(".yaml")):
        dct1 = generate_dict_yaml(file_path1)
        dct2 = generate_dict_yaml(file_path2)
    else:
        raise TypeError("Only JSON or YAML files")

    diff_dict = compare_dictionaries(dct1, dct2)
    report = get_report(diff_dict, format_name)
    return report


def generate_dict_yaml(file_path):
    dct = yaml.safe_load(open(file_path))
    return dct


def generate_dict_json(file_path):
    dct = json.load(open(file_path))
    return dct
