from gendiff import generate_diff


def test_gendiff_json_nested_1():
    result = generate_diff("tests/fixtures/test3_file1.json",
                           "tests/fixtures/test3_file2.json")
    print(result)
