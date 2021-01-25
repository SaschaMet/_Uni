import pandas as pd


def get_discount(d):
    """Returns a discount if there is a value greater than 0, otherwise return 0

    Args:
        d (int): Discount value from df

    Returns:
        [in]: Discount as int
    """
    if d > 0:
        return d
    return 0


def get_invoice_position_value(price, qty, discount):
    """Calculates the Rechnung_Position_Wert column

    Args:
        price (int): article price
        qty (int): article quantity
        discount (int): discount

    Returns:
        [int]: Rechnung_Position_Wert
    """
    total = price * qty
    if discount == 0:
        return round(total, 1)
    total_discounted = total - (total * discount / 100)
    # Laut Angabe eine Nachkommastelle, in ExpectedOutput allerdings mit 2?
    return round(total_discounted, 2)


def main():
    # read files
    articles = pd.read_csv("Task2/Input/Artikel.csv")
    customers = pd.read_csv("Task2/Input/Kunden.csv")
    invoices = pd.read_csv("Task2/Input/Rechnungen.csv")
    invoice_positions = pd.read_csv("Task2/Input/Rechnungen_Positionen.csv")

    # combine all files into a single df
    df = invoice_positions.merge(
        invoices,
        left_on='Rechnung_ID',
        right_on='ID'
    )

    df = df.merge(
        customers,
        left_on='Kunde_ID',
        right_on='ID'
    )

    df = df.merge(
        articles,
        left_on='Artikel_ID',
        right_on='ID'
    )

    # create new columns
    df['Artikel_Rabattiert'] = ""
    df['Rechnung_Position_Wert'] = ""

    # calculate the values for the new columns
    for index, row in df.iterrows():
        discount = get_discount(row['Rabatt'])
        df.at[index, 'Rabatt'] = discount
        df.at[index, 'Artikel_Rabattiert'] = 1 if discount > 0 else 0
        df.at[index, 'Rechnung_Position_Wert'] = get_invoice_position_value(
            float(row['Preis']), float(row['Menge']), discount
        )

    # one hot encode customer group
    one_hot = pd.get_dummies(df['Gruppe'])
    df = df.join(one_hot)

    # drop ID_x + ID_y + Gruppe column
    df.drop(columns=['ID_x', 'ID_y', 'Gruppe'], inplace=True)

    # columns for the resulting df
    columns = [
        "Rechnung_Jahr",
        "Rechnung_Nummer",
        "Rechnung_Datum",
        "Artikel_Kode",
        "Artikel_Preis",
        "Artikel_Rabattiert",
        "Rechnung_Position_Menge",
        "Rechnung_Position_Wert",
        "Kunde_Gruppe_K1",
        "Kunde_Gruppe_K2",
        "Kunde_Gruppe_K3"
    ]

    # holds the data for the resulting df
    rows = []

    # iterate over each row in the dataframe to extract the data
    for _, row in df.iterrows():
        rows.append([
            row['Jahr'],
            row['Nummer'],
            row['Datum'],
            row['Kode'],
            row['Preis'],
            row['Artikel_Rabattiert'],
            row['Menge'],
            row['Rechnung_Position_Wert'],
            row['K1'],
            row['K2'],
            row['K3']
        ])

    # create the resulting df
    df_r = pd.DataFrame(rows, columns=columns)

    # format column to datetime for sorting
    df_r['Rechnung_Datum'] = pd.to_datetime(df_r['Rechnung_Datum'])

    df_r.sort_values(by=[
        'Rechnung_Jahr',
        'Rechnung_Nummer',
        'Artikel_Kode'], inplace=True)

    # format column correctly
    df_r['Rechnung_Datum'] = df_r['Rechnung_Datum'].astype(str) + " 00:00:00"

    # save df to csv
    df_r.to_csv("Task2/Rechnungen_Pandas.csv", index=False, sep=",")


main()
