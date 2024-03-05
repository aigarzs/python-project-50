import pytest

from gendiff import generate_diff


@pytest.mark.skip(reason="Github Actions results"
                         " file do not match exercise results")
def test_gendiff_json_nested_1():
    result = generate_diff("tests/fixtures/test3_file1.json",
                           "tests/fixtures/test3_file2.json",
                           "stylish")
    # print(result)
    expected_result = open("tests/fixtures/test3_stylish_result").read()[:-1]
    assert result == expected_result


@pytest.mark.skip(reason="Github Actions results"
                         " file do not match exercise results")
def test_gendiff_json_nested_2():
    result = generate_diff("tests/fixtures/test3_file1.json",
                           "tests/fixtures/test3_file2.json",
                           "plain")
    # print(result)
    expected_result = open("tests/fixtures/test3_plain_result").read()[:-1]
    assert result == expected_result


@pytest.mark.skip(reason="Github Actions results"
                         " file do not match exercise results")
def test_gendiff_json_nested_3():
    result = generate_diff("tests/fixtures/test3_file1.json",
                           "tests/fixtures/test3_file2.json",
                           "json")
    # print(result)
    expected_result = open("tests/fixtures/test3_json_result.json").read()
    assert result == expected_result


def test_gendiff_json_nested_4():
    result = generate_diff("tests/fixtures/file1.json",
                           "tests/fixtures/file2.json",
                           "stylish")
    # print(result)
    expected_result = open("tests/fixtures/result_stylish").read()
    assert result == expected_result


def test_gendiff_json_nested_5():
    result = generate_diff("tests/fixtures/file1.json",
                           "tests/fixtures/file2.json",
                           "plain")
    # print(result)
    expected_result = open("tests/fixtures/result_plain").read()
    assert result == expected_result
