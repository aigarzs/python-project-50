import pytest
from gendiff import generate_diff, get_view


@pytest.mark.skip(reason="Developing new functionality")
def test_gendiff_yaml_1():
    result = generate_diff("tests/fixtures/test2_file1.yml",
                           "tests/fixtures/test2_file2.yml")
    result = get_view(result)

    expected_result = open("tests/fixtures/test1_result").read()[:-1]
    assert result == expected_result
