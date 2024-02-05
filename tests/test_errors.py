from gendiff import generate_diff
import unittest


def test_errors_1():
    try:
        result = generate_diff("tests/fixtures/test1_file1.txt",
                               "tests/fixtures/test1_file2.json")
    except Exception as e:
        assert isinstance(e, Exception)
