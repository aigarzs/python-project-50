from gendiff import stylish


def get_view(gendiff_dict, view_format):
    if view_format == "stylish":
        return stylish.get_view(gendiff_dict)
    else:
        raise TypeError(f"Unknown format = '{view_format}'")
