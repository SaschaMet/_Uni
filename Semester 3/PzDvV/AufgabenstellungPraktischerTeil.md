# Aufgabenstellung für den praktischen Teil der Prüfung

Diese Aufgaben sind Teil der Prüfung und müssen deshalb selbständig gelöst werden. Jeder Task Ordner enthält die nötigen Input Daten (Input), das erwartete Ergebnis (ExpectedOutput) zur Überprüfung, ob die Aufgabe korrekt gelößt wurde und eine Skript Datei mit den nötigen Imports.

Die erstellten Skripts und erzeugten Ergebnisdateien müssen als Zip-Datei bis zum 05.02.2021 - 12:00 an die Email Adresse volkmar.rigo@lektor.fh-kufstein.ac.at gesendet werden.

## Aufgabe 1 - Datenformate konvertieren 

Für eine Datenauswertung werden folgende Daten aus den Systemen exportiert:

* Rechnungen.xml: XML Datei exportiert mit Rechungen und den zugehörigen Positionen
* Kunden.json: JSON Datei mit den Kundendaten (Name, Adresse, Gruppierung)
* Artikel.csv: CSV Datei mit den Artikeldaten (Kode, Bezeichnung, Preis, Rabatt)

Um besser mit den exportieren Daten arbeiten zu können, muss die XML und JSON Datei in CSV-Dateien konvertiert werden. 
Erstelle ein Python Script, das diese Konvertierung durchführt.

### Rechnungen (5 Punkte)

* Rechnungen.xml -> Rechnungen.csv (ID \[fortlaufende Nummer\], Jahr, Nummer, Datum, Kunde_ID)
* Rechnungen.xml -> Rechnungen_Positionen.csv (Rechnung_ID \[Verweise auf die ID der Rechnungen.csv Datei], Artikel_ID, Menge)

### Kunden (5 Punkte)

* Kunden.json -> Kunden.csv (ID, Bezeichnung, Land, PLZ, Ort, Gruppe)

## Aufgabe 2 - Daten transformieren mit Pandas

Verwende die Pandas Bibliothek, um die folgenden Dateien zu transformieren

* Rechnungen.csv
* Rechnungen_Positionen.csv
* Kunden.csv
* Artikel.csv

Folgende Operationen müssen durchgeführt werden:

### Daten kombinieren (2 Punkte)

Kombiniere die 4 Dateien zu einem Tabelle. Verwende dazu die ID und [Tabellenname]_ID. (Bsp: ```Rechnungen.Kunde_ID -> Kunden.ID```). Achte beim Kombinieren darauf, dass in der Ergebnismenge nur Kunden und Artikel enthalten sind, zu denen es Rechnungen und Rechnungspositionen gibt.

### Fehlende Werte (2 Punkte)

Führe folgende Korrekturen durch

Artikel.Rabatt leer -> Fülle mit konstantem Wert 0

### Wertkonvertierung (2 Punkte)

Füge der Tabelle folgende berechnete Spalten hinzu:

* Rechnung_Position_Wert -> Menge * Preis - Rabatt in % (gegrundet auf 1 Kommastelle)
* Artikel_Rabattiert -> Wenn Rabatt in % > 0 dann 1, sonst 0

### One Hot Encoding (2 Punkte) 

Führe ein One Hot Encoding auf die Kundengruppe durch

### Projektion (2 Punkte)

Führe eine Projektion durch, damit die kombinierte Tabelle folgende Felder in der angegebenen Reihenfolge enthält:

* Rechnung_Jahr
* Rechnung_Nummer
* Rechnung_Datum
* Artikel_Kode
* Artikel_Preis
* Artikel_Rabattiert
* Rechnung_Position_Menge
* Rechnung_Position_Wert
* Kunde_Gruppe_K1
* Kunde_Gruppe_K2
* Kunde_Gruppe_K3

### Speichere das Ergebnis

Sortiere das Ergebnis nach den Spalten Rechnung_Jahr, Rechnung_Nummer und Artikel_Kode. Speichere das Ergebnis als Rechnungen_Pandas.csv mit , als Trenner ab.

## Aufgabe 3 - Daten transformieren mit DuckDB

Verwende die DuckDB Bibliothek (https://duckdb.org/), um dieselben Operationen wie in Aufgabe 2 durchzuführen.

* Daten kombinieren (3 Punkte)
* Fehlende Werte (3 Punkte)
* Wertkonvertierung (3 Punkte)
* One Hot Encoding (3 Punkte) 
* Projektion (3 Punkte)

Sortiere das Ergebnis nach den Spalten Rechnung_Jahr, Rechnung_Nummer und Artikel_Kode. Speichere das Ergebnis als Rechnungen_DuckDB.csv mit , als Trenner ab
