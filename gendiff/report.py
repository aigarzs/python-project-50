from gendiff import stylish


def get_report(diff_dict, format_name):
    if format_name == "stylish":
        return stylish.get_report(diff_dict)
    else:
        raise TypeError(f"Unknown report format = '{format_name}'")
