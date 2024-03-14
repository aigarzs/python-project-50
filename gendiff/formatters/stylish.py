def get_report(diff: dict):
    result = "{"

    for key in diff.keys():
        result += "\n" + format_item(1, key, diff[key])

    result += "\n}"
    return result


def format_item(nested_level: int, key, item):
    """
    1) item => Dict - {status, value}
    2) item => Dict - {status, nested dictionary}
    3) item => value
    4) item => nested dictionary

    first ensure that item is of type dict{status, value}
    then format_line either format_dictionary
    """

    if not is_valid_item(item):
        item = {"status": "unchanged", "value": item}

    status = item.get("status")
    value = item.get("value")

    if status == "changed":
        item_old = {"status": "removed", "value": item.get("value old")}
        item_new = {"status": "added", "value": item.get("value new")}

        return (format_item(nested_level, key, item_old) + "\n"
                + format_item(nested_level, key, item_new))

    if isinstance(value, dict):
        return format_dictionary(nested_level, key, item)
    else:
        return format_line(nested_level, key, item)


def is_valid_item(item):
    if not isinstance(item, dict) or len(item) < 2:
        return False

    valid_status_options = ["unchanged", "changed", "added", "removed", "nested dict"]
    if item.get("status") not in valid_status_options:
        return False

    if (item.get("status") == "changed" and len(item) == 3
            and "value old" in item and "value new" in item):
        return True

    return len(item) == 2 and "value" in item


def format_dictionary(nested_level: int, key, item: dict):
    """

    :param nested_level:
    :param key:
    :param item: dict{status, value}
    status => Unchanged / Added / Removed
    :return: str
    """

    assert len(item) == 2, "This method works only with gendiff.compare prepared diff dictionary"
    assert isinstance(item.get("value"), dict), "This method works only for values of type dict"

    status = item.get("status")
    plus_minus = format_plus_minus(status)
    dct = item.get("value")

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
    :param item: dict{status, value}
    status => Unchanged / Added / Removed
    :return: str
    """

    assert len(item) == 2, "This method works only with gendiff.compare prepared diff dictionary"

    status = item.get("status")
    plus_minus = format_plus_minus(status)
    value = item.get("value")

    result = (" " * (4 * nested_level - 2)
              + plus_minus + " "
              + str(key) + ":")

    # if value != "":
    result += " " + format_value_json_style(value)

    return result


def format_plus_minus(status):
    assert status in ["unchanged", "added", "removed", "nested dict"], \
        "changed has to be refactored to added and removed"

    plus_minus = " "

    if status == "added":
        plus_minus = "+"
    elif status == "removed":
        plus_minus = "-"

    return plus_minus


def format_value_json_style(value):
    if value is None:
        return "null"
    elif type(value) is bool:
        return str(value).lower()
    else:
        return str(value)
