from bs4 import BeautifulSoup
import requests
import re
import csv

page_content = requests.get("https://catalog.csusb.edu/coursesaz/")
# all department used to find all courses in that departments
soup = BeautifulSoup(page_content.text, "html.parser")
# get me the HTML
results = soup.find_all("div", {"class", "page_content"})
# pasar some
values = results.pop()
# get me those strings
All_Deparments = re.findall(r'\((.*?)\)', values.text)
# Get anything between () this is the departments

dataset = []
CSV_rows = {}

soup = BeautifulSoup(page_content.text, "html.parser")
for department in All_Deparments: # for each  department
    results = soup.find_all("a")
    for result in results:
        strin = result.text
        if department.upper() in strin:
            fullname = strin.split(" ")[0]
            temp_abbr = strin.split(" ")[1]
            abbr = re.findall(r'\((.*?)\)', strin)
            CSV_rows.update({"Abbr": abbr.pop()})
            CSV_rows.update({"Fullname": fullname})
            dataset.append(CSV_rows)
            CSV_rows = {}


attributes = ["Abbr", "Fullname"]
filename = 'trash.csv'
path = 'C:/Users/ORA PC/Desktop/Repos/DataBase_Project/Code/CSV/CSV Files/'

with open(path + filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(dataset)