import random
from random import randrange
import csv
from random import choice

filenames = ['Room.csv', 'Courses.csv', 'Instructor.csv', "Semster.csv"]
path = 'C:/Users/ORA PC/Desktop/Repos/DataBase_Project/CSV/CSV Files/'
Delimiter = '|'

ID_Room = []
ID_Courses = []
Units_course = []
ID_insuctor = []
ID_semster = []

for index in range(0, len(filenames)):
    with open(path + filenames[index], mode="r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=Delimiter)
        for row in reader:
            if (index == 0):
                ID_Room.append(row['ID'])
            if (index == 1):
                ID_Courses.append(row['ID'])
                Units_course.append(row['Units'])
            if (index == 2):
                ID_insuctor.append(row['ID'])
            if (index == 3):
                ID_semster.append(row['ID'])

CSV_row = {}
dataset = []
instructor_hours = 0
Instructor_index = 0
time_start = 9
room_counter = 0

ID = 1
for term in range(0, len(ID_semster)):
    for amount_courses in range(0, len(ID_Courses) - 50):
        course = random.choice(range(0, len(ID_Courses)))
        amount_section = random.choice([1, 2])
        for sec in range(0, amount_section):
            CSV_row.update({"ID": ID})
            ID += 1
            instructor_hours += int(Units_course[course])
            CSV_row.update({"ID_Instructor": ID_insuctor[Instructor_index % len(ID_insuctor)]})
            if (instructor_hours > 40):
                instructor_hours = 0
                Instructor_index += 1
            CSV_row.update({"Max_Cap": 30})
            CSV_row.update({"Max_Wait": 10})
            CSV_row.update({"Start_Time": str(time_start) + ':00:00'})
            time_start += int(Units_course[course])
            CSV_row.update({"End_Time": str(time_start) + ':00:00'})
            if (time_start > 17):
                time_start = 9
                room_counter += 1
            CSV_row.update({"ID_Room": ID_Room[room_counter % len(ID_Room)]})
            CSV_row.update({"ID_Course": ID_Courses[course]})
            frist = random.choice([0, 1, 10])
            second = random.choice([100, 1000, 10000])
            temp = frist + second
            days = int("{:05d}".format(int(temp)))
            CSV_row.update({"Days": days})
            dataset.append(CSV_row)
            CSV_row = {}


filename_csv = r"\Section.csv"
attributes = ['ID', 'ID_Course', 'ID_Room', 'ID_Instructor', 'Start_Time', 'End_Time', 'Days', 'Max_Cap', "Max_Wait"]

with open(path + filename_csv, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(dataset)
