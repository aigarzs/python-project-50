import json


def generate_diff(file_path1, file_path2):

    dct1 = json.load(open(file_path1))
    dct2 = json.load(open(file_path2))

    all_keys = sorted(set(dct1.keys()) | set(dct2.keys()))

    result = [compare_items(key, dct1, dct2) for key in all_keys]
    diff = "\n".join(result)
    return diff


def compare_items(key, data1, data2):
    if key in data1 and key in data2:
        if data1[key] == data2[key]:
            return f"  {key}: {data1[key]}"
        else:
            return f"- {key}: {data1[key]}\n+ {key}: {data2[key]}"
    elif key in data1:
        return f"- {key}: {data1[key]}"
    elif key in data2:
        return f"+ {key}: {data2[key]}"


if __name__ == "__main__":
    print(generate_diff("../tests/fixtures/test1_file1.json", "../tests/fixtures/test1_file2.json"))
