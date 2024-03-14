import json
import yaml
from gendiff.compare import compare_dictionaries
from gendiff.formatters import get_format


def generate_diff(file_path1, file_path2, format_name="stylish"):

    with open(file_path1) as file1:
        file_format = get_file_format(file_path1)
        dct1 = parse(file1, file_format)

    with open(file_path2) as file2:
        file_format = get_file_format(file_path2)
        dct2 = parse(file2, file_format)

    diff_dict = compare_dictionaries(dct1, dct2)
    report = get_format(diff_dict, format_name)

    return report


def get_file_format(file_path):
    assert isinstance(file_path, str), "file_path has to be string"
    assert file_path.endswith((".json", ".yml", ".yaml")), "Only JSON, YML, YAML files allowed"

    if file_path.endswith(".json"):
        return "json"
    else:
        return "yaml"


def parse(file_content, file_format):
    if file_format == "json":
        return json.load(file_content)
    elif file_format == "yaml":
        return yaml.safe_load(file_content)
    else:
        raise TypeError("Only YAML or JSON files recognized")
