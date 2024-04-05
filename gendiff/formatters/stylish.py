def get_report(diff: dict):
    result = "{\n"

    result += "\n".join(format_item(1, key, diff[key]) for key in diff.keys())

    result += "\n}"
    return result


def format_item(nested_level: int, key: str, item):
    """
    1) item => Dict - {status, value}
    2) item => Dict - {status, nested dictionary}

    """

    status = item.get("status")
    value = item.get("value")

    if status == "changed":
        item_old = {"status": "removed", "value": item.get("value old")}
        item_new = {"status": "added", "value": item.get("value new")}

        return (format_item(nested_level, key, item_old) + "\n"
                + format_item(nested_level, key, item_new))

    if isinstance(value, dict):
        if status == "nested":
            return format_nested_dictionary(nested_level, status, key, value)
        else:
            return format_plain_dictionary(nested_level, status, key, value)

    else:
        return format_line(nested_level, status, key, value)


def format_plain_dictionary(nested_level: int, status: str, key: str,
                            item: dict):
    """

    :param nested_level:
    :param status:
    :param key
    :param item:
    :return: formatted stylish report multiple lines
    """

    prefix = {"added": "+", "removed": "-"}.get(status, " ")
    result = build_line_indent(nested_level, prefix) + " " + str(key) + ": {\n"
    for k in item:
        if isinstance(item[k], dict):
            result += format_plain_dictionary(nested_level + 1,
                                              "unchanged",
                                              k,
                                              item[k]) + "\n"
        else:
            result += format_line(nested_level + 1,
                                  "unchanged",
                                  k,
                                  item[k]) + "\n"

    result += (" " * 4 * nested_level) + "}"
    return str(result)


def format_nested_dictionary(nested_level: int, status: str, key: str,
                             item: dict):
    """
    :param nested_level:
    :param status: => nested
    :param key:
    :param item:
    :return: formatted stylish report multiple lines
    """

    result = build_line_indent(nested_level, " ") + " " + str(key) + ": {\n"

    for key in item:
        result += format_item(nested_level + 1, key, item[key]) + "\n"

    result += (" " * 4 * nested_level) + "}"
    return result


def format_line(nested_level: int, status: str, key: str, value):
    """

    :param nested_level:
    :param status:
    :param key:
    :param value:
    :return: formatted stylish report line
    """

    prefix = {"added": "+", "removed": "-"}.get(status, " ")
    result = build_line_indent(nested_level, prefix) + " " + str(key) + ": "
    result += format_value(value)

    return result


def format_value(value):
    if value is None:
        return "null"
    elif type(value) is bool:
        return str(value).lower()
    else:
        return str(value)


def build_line_indent(nested_level: int, prefix: str):
    return " " * (4 * nested_level - 2) + prefix
