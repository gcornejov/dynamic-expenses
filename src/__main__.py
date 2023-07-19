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


def compute_percentages(expenses):
    # tot = sum(item["amount"] for item in expenses)

    locale.setlocale(locale.LC_MONETARY, "es_CL.UTF-8")
    locale._override_localeconv = {"frac_digits": 0}
    # print(locale.localeconv()["frac_digits"])
    # print(locale.currency(tot, symbol=True, grouping=True))

    summ = {}
    tot = 0
    for ex in expenses:
        grp = ex["group"]
        amnt = ex["amount"]

        summ[grp] = summ.get(grp, 0) + amnt
        tot = tot + amnt

    grouped_ammounts = {
        k: locale.currency(v, symbol=True, grouping=True) for (k, v) in summ.items()
    }
    percentages = {k: f"{v/tot:.2%}" for (k, v) in summ.items()}

    print(grouped_ammounts)
    print(percentages)


if "__name__" == "__name__":
    groups, expenses = load_data()
    compute_percentages(expenses)
