import json


def get_report(diff: dict):
    result = json.dumps(diff, indent=4)
    return result
