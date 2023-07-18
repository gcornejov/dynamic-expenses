import json
import locale


def load_data():
    groups = {}
    expenses = {}

    with open("src/resources/groups.json") as gp, open(
        "src/resources/expenses.json"
    ) as ex:
        groups = json.load(gp)
        expenses = json.load(ex)
    return groups, expenses


def compute_percentajes(groups, expenses):
    tot = sum(item["amount"] for item in expenses)

    locale.setlocale(locale.LC_MONETARY, "es_CL.UTF-8")
    locale._override_localeconv = {"frac_digits": 0}
    # print(locale.localeconv()["frac_digits"])
    print(locale.currency(tot, symbol=True, grouping=True))


if "__name__" == "__name__":
    compute_percentajes(*load_data())
