import json


def generate_diff(file_path1, file_path2):

    dct1 = json.load(open(file_path1))
    dct2 = json.load(open(file_path2))

    merged = {}

    for k in dct1:
        v1 = dct1[k]
        if k in dct2:
            v2 = dct2[k]
            merged[k] = [v1, v2]
            del dct2[k]
        else:
            merged[k] = [v1, None]

    for k in dct2:
        v2 = dct2[k]
        merged[k] = [None, v2]

    diff = ""
    for k in sorted(merged):
        m = merged[k]
        v1, v2 = m[0], m[1]

        if v1 == v2:
            diff += f"  {k}: {v1}\n"
        elif v1 is None:
            diff += f"+ {k}: {v2}\n"
        elif v2 is None:
            diff += f"- {k}: {v1}\n"
        else:
            diff += f"- {k}: {v1}\n+ {k}: {v2}\n"

    diff = diff[:-1]
    return diff


if __name__ == "__main__":
    print(generate_diff("file1.json", "file2.json"))
