def get_report(diff: dict):
    result = "{"

    for key in diff.keys():
        result += "\n" + format_item(1, key, diff[key])

    result += "\n}"
    return result


def format_item(nested_level: int, key, item):
    """
    1) item => Tuple - (status, value)
    2) item => Tuple - (status, nested dictionary)
    3) item => value
    4) item => nested dictionary

    first ensure that item is of type tuple(status, value)
    then format_line either format_dictionary
    """

    result = ""

    if (isinstance(item, tuple)
            and len(item) > 1
            and item[0] in ["Unchanged", "Changed", "Added", "Removed"]):
        status = item[0]
        value = item[1]
    else:
        status = "Unchanged"
        value = item
        item = (status, value)

    if status == "Changed":
        if len(item) == 3:
            value_old = item[1]
            item_old = ("Removed", value_old)
            value_new = item[2]
            item_new = ("Added", value_new)

            result += format_item(nested_level, key, item_old) + "\n"
            result += format_item(nested_level, key, item_new)
            return result
        else:
            raise TypeError("For status == Changed, "
                            "the old and the new values have to be provided")

    if isinstance(value, dict):
        result += format_dictionary(nested_level, key, item)
    else:
        result += format_line(nested_level, key, item)

    return result


def format_dictionary(nested_level: int, key, item: dict):
    """

    :param nested_level:
    :param key:
    :param item: tuple(status, value)
    status => Unchanged / Added / Removed
    :return: str
    """

    assert len(item) == 2
    assert isinstance(item[1], dict)

    status = item[0]
    plus_minus = format_plus_minus(status)
    dct = item[1]

    result = (" " * (4 * nested_level - 2)
              + plus_minus + " "
              + str(key) + ": {\n")

    for key in dct:
        result += format_item(nested_level + 1, key, dct[key]) + "\n"

    result += (" " * 4 * nested_level) + "}"
    return result


def format_line(nested_level: int, key, item):
    """

    :param nested_level:
    :param key:
    :param item: tuple(status, value)
    status => Unchanged / Added / Removed
    :return: str
    """

    assert len(item) == 2

    status = item[0]
    plus_minus = format_plus_minus(status)
    value = item[1]

    result = (" " * (4 * nested_level - 2)
              + plus_minus + " "
              + str(key) + ":")

    if value != "":
        result += " " + format_value_json_style(value)

    return result


def format_plus_minus(status):
    assert status in ["Unchanged", "Added", "Removed"]

    plus_minus = " "

    if status == "Added":
        plus_minus = "+"
    elif status == "Removed":
        plus_minus = "-"

    return plus_minus


def format_value_json_style(value):
    if value is None:
        return "null"
    elif type(value) is bool:
        return str(value).lower()
    else:
        return str(value)
