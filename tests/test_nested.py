import pytest

from gendiff import generate_diff


@pytest.mark.parametrize("file1_path, file2_path, report_format, expected",
                         [("tests/fixtures/file1.json",
                           "tests/fixtures/file2.json",
                           "stylish",
                           "tests/fixtures/result_stylish"
                           ),
                          ("tests/fixtures/file1.json",
                           "tests/fixtures/file2.json",
                           "plain",
                           "tests/fixtures/result_plain"
                           ),
                          ("tests/fixtures/file1.yml",
                           "tests/fixtures/file2.yml",
                           "stylish",
                           "tests/fixtures/result_stylish"
                           ),
                          ("tests/fixtures/file1.yml",
                           "tests/fixtures/file2.yml",
                           "plain",
                           "tests/fixtures/result_plain"
                           ),
                          ])
def test_gendiff_nested(file1_path, file2_path, report_format, expected):
    result = generate_diff(file1_path, file2_path, report_format)
    expected_result = open(expected).read()
    assert result == expected_result
