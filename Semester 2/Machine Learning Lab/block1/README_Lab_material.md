# Material für das Lab

Welche Materialen/Software/Bibliotheken benötigen wir im Lab? In diesem Readme beantworten wir diese Frage und stellen euch alle Materialen vor. Außerdem zeigen wir euch, wie ihr euch diese Materialien beschaft.

## Python

Wir verwenden im Lab ausschließlich Python und empfehlen euch die Version 3.6 oder 3.7. Normalerweise spielt dit Subversion bei Python keine wichtige Rolle. Hier im Lab verwenden wir aber Tensorflow - eine Bibliothek von Google für die explizit die Py-Versionen 3.5, 3.6 und 3.7 empfohlen werden.

Wir empfehlen außerdem die Verwendung eines nativen Pythons, das ihr euch direkt über python.org herunterladen könnt. Die empfohlenen Versionen findet ihr hier:

* [Python 3.6](https://www.python.org/downloads/release/python-3610/)
* [Python 3.7](https://www.python.org/downloads/release/python-376/)

**ACHTUNG:** Die aktuellste Python-Version (derzeit 3.8) wird nicht unterstützt. Außerdem unterstützt `tensorflow` ausschließliche Python 64-bit.

## Virutualenv

Wir empfehlen euch in diesem Lab die Verwendung eines Python virtualenv - eines virtuellen Environments, insbesondere dann, wenn ihr neben dem oben empfohlenen Python noch andere Python-Versionen auf eurem System laufen habt.

`virtualenv` könnt ihr euch direkt mit dem Python-Paketmanager `pip` installieren:

```shell
pip install virtualenv
```

Anschließend könnt ihr euch einen Projektordner für Machine-Learning anlegen. Über die Kommandozeile von Windows könnte das z.B. so aussehen. Anstelle von `ml_ordner` könnt ihr einen eigenen Ordnernamen festlegen. Mit Hilfe von `cd ml_ordner` springt ihr anschließend in den Ordner hinein.

```shell
mkdir ml_ordner
cd ml_ordner
```

Nun könnt ihr euch in eurem Machine-Learning-Ordner ein neues `virtualenv` anlegen. Um sicher zu sein, dass die richtige Python-Version verwendet wird, fügt bitte den korrekten Pfad für euer System ein. Anstelle von `venv` könnt ihr eurem `virtualenv` natürlich auch einen anderen Namen geben.

```shell
virutalenv --python={{Pfad zur python.exe eurer wahl}} venv
```

`virtualenv` legt für euch eine neue "Python-Kopie" auf eurem System an, die ihr nun für Machine Learning vorbereiten könnt. Sobald ihr diese Kopie nicht mehr braucht könnt ihr den Ordner `venv` entfernen - euer Python-Kernel bleibt sauber.

## Virutualenv aktivieren

Standardmäßg werden alle Python-Anweisungen an euren Haupt-Kernel geschickt. Um diese auf euer neues `virtualenv` umzuleiten, müsst ihr dieses aktivieren. Dazu kehrt einfach wieder in euren Machine Learning Projektordner zurück, öffnet eine Kommandozeile/Terminal und führt folgenden Befehl aus (Achtung: wenn ihr euer `virtualenv` anders genannt habt, müsst ihr `venv` natürlich austauschen):

**Windows**
```shell
venv\Scripts\activate
```

**Linux/Mac**
```shell
venv/bin/activate
```

## Verwendete Bibliotheken

Wir arbeiten im Lab mit Python und [Jupyter Notebooks](https://jupyter.org/index.html). Jupyter ist sehr komfortables Tool für die Datenanalyse, weil wir den Code unseres Notebooks in Zellen aufspalten und diese Zell unabhängig voneinander ausführen können. Außerdem werden Objekte nicht nach jedem Durchlauf zerstört, sondern bleiben erhalten. Auf diese Weise können wir unkompliziert auf die Ergebnisse bereits ausgeführter Code-Zellen zugreifen.

Unterhalb haben wir euch die `cmd`/`shell`-Anweisungen zum Installieren von Jupyter eingefügt. Die Zweite Zeile installiert euch die Jupyter NBExtensions, die manchmal sehr praktisch sein können - darum empfehle ich die Installation. Ich verwende hier den Paketmanager `pip`. Ihr könnt aber auch gerne den Paketmanager von PyCharms, Anaconda usw. verwenden.

> Bitte alle Befehle bei aktiviertem virtualenv ausführen, damit die entsprechenden Bibliotheken in unserem venv installiert werden.

> Um die Installation zu beschleunigen haben wir ein `requirements.txt` zusammengestellt, mit dessen Hilfe die gesamte Installation in einem durchgeführt werden kann `pip install -r requirements.txt`

```shell
pip install jupyter
pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install
```

In python arbeiten wir vorwiegend mit `pandas` und `sklearn`. Wir werden im weiteren Verlauf des Labs noch auf einige andere Bibliotheken stoßen, aber die kommen dann, wenn's soweit ist. Bei der Visualisierung arbeiten wir mit `matplotlib`, `bokeh` und `seaborn`.

```shell
pip install pandas
pip install matplotlib
pip install seaborn
pip install bokeh
pip install pandas
pip install sklearn
```

Für einige, wenngleich seltene, Operationen brauchen wir dann noch `numpy` (z.B. für die Zufallszahlen oder Wurzelfunktionen). Auch wenn ich davon ausgehe, dass ihr alle schon mit `numpy` gearbeitet habt, hier noch einmal die Anweisung zur Installation:

```shell
pip install numpy
```

Später im Lab werden wir uns auch noch mit Deep-Learning Frameworks beschäftigen. Hier setzten wir auf `tensorflow` (Deep learning backend) und `keras` (Deep learning frontend). Achtung: Wenn wir ihr `tensorflow`-Version 2 installiert habt, ist keras bereits installiert; wenn ihr eine ältere Version von `tensorflow` installiert, muss `keras` separat installiert werden (`pip install keras`).

```shell
pip install tensorflow
```

Wer im Lab 1 gerne einen Webservice bauen möchte, um seine/ihre entwickelten Modelle zugänglich zu machen (das besprechen wir noch ausführlich im Lab), der/die kann z.B. auf `flask` zurück greifen.

```shell
pip install flask
```

Zum Serialisieren von Objekten bietet uns Python eine vielzahl von Möglichkeiten an. Wir verwenden im Lab `dill` um dies zu tun.

```shell
pip install dill
```

## Quick-Installation
