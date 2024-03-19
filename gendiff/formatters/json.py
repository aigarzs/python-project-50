# import json
import json


def get_report(diff: dict):
    result = json.dumps(diff, indent=4)
    # with open("tests/fixtures/result_json.json", "w") as outfile:
    #     # json.dump(result, outfile)
    #     outfile.write(result)

    return result

