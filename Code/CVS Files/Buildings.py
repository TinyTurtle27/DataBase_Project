import csv
import re

filename = "Buildings.txt"
ID = 1

dataset = []
row = {'ID': -1,
       'Abbr': 'NA',
       'Title': 'NA'
       }

attributes = ['ID', 'Abbr', 'Title']

with open(filename) as file:
    for line in file:
        Abbr = line.split(' ', 1)[0]
        Title = line.split(' ', 1)[1].strip()
        row.update({'ID': ID})
        row.update({'Abbr': Abbr})
        row.update({'Title': Title})
        ID += 1
        dataset.append(row)
        row = {}

filename_csv = "Buildings.csv"

with open(filename_csv, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(dataset)

