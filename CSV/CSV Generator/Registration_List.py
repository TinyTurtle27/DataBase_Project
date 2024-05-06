import random

from bs4 import BeautifulSoup
import requests
import re
import csv

attributes = ["ID_Section", "ID_Student", "Date_of_Entry"]

filename = r'\Registration_List.csv'
path = r'C:\Users\ORA PC\Desktop\Repos\DataBase_Project\CSV\CSV Files'

dataset = []
CSV_rows = {}
for index in range(1, 50):
    CSV_rows.update({"ID_Student": index})
    item = random.choice(range(1, 120000))
    CSV_rows.update({"ID_Section": int(item)})
    year = random.choice(range(2020,2025))
    day = random.choice(range(1,25))
    month = random.choice(range(1,11))
    hour = random.choice(range(1,23))
    min = random.choice(range(1,59))

    strin = str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(min) + ":00"
    CSV_rows.update({"Date_of_Entry": strin})
    dataset.append(CSV_rows)
    CSV_rows = {}
    year = random.choice(range(2020, 2025))
    day = random.choice(range(1, 25))
    month = random.choice(range(1, 11))
    hour = random.choice(range(1, 23))
    min = random.choice(range(1, 59))

    CSV_rows.update({"ID_Student": index})

    strin = str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(min) + ":00"
    item = random.choice(range(1, 120000))
    CSV_rows.update({"ID_Section": int(item)})
    CSV_rows.update({"Date_of_Entry": strin})
    dataset.append(CSV_rows)
    CSV_rows = {}


with open(path + filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(dataset)
