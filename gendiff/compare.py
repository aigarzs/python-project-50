def compare_dictionaries(dict1: dict, dict2: dict):
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = {}
    for key in all_keys:
        formatted_item = compare_items(key, dict1, dict2)
        result.update(formatted_item)
    return result


def compare_items(key, data1: dict, data2: dict):
    if key in data1 and key in data2:
        value1 = data1[key]
        value2 = data2[key]
        # if key matches and both value1 and value2 are dictionaries
        # return key with "Unchanged" and compare value1 with value2
        if isinstance(value1, dict) and isinstance(value2, dict):
            return {key: ("Unchanged", compare_dictionaries(data1[key], data2[key]))}
        # if key matches and value1 is equal to value2
        # return key with "Unchanged" and value1
        elif value1 == value2:
            return {key: ("Unchanged", value1)}
        # if key matches and value1 is not equal to value2
        # return key with "Changed" and value1 / value2
        else:
            return {key: ("Changed", value1, value2)}
    # key only in data1
    # return key with "Removed" and value1
    elif key in data1:
        return {key: ("Removed", data1[key])}
    # key only in data2
    # return key with "Added" and value2
    elif key in data2:
        return {key: ("Added", data2[key])}
    # key neither in data1 nor data2
    else:
        raise KeyError(f"key '{key}' not in data1 nor data2")
