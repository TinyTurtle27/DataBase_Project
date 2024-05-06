import random
from random import randrange
import csv
from random import choice

filenames = "Section.csv"
path = r'C:/Users/ORA PC/Desktop/Repos/DataBase_Project/CSV/CSV Files/'
Delimiter = '|'

ID_sec = []

with open(path + filenames, mode="r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=Delimiter)
    for row in reader:
        ID_sec.append(row["ID"])

ID_sem = []
with open(path + "Semster.csv", mode="r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=Delimiter)
    for row in reader:
        ID_sem.append(row["ID"])

dataset = []
CSV_row = {}
counter = int (len(ID_sec) / len(ID_sem))
index = 0;
for i in range(0, len(ID_sec)):
    CSV_row.update({"ID_Semster": ID_sem[index % len(ID_sem)]})
    if (counter <= 0):
        index += 1
        counter = int(len(ID_sec) / len(ID_sem))
    counter -= 1
    CSV_row.update({"ID_Section": ID_sec[i]})
    dataset.append(CSV_row)
    CSV_row = {}

attributes = ["ID_Semster", "ID_Section"]

with open(path + "semseter_to_section.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(dataset)
