import duckdb
con = duckdb.connect(database=':memory:', read_only=False)


def exe(statement):
    return con.execute(statement + ";").fetchall()


def init():
    con.execute(
        "CREATE TABLE customers AS SELECT * FROM read_csv_auto('Task3/Input/Kunden.csv');"
    )
    con.execute(
        "CREATE TABLE articles AS SELECT * FROM read_csv_auto('Task3/Input/Artikel.csv');"
    )
    con.execute(
        "CREATE TABLE invoices AS SELECT * FROM read_csv_auto('Task3/Input/Rechnungen.csv');"
    )
    con.execute(
        "CREATE TABLE invoice_positions AS SELECT * FROM read_csv_auto('Task3/Input/Rechnungen_Positionen.csv');"
    )


def main():
    init()

    # combine all 4 files to a single table
    exe(
        """
            CREATE TABLE result AS
            SELECT customers.ID, customers.Gruppe, invoices.Jahr, invoices.Nummer, invoices.Datum, invoices.Kunde_ID, ip.Rechnung_ID, ip.Menge, articles.Kode, articles.Bezeichnung, articles.Preis, articles.Rabatt
            FROM invoice_positions ip
            INNER JOIN invoices ON ip.Rechnung_ID = invoices.id
            INNER JOIN customers ON invoices.Kunde_ID = customers.id
            INNER JOIN articles ON ip.Artikel_ID = articles.id
        """
    )

    # add a default discount
    exe("UPDATE result SET Rabatt = 0 WHERE Rabatt IS NULL")

    # Artikel_Rabattiert -> Wenn Rabatt in % > 0 dann 1, sonst 0
    exe("ALTER TABLE result ADD COLUMN Artikel_Rabattiert INTEGER DEFAULT 0")
    exe("UPDATE result SET Artikel_Rabattiert = 1 WHERE Rabatt > 0")

    # Rechnung_Position_Wert -> Menge * Preis - Rabatt in % (gegrundet auf 1 Kommastelle)
    exe("ALTER TABLE result ADD COLUMN rechnung_position_wert FLOAT DEFAULT 0")
    exe("UPDATE result SET rechnung_position_wert = Preis * Menge")
    exe("UPDATE result SET rechnung_position_wert = rechnung_position_wert - (rechnung_position_wert * Rabatt / 100) WHERE Artikel_Rabattiert = 1")
    exe("UPDATE result SET rechnung_position_wert = round(rechnung_position_wert, 2)")

    # One Hot Encoding auf die Kundengruppe durch
    exe("ALTER TABLE result ADD COLUMN kunde_gruppe_k1 INTEGER DEFAULT 0")
    exe("ALTER TABLE result ADD COLUMN kunde_gruppe_k2 INTEGER DEFAULT 0")
    exe("ALTER TABLE result ADD COLUMN kunde_gruppe_k3 INTEGER DEFAULT 0")
    exe("UPDATE result SET kunde_gruppe_k1 = 1 WHERE Gruppe = 'K1'")
    exe("UPDATE result SET kunde_gruppe_k2 = 1 WHERE Gruppe = 'K2'")
    exe("UPDATE result SET kunde_gruppe_k3 = 1 WHERE Gruppe = 'K3'")

    print(exe("select column_name from information_schema.columns where table_name='result'"))
    print(exe("SELECT * FROM result LIMIT 1"))

    con.execute(
        """copy (
            SELECT Jahr as rechnung_jahr,
                Nummer as rechnung_nummer,
                Datum as rechnung_datum,
                Kode as artikel_kode,
                Preis as artikel_preis,
                artikel_rabattiert,
                Menge as rechnung_position_menge,
                rechnung_position_wert,
                kunde_gruppe_k1,
                kunde_gruppe_k2,
                kunde_gruppe_k3
            FROM result
            ORDER BY
                rechnung_jahr,
                rechnung_nummer,
                artikel_kode
        ) to 'Task3/Rechnungen_DuckDB.csv' (HEADER)"""
    )

    con.close()


main()
