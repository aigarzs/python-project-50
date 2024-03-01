import pytest

from gendiff import generate_diff


def test_gendiff_yaml_nested_1():
    result = generate_diff("tests/fixtures/test3_file1.yml",
                           "tests/fixtures/test3_file2.yml",
                           "stylish")
    # print(result)
    expected_result = open("tests/fixtures/test3_stylish_result").read()[:-1]
    assert result == expected_result


def test_gendiff_yaml_nested_2():
    result = generate_diff("tests/fixtures/test3_file1.yml",
                           "tests/fixtures/test3_file2.yml",
                           "plain")
    # print(result)
    expected_result = open("tests/fixtures/test3_plain_result").read()[:-1]
    assert result == expected_result
