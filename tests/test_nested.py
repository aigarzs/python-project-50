import os

import pytest

from gendiff import generate_diff


TESTS_DIR = os.path.abspath("tests")
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


def get_full_file_path(file):
    return f"{FIXTURES_PATH}/{file}"


@pytest.mark.parametrize("file1, file2, report_format, expected",
                         [
                             ("file1.json", "file2.json",
                              "stylish", "result_stylish"),
                             ("file1.yml", "file2.yml",
                              "stylish", "result_stylish"),
                             ("file1.json", "file2.json",
                              "plain", "result_plain"),
                             ("file1.yml", "file2.yml",
                              "plain", "result_plain"),
                             ("file1.json", "file2.json",
                              "json", "result_json.json"),
                             ("file1.yml", "file2.yml",
                              "json", "result_json.json"),
                         ])
def test_gendiff_nested(file1, file2, report_format, expected):
    file1_path = get_full_file_path(file1)
    file2_path = get_full_file_path(file2)
    expected_path = get_full_file_path(expected)
    result = generate_diff(file1_path, file2_path, report_format)
    with open(expected_path) as expected_file:
        expected_result = expected_file.read()
        assert result == expected_result
