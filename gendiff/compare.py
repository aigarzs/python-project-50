def compare_dictionaries(dict1: dict, dict2: dict):
    result = {}

    all_keys = sorted(set(dict1) | set(dict2))

    for key in all_keys:
        if key in dict1 and key in dict2:
            value1, value2 = dict1[key], dict2[key]
            if isinstance(value1, dict) and isinstance(value2, dict):
                result[key] = ("Unchanged", compare_dictionaries(value1, value2))
            elif value1 == value2:
                result[key] = ("Unchanged", value1)
            else:
                result[key] = ("Changed", value1, value2)
        elif key in dict1:
            result[key] = ("Removed", dict1[key])
        else:  # key in dict2:
            result[key] = ("Added", dict2[key])

    return result
