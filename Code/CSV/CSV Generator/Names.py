from bs4 import BeautifulSoup
import requests
import re
import csv

page_content = requests.get("https://www.ssa.gov/oact/babynames/decades/century.html")

soup = BeautifulSoup(page_content.text, "html.parser")

results = soup.find_all("tbody")

First_Names = []
Last_Names = []

for item in results:
    First_Names = re.findall("[a-zA-Z]+", item.text)

filename = "Text Files/Last Names.txt"
with open(filename) as file:
    while line := file.readline():
        Last_Names.append(re.findall("[a-zA-Z]+", line))

CSV_rows = {}
Dataset = []

for index in range(0, 50, 1):
    CSV_rows.update({"ID": index+1})
    CSV_rows.update({"Last_Name": First_Names[index]})
    CSV_rows.update({"First_Name": Last_Names[index][0]})
    CSV_rows.update({"Password": index+1})
    Dataset.append(CSV_rows)
    CSV_rows = {}

filename_csv = "../CSV Files/Student.csv"
attributes = ["ID", "Last_Name", "First_Name", "Password"]

with open(r'/Code/CSV Files/Student.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(Dataset)




# `ID` int not null AUTO_INCREMENT,
# `Last_Name` char(255),
# `First_Name` char(255),
# `Password` char(255),
