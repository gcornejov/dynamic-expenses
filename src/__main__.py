import pandas as pd

DATA_FILENAME = "src/resources/Saldo_y_Mov_No_Facturado.xls"

if "__name__" == "__name__":
    # Load data from bank excel (Banco de Chile - National Credit)
    # raw_data.iloc[17:,[4,10]]
    expenses_df = pd.read_excel(
        DATA_FILENAME,
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

    print(expenses_df)
