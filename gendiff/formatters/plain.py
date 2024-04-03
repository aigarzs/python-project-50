def get_report(diff: dict):

    result = "".join(format_item("", key, diff[key]) for key in diff.keys())

    # Remove last row's \n
    return result[:-1]


def format_item(nested_key, key, item):
    """
        Working only with items => dict{status, value/dict}

        1) item => Dict - {status, value}
        2) item => Dict - {status, nested dictionary}

        dictionary value in form not `gendiff.compare`
        diff dict never reaches this method,
        because Changed dictionary is returned as str("[complex value]")
        """
    assert is_valid_item(item), \
        "Working only with items => dict{status, value/dict}"

    full_key = f"{nested_key}.{key}" if len(nested_key) > 1 else key
    status = item.get("status")
    value = item.get("value")

    if status in ["changed", "added", "removed"]:
        return format_row(full_key, item) + "\n"

    # nested dict
    elif status == "nested" and isinstance(value, dict):
        return "".join(format_item(full_key, k, value[k]) for k in value.keys())

    # else Unchanged return "" => skip this item
    return ""


def is_valid_item(item):
    if not isinstance(item, dict) or len(item) < 2:
        return False

    valid_status_options = ["unchanged",
                            "changed",
                            "added",
                            "removed",
                            "nested"]
    if item.get("status") not in valid_status_options:
        return False

    if (item.get("status") == "changed" and len(item) == 3
            and "value old" in item and "value new" in item):
        return True

    return len(item) == 2 and "value" in item


def format_row(full_key, item):
    assert is_valid_item(item), \
        "Working only with items `gendiff.comparator` diff dict"
    assert item.get("status") in ["changed", "added", "removed"], \
        "Working only with statuses ['changed', 'added', 'removed']"

    status = item.get("status")
    result = ""
    if status == "changed":
        result = f"Property '{full_key}' was updated. "
        value_old = format_value(item.get("value old"))
        value_new = format_value(item.get("value new"))
        result += f"From {value_old} to {value_new}"
    elif status == "added":
        result = f"Property '{full_key}' was added "
        result += f"with value: {format_value(item.get('value'))}"
    elif status == "removed":
        result = f"Property '{full_key}' was removed"

    return result


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif value is None:
        return "null"
    elif type(value) is bool:
        return str(value).lower()
    elif type(value) is int or type(value) is float:
        return str(value)
    else:
        return "'" + str(value) + "'"
