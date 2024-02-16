def get_view(gendiff: set):
    result = "{"

    for item in gendiff:
        result += "\n" + format_item(1, item)

    result += "\n}"
    return result


def format_item(nested_level: int, item: tuple):
    result = ""

    if isinstance(item, list):
        # List item breaking into tuple items
        for i in item:
            result += format_item(nested_level, i) + "\n"
        return result[:-1]
    elif not isinstance(item, tuple):
        raise TypeError("Item only list or tuple")

    # Proceeding with tuple item
    plus_minus = item[0]
    key = item[1]
    value = item[2]

    if isinstance(value, list):
        # New nested level
        result += format_line(nested_level, plus_minus, key, "{")
        for item in value:
            result += "\n" + format_item(nested_level + 1, item)
        result += "\n" + " " * 4 * nested_level + "}"
    else:
        # Format value in same line
        result += format_line(nested_level, plus_minus, key, value)

    return result


def format_line(nested_level: int, plus_minus: str, key, value):
    result = (" " * (4 * nested_level - 2)
              + plus_minus + " "
              + str(key) + ":")

    if value != "":
        result += " " + format_json_style(value)

    return result


def format_json_style(value):
    if value is None:
        return "null"
    elif type(value) is bool:
        return str(value).lower()
    else:
        return str(value)
