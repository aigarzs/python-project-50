def get_report(diff: dict):
    result = ""

    for key in diff.keys():
        result += format_item("", key, diff[key])

    return result[:-1]


def format_item(nested_key, key, item):
    """
        Working only with items => tuple(status, value/dict)

        1) item => Tuple - (status, value)
        2) item => Tuple - (status, nested dictionary)

        dictionary value in form not tuple never reaches this method,
        because Changed dictionary is returned as str("[complex value]")
        """
    assert isinstance(item, tuple)
    assert len(item) > 1
    assert item[0] in ["Unchanged", "Changed", "Added", "Removed"]

    result = ""
    full_key = format_key(nested_key, key)
    status = item[0]
    value = item[1]

    if status in ["Changed", "Added", "Removed"]:
        result = format_row(full_key, item) + "\n"
    # Unchanged dict means nested dict
    elif status == "Unchanged" and isinstance(value, dict):
        for k in value.keys():
            result += format_item(full_key, k, value[k])
    # else Unchanged return "" => skip this item
    else:
        return result

    return result


def format_key(nested_key, key):
    if len(nested_key) > 1:
        return nested_key + "." + key
    else:
        return key


def format_row(full_key, item):
    assert isinstance(item, tuple)
    assert len(item) > 1
    assert item[0] in ["Changed", "Added", "Removed"]
    if item[0] == "Changed":
        assert len(item) == 3

    status = item[0]
    result = ""
    if status == "Changed":
        result = f"Property '{full_key}' was updated. "
        result += f"From {format_value(item[1])} to {format_value(item[2])}"
    elif status == "Added":
        result = f"Property '{full_key}' was added "
        result += f"with value: {format_value(item[1])}"
    elif status == "Removed":
        result = f"Property '{full_key}' was removed"

    return result


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif value is None:
        return "null"
    elif type(value) is bool:
        return str(value).lower()
    else:
        return "'" + str(value) + "'"
