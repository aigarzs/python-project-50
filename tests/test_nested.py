import pytest

from gendiff import generate_diff


@pytest.fixture
def fixtures_files_path():
    return "tests/fixtures/"


@pytest.mark.parametrize("file1, file2, report_format, expected",
                         [
                             ("file1.json", "file2.json", "stylish", "result_stylish"),
                             ("file1.yml", "file2.yml", "stylish", "result_stylish"),
                             ("file1.json", "file2.json", "plain", "result_plain"),
                             ("file1.yml", "file2.yml", "plain", "result_plain"),
                             ("file1.json", "file2.json", "json", "result_json.json"),
                             ("file1.yml", "file2.yml", "json", "result_json.json"),
                         ])
def test_gendiff_nested(fixtures_files_path, file1, file2, report_format, expected):
    file1_path = fixtures_files_path + file1
    file2_path = fixtures_files_path + file2
    expected_path = fixtures_files_path + expected
    result = generate_diff(file1_path, file2_path, report_format)
    with open(expected_path) as expected_file:
        expected_result = expected_file.read()

    assert result == expected_result
