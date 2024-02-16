def compare_dictionaries(dict1: dict, dict2: dict):
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = []
    for key in all_keys:
        formatted_item = compare_items(key, dict1, dict2)
        # Changed item is get as list with + and -
        if isinstance(formatted_item, list):
            for i in formatted_item:
                result.append(i)
        else:
            result.append(formatted_item)
    return result


def compare_items(key, data1: dict, data2: dict):
    if key in data1 and key in data2:
        # if key matches and both value1 and value2 are dictionaries
        # return key with no changes and compare value1 with value2
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            return " ", key, compare_dictionaries(data1[key], data2[key])
        # if key matches and value1 is equal to value2
        # return key with no changes and value1
        elif data1[key] == data2[key]:
            return format_value(" ", key, data1[key])
        # if key matches and value1 is not equal to value2
        # return key (-/+) and value1 / value2
        else:
            return [
                format_value("-", key, data1[key]),
                format_value("+", key, data2[key])
                   ]
    # key only in data1
    # return key (-) and value1
    elif key in data1:
        return format_value("-", key, data1[key])
    # key only in data2
    # return key (+) and value2
    elif key in data2:
        return format_value("+", key, data2[key])
    # key neither in data1 nor data2
    else:
        raise KeyError(f"key '{key}' not in data1 nor data2")


def format_value(plus_minus: str, key: str, value):
    """
    :param plus_minus:
    :param key:
    :param value:
    :return:
    Formats value into tuple (+/-), key, value
    Converts dictionary into set
    """

    # If dictionary is requested as value,
    # all dictionary keys are returned without changes
    if isinstance(value, dict):
        subdict = []
        for k in sorted(value.keys()):
            v = value[k]
            if isinstance(v, dict):
                subdict.append(format_value(" ", k, v))
            else:
                subdict.append((" ", k, v))
        return plus_minus, key, subdict
    else:
        return plus_minus, key, value
