from pathlib import Path

import pandas as pd

INPUT_FILES_DIR = "input_data"
DATA_FILENAME = "Saldo_y_Mov_No_Facturado.xls"

ACCOUNT_AMOUNT = 1254994
FIXED_WEEK_MONEY = 120000
REMAINING_WEEKS = 4

OTHER_PURPOSE = {"Leisure": 430000, "Tita's Gift": 50000}
SUBSCRIPTIONS_NEW = [
    {"Name": "Crunchyroll", "Alias": ["CRUNCHYROLL"], "Amount": 4900},
    {"Name": "Prime Video", "Alias": ["PRIME VIDEO"], "Amount": 5790},
    {"Name": "Youtube", "Alias": ["GOOGLE"], "Amount": 6150},
    {"Name": "Spotify", "Alias": ["SPOTIFY"], "Amount": 7200},
    {"Name": "Google", "Alias": ["GOOGLE"], "Amount": 1900},
    {"Name": "Pokemon", "Alias": ["GOOGLE"], "Amount": 1900},
]
SUBSCRIPTIONS = {
    "Crunchyroll": 4900,
    "Prime Video": 5790,
    "Youtube": 6150,
    "Spotify": 7200,
    "Google": 1900,
    "Pokemon": 1900,
}
ACCUMULATED = 0

INCOMING_CARGES = {"Light": 46000, "Potina Bday": 15000}

INCOMING_DEPOSITS = {}

CURRENT_WEEK_FUTURE = {}

if "__name__" == "__name__":
    # Load data from bank excel (Banco de Chile - National Credit)
    # raw_data.iloc[17:,[4,10]]
    expenses_df = pd.read_excel(
        Path(INPUT_FILES_DIR) / DATA_FILENAME,
        sheet_name=0,
        header=17,
        names=["Date", "Description", "Amount"],
        usecols=[1, 4, 10],
    )

    expenses_df = expenses_df[
        expenses_df["Description"].str.contains("TEF PAGO NORMAL") == False
    ]
    carged_subs_df = expenses_df[expenses_df["Description"].str.contains("GOOGLE")]

    credit_expenses = expenses_df.sum()["Amount"]
    carged_subs = carged_subs_df.sum()["Amount"]

    # Account amount - Credit - Sum(Other purpouse) - (Sum(Subscriptions) - Sum(Currently carged subscrptions)) - Accumulated - Sum(Incomming charges) +  Sum(Incoming deposits)
    remaining = (
        ACCOUNT_AMOUNT
        - credit_expenses
        - sum(OTHER_PURPOSE.values())
        - (sum(SUBSCRIPTIONS.values()) - carged_subs)
        - ACCUMULATED
        - sum(INCOMING_CARGES.values())
        + sum(INCOMING_DEPOSITS.values())
    )
    remaining_p_week = remaining / REMAINING_WEEKS
    remaining_c_week = remaining - (FIXED_WEEK_MONEY * (REMAINING_WEEKS - 1))

    print(expenses_df)
    print(remaining)
    print(remaining_p_week)
    print(remaining_c_week)
