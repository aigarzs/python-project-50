import json
import yaml
from gendiff.compare import compare_data


def generate_diff(file_path1, file_path2):
    assert isinstance(file_path1, str)
    assert isinstance(file_path2, str)

    if file_path1.endswith(".json") and file_path2.endswith(".json"):
        return generate_diff_json(file_path1, file_path2)
    elif (file_path1.endswith(".yml") or file_path1.endswith(".yaml")) and (
            file_path2.endswith(".yml") or file_path2.endswith(".yaml")):
        return generate_diff_yaml(file_path1, file_path2)
    else:
        raise TypeError("Only JSON or YAML files")


def generate_diff_yaml(file_path1, file_path2):
    dct1 = yaml.safe_load(open(file_path1))
    dct2 = yaml.safe_load(open(file_path2))
    return compare_data(dct1, dct2)


def generate_diff_json(file_path1, file_path2):
    dct1 = json.load(open(file_path1))
    dct2 = json.load(open(file_path2))
    return compare_data(dct1, dct2)
