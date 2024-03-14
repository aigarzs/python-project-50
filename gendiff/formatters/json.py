# import json
import json


def get_report(diff: dict):
    result = {}

    key = "unchanged"
    value = filter_dict_unchanged(diff)
    result.update({key: value})

    key = "added"
    value = filter_dict_added(diff)
    result.update({key: value})

    key = "removed"
    value = filter_dict_removed(diff)
    result.update({key: value})

    result = json.dumps(result, indent=4)
    # with open("tests/fixtures/result_json.json", "w") as outfile:
    #     # json.dump(result, outfile)
    #     outfile.write(result)

    return result


def filter_dict_unchanged(diff: dict):
    result = {}
    for key in diff.keys():
        item = diff[key]
        if is_gendiff_item(item):
            value = item.get("value")
            status = item.get("status")
            if status == "unchanged":
                result.update({key: value})
            elif status == "nested dict" and isinstance(value, dict):
                value = filter_dict_unchanged(value)
                result.update({key: value})
    return result


def filter_dict_added(diff: dict):
    result = {}
    for key in diff.keys():
        item = diff[key]
        if is_gendiff_item(item):
            status = item.get("status")
            if status == "added":
                value = item.get("value")
                result.update({key: value})
            elif status == "changed":
                value = item.get("value new")
                result.update({key: value})
            elif status == "nested dict" and isinstance(item.get("value"), dict):
                value = item.get("value")
                value = filter_dict_added(value)
                result.update({key: value})

    return result


def filter_dict_removed(diff: dict):
    result = {}
    for key in diff.keys():
        item = diff[key]
        if is_gendiff_item(item):
            status = item.get("status")
            if status == "removed":
                value = item.get("value")
                result.update({key: value})
            elif status == "changed":
                value = item.get("value old")
                result.update({key: value})
            elif status == "nested dict" and isinstance(item.get("value"), dict):
                value = item.get("value")
                value = filter_dict_removed(value)
                result.update({key: value})

    return result


def is_gendiff_item(item):
    if not isinstance(item, dict) or len(item) < 2:
        return False

    valid_status_options = ["unchanged", "changed", "added", "removed", "nested dict"]
    if item.get("status") not in valid_status_options:
        return False

    if (item.get("status") == "changed" and len(item) == 3
            and "value old" in item and "value new" in item):
        return True

    return len(item) == 2 and "value" in item
