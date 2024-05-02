from bs4 import BeautifulSoup
import requests
import re

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


course_pre = []

for department in All_Deparments: # for each  department
    department_courses = requests.get("https://catalog.csusb.edu/coursesaz/" + department.lower() + "/")
    soup = BeautifulSoup(department_courses.text, "html.parser")
    #department has a list of courses


    courses_des = soup.find_all("p", {"class", "courseblockdesc"})



    

    test = soup.find_all("a", class_='bubblelink code')
    for txt in test:
        print(txt.text)




    courses_in_dep = soup.find_all("span", {"class", "coursetitle"}) # department / #  title
    for course in courses_in_dep:
        title = course.text.split(".")[1].strip()  # title
        number = re.findall(r'\d+', course.text) # course number
        course_number.append(number)
        Course_title.append(title)
        Course_deparment.append(department)

    units = soup.find_all("span", {"class", "coursehours"})
    for unit in units:
        credit = re.findall(r'\d+', unit.text)  # units
        course_units.append(credit)

courses = []
course = []
for index in range(0, len(course_number)):
    course.append(Course_deparment[index])
    course.append(course_number[index])
    course.append(Course_title[index])
    course.append(course_units[index])
    courses.append(course)
    course = []



    # get all the courses title + abbr + number
    # courses_des = soup.find_all("p", {"class", "courseblockdesc"})
