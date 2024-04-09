def build_diff_tree(dict1: dict, dict2: dict):
    result = {}

    all_keys = sorted(set(dict1) | set(dict2))
    common_keys = dict1.keys() & dict2.keys()
    removed_keys = dict1.keys() - dict2.keys()
    added_keys = dict2.keys() - dict1.keys()

    for key in all_keys:
        if key in common_keys:
            result[key] = build_diff_common_key(key, dict1, dict2)

        elif key in removed_keys:
            result[key] = {"status": "removed", "value": dict1[key]}

        elif key in added_keys:
            result[key] = {"status": "added", "value": dict2[key]}

    return result


def build_diff_common_key(key: str, dict1: dict, dict2: dict):
    value1, value2 = dict1[key], dict2[key]
    if isinstance(value1, dict) and isinstance(value2, dict):
        return {"status": "nested",
                "value": build_diff_tree(value1, value2)}
    elif value1 == value2:
        return {"status": "unchanged", "value": value1}
    else:
        return {"status": "changed",
                "value old": value1,
                "value new": value2}
