from gendiff import generate_diff


def test_gendiff_json_nested_1():
    result = generate_diff("tests/fixtures/test4_file1.yml",
                           "tests/fixtures/test4_file2.yml",
                           "stylish")
    print(result)
    expected_result = open("tests/fixtures/test3_result").read()[:-1]
    assert result == expected_result
