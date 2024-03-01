import json
import yaml
from gendiff.compare import compare_dictionaries
from gendiff.report import get_report


def generate_diff(file_path1, file_path2, format_name):
    assert isinstance(file_path1, str)
    assert isinstance(file_path2, str)

    dct1 = generate_dict(file_path1)
    dct2 = generate_dict(file_path2)

    diff_dict = compare_dictionaries(dct1, dct2)
    report = get_report(diff_dict, format_name)
    return report


def generate_dict(file_path):
    assert isinstance(file_path, str)
    assert file_path.endswith((".json", ".yml", ".yaml"))

    if file_path.endswith(".json"):
        return generate_dict_json(file_path)
    else:
        return generate_dict_yaml(file_path)


def generate_dict_yaml(file_path):
    dct = yaml.safe_load(open(file_path))
    return dct


def generate_dict_json(file_path):
    dct = json.load(open(file_path))
    return dct
