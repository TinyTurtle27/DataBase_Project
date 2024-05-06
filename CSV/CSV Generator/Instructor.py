from bs4 import BeautifulSoup
import requests
import re
import csv


page_content = requests.get("https://www.library.ucsb.edu/staff/list")

soup = BeautifulSoup(page_content.text, "html.parser")

results = soup.find_all("td", {'class', 'staff-listing-name'})

First_name = []
Last_name = []

for item in results:
    First_name.append(item.text.split(" ")[0].strip())
    Last_name.append(item.text.split(" ")[1].strip())


for page in range(1, 6, 1):
    page_content = requests.get("https://www.library.ucsb.edu/staff/list?page=" + str(page))
    soup = BeautifulSoup(page_content.text, "html.parser")
    results = soup.find_all("td", {'class', 'staff-listing-name'})
    for item in results:
        First_name.append(item.text.split(" ")[0].strip())
        Last_name.append(item.text.split(" ")[1].strip())

Instructor = {}
CSV_rows = []

for index in range(0, len(First_name)):
    Instructor.update({'ID': index + 1})
    Instructor.update({'First_Name': First_name[index]})
    Instructor.update({'Last_Name': Last_name[index]})
    Instructor.update({'Email': '{:08.0f}'.format(index + 1) + "@CSUBS.edu"})
    CSV_rows.append(Instructor)
    Instructor = {}

attributes = ["ID", "First_Name", "Last_Name", "Email"]

with open(r'C:\Users\ORA PC\Desktop\Repos\DataBase_Project\CSV\CSV Files\Instructor.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(CSV_rows)