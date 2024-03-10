import json

import yaml


def json_to_yaml(input_file, output_file):
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)
    with open(output_file, 'w') as yaml_file:
        yaml.dump(data, yaml_file, sort_keys=True)


if __name__ == "__main__":
    json_to_yaml("../tests/fixtures/test3_file1.json",
                 "../../tests/fixtures/test3_file1.yml")
    json_to_yaml("../tests/fixtures/test3_file2.json",
                 "../../tests/fixtures/test3_file2.yml")
