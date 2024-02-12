def format(gendiff: dict):
    pass


def format_item(nested_level: int, gendiff_key: str, gendiff_value):
    result = ""
    for i in range(len(gendiff_value)):
        plus_minus = gendiff_value[i][0]
        dict_value = gendiff_value[i][1]
        if isinstance(dict_value, dict):
            result += format_dictionary(nested_level + 1, dict_value)
        elif isinstance(dict_value, set):
            pass
        else:
            result += format_line(nested_level + 1,
                                  plus_minus, gendiff_key, dict_value)
        result += "\n"

    return result


def format_dictionary(nested_level: int, dictionary: dict):
    result = "{"
    for key in dictionary:
        value = dictionary[key]
        if isinstance(value, dict):
            result += format_dictionary(nested_level + 1, value)
        else:
            result += "\n" + format_line(nested_level, " ", key, value)

    result += " " * 4 * nested_level + "}"
    return result


def format_line(nested_level: int, plus_minus: str, key, value):
    return (" " * 4 * nested_level - 2
            + plus_minus + " "
            + str(key) + ": "
            + str(value))
