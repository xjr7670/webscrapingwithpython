#!/usr/bin/env python3

from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://www.pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)

print(dictReader.fieldnames)

for row in dictReader:
    print(row)

