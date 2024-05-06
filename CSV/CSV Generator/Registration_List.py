from bs4 import BeautifulSoup
import requests
import re
import csv

attributes = ["ID_Section", "ID_Student", "Date_of_Entry"]

dataset = [{"ID_Section": 1, "ID_Student": 1, "Date_of_Entry": "1000-01-01 00:00:00"},
           {"ID_Section": 2, "ID_Student": 1, "Date_of_Entry": "1000-01-01 00:00:00"},
           {"ID_Section": 3, "ID_Student": 1, "Date_of_Entry": "1000-01-01 00:00:00"},
           {"ID_Section": 4, "ID_Student": 1, "Date_of_Entry": "1000-01-01 00:00:00"},
           ]

filename = 'Registration_List.csv'
path = '/CSV/CSV Files/'

with open(path + filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(dataset)
