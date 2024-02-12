def compare_dictionaries(dict1, dict2):
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = {}
    for key in all_keys:
        result.update(compare_items(key, dict1, dict2))
    return result


def compare_items(key, data1, data2):
    # if key in data1 and key in data2:
    #     if data1[key] == data2[key]:
    #         return f"  {key}: {data1[key]}"
    #     else:
    #         return f"- {key}: {data1[key]}\n+ {key}: {data2[key]}"
    # elif key in data1:
    #     return f"- {key}: {data1[key]}"
    # elif key in data2:
    #     return f"+ {key}: {data2[key]}"

    if key in data1 and key in data2:
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            return {key:
                    [[" ", compare_dictionaries(data1[key], data2[key])]]
                    }
        elif data1[key] == data2[key]:
            return {key:
                    [[" ", data1[key]]]
                    }
        else:
            return {key:
                    [
                        ["-", data1[key]],
                        ["+", data2[key]]
                    ]
                    }
    elif key in data1:
        return {key:
                [["-", data1[key]]]
                }
    elif key in data2:
        return {key:
                [["+", data2[key]]]
                }
    else:
        return {key: [[None, None]]}
