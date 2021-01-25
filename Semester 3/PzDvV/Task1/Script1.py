from xml.etree import ElementTree
from datetime import datetime
import csv
import json


def convert_customer_json():
    """Creates the Kunden.csv file from the Kunden.json file
    """
    # load the customer json file
    with open('Task1/Input/Kunden.json') as json_file:
        customers = json.load(json_file)

    # create a customer csv file
    csv_file = open('Task1/Kunden.csv', 'w')

    # create a csv writer
    csv_writer = csv.writer(csv_file)

    # write header to csv
    header = ["ID", "Bezeichnung", "Land", "PLZ", "Ort", "Gruppe"]
    csv_writer.writerow(header)

    # iterate over customers and write to the csv file
    for c in customers:
        id = c["ID"]
        bez = c["Bezeichnung"]
        country = c["Ort"]["Land"]
        zip = c["Ort"]["Plz"]
        city = c["Ort"]["Ort"]
        group = c["Gruppe"]
        csv_writer.writerow([id, bez, country, zip, city, group])

    csv_file.close()


def create_invoide_csv(xml_root):
    # create csv file
    csv_file = open('Task1/Rechnungen.csv', 'w')

    # create csv writer
    csv_writer = csv.writer(csv_file)

    # write header to csv file
    csv_writer.writerow(["ID", "Jahr", "Nummer", "Datum", "Kunde_ID"])

    counter = 1
    # iterate over each invoice in the xml file
    for invoice in xml_root:
        # holds the data for each row
        row = {}

        # iterate over each element in an invoice
        for e in invoice:
            # add the data of an element to the row data
            row[e.tag] = e.text

        # write to invoice csv
        csv_writer.writerow([
            counter,
            row['Jahr'],
            row['Nummer'],
            row['Datum'] + " 00:00:00",
            row['Kunde_Id']
        ])

        counter = counter + 1

    csv_file.close()


def create_invoice_positions_csv(xml_root):
    csv_file = open('Task1/Rechnungen_Positionen.csv', 'w')

    # create csv writer
    csv_writer = csv.writer(csv_file)

    # write header to csv file
    csv_writer.writerow(["Rechnung_ID", "Artikel_ID", "Menge"])

    counter = 1
    # iterate over each invoice in the xml file
    for invoice in xml_root:
        # iterate over each element in an invoice
        for e in invoice:
            if e.tag == "Positionen":
                for position in e:
                    id = position.attrib['Artikel_ID']
                    qty = position.attrib['Menge']
                    csv_writer.writerow([counter, id, qty])

        counter = counter + 1

    csv_file.close()


def convert_invoice_xml():
    """Creates the Rechnunen.csv and Rechnungen_Positionen.csv file from the Rechnungen.xml file
    """
    # get the xml file
    root = ElementTree.parse('Task1/Input/Rechnungen.xml').getroot()

    # create the csv files
    create_invoide_csv(root)
    create_invoice_positions_csv(root)


def main():
    convert_customer_json()
    convert_invoice_xml()


main()
