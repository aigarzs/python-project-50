from gendiff.formatters import json, plain, stylish


def get_format(diff_dict, format_name):
    if format_name == "stylish":
        return stylish.get_report(diff_dict)
    elif format_name == "plain":
        return plain.get_report(diff_dict)
    elif format_name == "json":
        return json.get_report(diff_dict)
    else:
        raise ValueError(f"Unknown report format = '{format_name}'")
