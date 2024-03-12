import json
import yaml
from gendiff.compare import compare_dictionaries
from gendiff.formatters import get_format


def generate_diff(file_path1, file_path2, format_name="stylish"):
    assert isinstance(file_path1, str), "file_path has to be string"
    assert isinstance(file_path2, str), "file_path has to be string"

    dct1 = generate_dict(file_path1)
    dct2 = generate_dict(file_path2)

    diff_dict = compare_dictionaries(dct1, dct2)
    report = get_format(diff_dict, format_name)

    return report


def generate_dict(file_path):
    assert isinstance(file_path, str), "file_path has to be string"
    assert file_path.endswith((".json", ".yml", ".yaml")), "Only JSON, YML, YAML files allowed"

    if file_path.endswith(".json"):
        return json.load(open(file_path))
    else:
        return yaml.safe_load(open(file_path))
