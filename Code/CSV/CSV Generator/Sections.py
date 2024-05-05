import random
from random import randrange
import csv
from random import choice

filenames = ['Buildings.csv', "Room_with_Building.csv", 'Courses.csv', 'Instructor.csv']
path = 'C:/Users/ORA PC/Desktop/Repos/DataBase_Project/Code/CSV/CSV Files/'
Delimiter = '|'

ID_building = []
ID_rooms_with_buildings = []
ID_Courses = []
ID_instructor = []

for index in range(0, len(filenames)):
    with open(path + filenames[index], mode="r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=Delimiter)
        for row in reader:
            if index == 0:
                ID_building.append(row['ID'])
            if index == 1:
                ID_rooms_with_buildings.append(row)
            if index == 2:
                ID_Courses.append(row['ID'])
            if index == 3:
                ID_instructor.append(row['ID'])

CSV_row = {}
dataset = []

ID = 1

for index in range(0, len(ID_Courses)):
    temp = random.choice([1, 2])
    for sec_number in range(0, temp):
        CSV_row.update({"ID": ID})
        CSV_row.update({"ID_Course": ID_Courses[index]})
        roo_Build = random.choice(ID_rooms_with_buildings)
        room = roo_Build['ID_Room']
        build = roo_Build['ID_Building']
        CSV_row.update({"ID_Room": room})
        CSV_row.update({"ID_Building": build})
        CSV_row.update({"ID_Instructor": random.choice(ID_instructor)})
        time = (randrange(12) + 9)
        CSV_row.update({"Start_Time": str(time) + ":" + "00:00"})
        time2 = (randrange(12) + 9)
        CSV_row.update({"End_Time": str(time2) + ":" + "00:00"})
        CSV_row.update({"Days": 1})
        CSV_row.update({"Max_Cap": 30})
        CSV_row.update({"Max_Wait": 20})
        dataset.append(CSV_row)
        CSV_row = {}
        ID += 1


path = 'C:/Users/ORA PC/Desktop/Repos/DataBase_Project/Code/CSV/CSV Files/'
Delimiter = '|'

filename_csv = "Section.csv"
attributes = ['ID', 'ID_Course', 'ID_Room', "ID_Building", 'ID_Instructor', 'Start_Time', 'End_Time', 'Days', 'Max_Cap', "Max_Wait"]

with open(path + filename_csv, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(dataset)
