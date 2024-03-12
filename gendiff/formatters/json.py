# import json


def get_report(diff: dict):
    result = {}

    key = "Unchanged"
    value = filter_dict_unchanged(diff)
    result.update({key: value})

    key = "Added"
    value = filter_dict_added(diff)
    result.update({key: value})

    key = "Removed"
    value = filter_dict_removed(diff)
    result.update({key: value})

    result = format_dict(1, result)

    # with open("tests/fixtures/test3_json_result.json", "w") as outfile:
    #     # json.dump(result, outfile)
    #     outfile.write(result)

    return result


def format_dict(nested_level: int, dictionary: dict):
    result = "{\n"
    for key in dictionary.keys():
        result += 2 * ' ' * nested_level + '"' + str(key) + '": '
        value = dictionary[key]
        if isinstance(value, dict):
            result += format_dict(nested_level + 1, value) + ",\n"
        else:
            result += format_value(value) + ",\n"

    # For empty dict does not remove last characters
    if len(result) > 2:
        # Remove last ",\n"
        result = result[:-2]

    result += "\n" + 2 * " " * (nested_level - 1) + "}"
    return result


def format_value(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int) or isinstance(value, float):
        return str(value)
    else:
        return '"' + str(value) + '"'


def filter_dict_unchanged(diff: dict):
    result = {}
    for key in diff.keys():
        item = diff[key]
        if is_gendiff_item(item) and item[0] == "Unchanged":
            value = item[1]
            if isinstance(value, dict):
                value = filter_dict_unchanged(value)
            result.update({key: value})
    return result


def filter_dict_added(diff: dict):
    result = {}
    for key in diff.keys():
        item = diff[key]
        if is_gendiff_item(item):
            if item[0] == "Added":
                value = item[1]
                result.update({key: value})
            elif item[0] == "Changed":
                value = item[2]
                result.update({key: value})
            elif item[0] == "Unchanged" and isinstance(item[1], dict):
                value = item[1]
                value = filter_dict_added(value)
                result.update({key: value})

    return result


def filter_dict_removed(diff: dict):
    result = {}
    for key in diff.keys():
        item = diff[key]
        if is_gendiff_item(item):
            if item[0] == "Removed":
                value = item[1]
                result.update({key: value})
            elif item[0] == "Changed":
                value = item[1]
                result.update({key: value})
            elif item[0] == "Unchanged" and isinstance(item[1], dict):
                value = item[1]
                value = filter_dict_removed(value)
                result.update({key: value})

    return result


def is_gendiff_item(item):
    if not isinstance(item, tuple) or len(item) < 2:
        return False

    valid_status_options = ["Unchanged", "Changed", "Added", "Removed"]
    if item[0] not in valid_status_options:
        return False

    if item[0] == "Changed" and len(item) == 3:
        return True

    return len(item) == 2
