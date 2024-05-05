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


#//////////////////////^ get all department

Course_deparment = []
course_number = []
Course_title = []
course_units = []
course_desrption = []

for department in All_Deparments: # for each  department
    department_courses = requests.get("https://catalog.csusb.edu/coursesaz/" + department.lower() + "/")
    soup = BeautifulSoup(department_courses.text, "html.parser")
    #department has a list of courses


    courses_des = soup.find_all("p", {"class", "courseblockdesc"})
    for des in courses_des:
        des_string = des.text
        text = des_string.strip()
        course_desrption.append(text)

    courses_in_dep = soup.find_all("span", {"class", "coursetitle"}) # department / #  title
    for course in courses_in_dep:
        title = course.text.split(".")[1].strip()  # title
        number = re.findall(r'\d+', course.text) # course number
        course_number.append(int(number[0]))
        Course_title.append(title)
        Course_deparment.append(department)

    units = soup.find_all("span", {"class", "coursehours"})
    for unit in units:
        credit = re.findall(r'\d+', unit.text)  # units
        course_units.append(int(credit[0]))

courses = []
course = {}
for index in range(0, len(course_number)):
    course.update({'Department': Course_deparment[index]})
    course.update({'Number': course_number[index]})
    course.update({'Title': Course_title[index]})
    course.update({'Units': course_units[index]})
    course.update({'Description': course_desrption[index]})
    courses.append(course)
    course = {}

filename_csv = "../CSV Files/Courses.csv"
attributes = ["Department", "Number", "Title", "Units", "Description"]

with open(r'/Code/CSV Files/Courses.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(courses)




    # Course_deparment = []
    # course_number = []
    # Course_title = []
    # course_units = []
    # course_desrption = []


    # get all the courses title + abbr + number
    # courses_des = soup.find_all("p", {"class", "courseblockdesc"})
# Abbr char(255)
# Title char(255)
# Units int
# Description text
# ID_Semster int

    # test = soup.find_all("a", class_='bubblelink code')
    # for txt in test:
    #     print(txt.text)
