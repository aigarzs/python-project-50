def build_diff_tree(dict1: dict, dict2: dict):
    result = {}

    all_keys = sorted(set(dict1) | set(dict2))

    for key in all_keys:
        if key in dict1 and key in dict2:
            value1, value2 = dict1[key], dict2[key]
            if isinstance(value1, dict) and isinstance(value2, dict):
                result[key] = {"status": "nested dict",
                               "value": build_diff_tree(value1, value2)}

            elif value1 == value2:
                result[key] = {"status": "unchanged", "value": value1}
            else:
                result[key] = {"status": "changed",
                               "value old": value1,
                               "value new": value2}
        elif key in dict1:
            result[key] = {"status": "removed", "value": dict1[key]}
        else:  # key in dict2:
            result[key] = {"status": "added", "value": dict2[key]}

    return result
