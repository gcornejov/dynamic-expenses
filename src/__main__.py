import json


def load_groups():
    groups = {}
    with open("src/resources/groups.json") as f:
        groups = json.load(f)
    return groups


if "__name__" == "__name__":
    print(load_groups())
