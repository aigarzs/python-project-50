import pytest

from gendiff import generate_diff


def test_gendiff_json_nested_1():
    result = generate_diff("tests/fixtures/test3_file1.json",
                           "tests/fixtures/test3_file2.json",
                           "stylish")
    # print(result)
    expected_result = open("tests/fixtures/test3_stylish_result").read()[:-1]
    assert result == expected_result


def test_gendiff_json_nested_2():
    result = generate_diff("tests/fixtures/test3_file1.json",
                           "tests/fixtures/test3_file2.json",
                           "plain")
    # print(result)
    expected_result = open("tests/fixtures/test3_plain_result").read()[:-1]
    assert result == expected_result
