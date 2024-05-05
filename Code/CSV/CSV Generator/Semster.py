from bs4 import BeautifulSoup
import requests
import re
import csv
import random

attributes = ["ID", "Year", "Term"]
Term = ['Fall', 'Winter', 'Spring', 'Summer']

Year = []
base_year = 2020
for Delta_time in range(0, 6, 1):
    Year.append(base_year + Delta_time)

index = 1
CSV_rows = {}
dataset = []
for term in Term:
    for time in Year:
        CSV_rows.update({'ID': index})
        CSV_rows.update({'Year': time})
        CSV_rows.update({'Term': term})
        dataset.append(CSV_rows)
        CSV_rows = {}
        index += 1

filename = 'Semster.csv'
path = 'C:/Users/ORA PC/Desktop/Repos/DataBase_Project/Code/CSV/CSV Files/'

with open(path + filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(dataset)