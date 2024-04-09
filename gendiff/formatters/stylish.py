def get_report(diff: dict):
    result = "{\n"
    result += format_diff(1, diff)
    result += "}"
    return result


def format_diff(nested_level: int, diff: dict):
    result = ""

    for key, value in diff.items():
        status = value.get("status")
        if status == "nested":
            result += (build_line_indent(nested_level, " ") + " "
                       + str(key) + ": {\n")
            result += format_diff(nested_level + 1, value.get("value"))
            result += (" " * 4 * nested_level) + "}\n"

        elif status == "changed":
            result += format_item(nested_level,
                                  "-", key, value.get("value old"))
            result += format_item(nested_level,
                                  "+", key, value.get("value new"))

        elif status in ("removed", "added", "unchanged"):
            prefix = {"added": "+", "removed": "-"}.get(status, " ")
            result += format_item(nested_level,
                                  prefix, key, value.get("value"))

    return result


def format_item(nested_level: int, prefix: str, key: str, value):
    result = (build_line_indent(nested_level, prefix) + " "
              + str(key) + ": ")

    if isinstance(value, dict):
        result += "{\n"
        for k, v in value.items():
            result += format_item(nested_level + 1,
                                  " ", k, v)
        result += (" " * 4 * nested_level) + "}\n"
    else:
        result += format_value(value) + "\n"

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
