def compare_data(dict1, dict2):
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = [compare_items(key, dict1, dict2) for key in all_keys]
    diff = "\n".join(result)
    return diff


def compare_items(key, data1, data2):
    if key in data1 and key in data2:
        if data1[key] == data2[key]:
            return f"  {key}: {data1[key]}"
        else:
            return f"- {key}: {data1[key]}\n+ {key}: {data2[key]}"
    elif key in data1:
        return f"- {key}: {data1[key]}"
    elif key in data2:
        return f"+ {key}: {data2[key]}"
