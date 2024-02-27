import pytest

from gendiff import generate_diff, get_report


@pytest.mark.skip(reason="Developing new functionality")
def test_gendiff_json_1():
    result = generate_diff("tests/fixtures/test1_file1.json",
                           "tests/fixtures/test1_file2.json")
    result = get_report(result)

    expected_result = open("tests/fixtures/test1_result").read()[:-1]
    assert result == expected_result
