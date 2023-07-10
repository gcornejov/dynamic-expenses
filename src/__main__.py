import json


def load_data():
    groups = {}
    expenses = {}

    with open("src/resources/groups.json") as gp, open(
        "src/resources/expenses.json"
    ) as ex:
        groups = json.load(gp)
        expenses = json.load(ex)
    return groups, expenses


if "__name__" == "__name__":
    print(load_data())
