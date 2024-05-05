from bs4 import BeautifulSoup
import requests
import re
import csv
import random

page_content = requests.get("https://catalog.csusb.edu/coursesaz/")

soup = BeautifulSoup(page_content.text, "html.parser")

results = soup.find_all("div", {"class", "page_content"})

values = results.pop()

All_Deparments = re.findall(r'\((.*?)\)', values.text)

CSV_rows = {}
dataset = []
course_abbr = []
index = 0

for department in All_Deparments: # for each  department
    department_courses = requests.get("https://catalog.csusb.edu/coursesaz/" + department.lower() + "/")
    soup = BeautifulSoup(department_courses.text, "html.parser")

    courses_in_dep = soup.find_all("span", {"class", "coursetitle"})  # department / #  title
    for course in courses_in_dep:
        number = re.findall(r'\d+', course.text)  # course number
        course_abbr.append(department + " " + str(number[0]))

    test = soup.find_all("p", {'class', 'courseblockdesc'})
    for txt in test:
        index += 1
        if "Quarter" in txt.text:
            soup = BeautifulSoup(str(txt), "html.parser")
            test = soup.find_all("a", {'class', 'bubblelink code'})
            for text in test:
                CSV_rows.update({"ID_Original": course_abbr[index - 1]})
                abr = re.findall("[a-zA-Z]+", text.text)
                number = re.findall(r'\d+', text.text)
                if len(abr) == 0 or len(number) == 0:
                    break
                CSV_rows.update({"ID_Required": str(abr[0]) + " " + str(number[0])})
                dataset.append(CSV_rows)
                CSV_rows = {}


attributes = ["ID_Original", "ID_Required"]
filename = 'Prerequisite.csv'
path = 'C:/Users/ORA PC/Desktop/Repos/DataBase_Project/Code/CSV/CSV Files/'

with open(path + filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(dataset)