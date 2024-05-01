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

department_abbrs = re.findall(r'\((.*?)\)', values.text)
# Get anything between () this is the departments

table = []
# data stored here

for department in department_abbrs: # for each  department
    department_courses = requests.get("https://catalog.csusb.edu/coursesaz/" + department.lower() + "/")
    # request list of courses offered

    soup = BeautifulSoup(department_courses.text, "html.parser")

    courses_in_dep = soup.find_all("span", {"class", "coursetitle"})
    # get all the courses title + abbr + number
    courses_des = soup.find_all("p", {"class", "courseblockdesc"})
    # get all the course des with requirements and other things

    requirements = []


    for course_des in courses_des: # for each course des we need to filter out requirements and name
        description = course_des.text.strip() # remove space in the ends
        if "Semester" in description: # see if they have requirements
            requirements.append(course_des.split(":")[1].split(".")[0]) # requirements
        else:
            requirements.append("")

        # removing all Previously or Formerly names of the course if they have them
        if "Previously" in description:
            Second_des = description.split("Previously", 1)[0]
        elif "Formerly" in description:
            Second_des = description.split("Formerly", 1)[0]
        else:
            Second_des = description

        Last number

            #print(preq.split(".")[1])
            #print(preq.split("Previously", 1)[0])
            #print(re.findall(r'\d+', preq))
    # for course in courses_in_dep:
    #     title = course.text.split(".")[1].strip()
    #     number = re.findall(r'\d+', course.text)
    #     group = [department + " " + number.pop(), title]
    #     table.append(group)









