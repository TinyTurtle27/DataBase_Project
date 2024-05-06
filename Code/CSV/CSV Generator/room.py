from random import randrange
import csv

filename = 'Buildings.csv'
path = 'C:/Users/ORA PC/Desktop/Repos/DataBase_Project/Code/CSV/CSV Files/'
Delimiter = '|'

Rooms = {}
dataset = []
index = 1

junction_row = {}
junction_dataset = []

with open(path + filename, mode="r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=Delimiter)
    for row in reader:
        floors = randrange(2) + 2
        for floor in range(1, floors):
            lim = randrange(10) + 10
            for room_number in range(0, lim):
                Rooms.update({"ID": index})
                number = floor * 1000 + room_number
                Rooms.update({"Number": number})
                dataset.append(Rooms)
                Rooms = {}
                index += 1
        for roo in range(0, len(dataset)):
            dic = dataset[roo]
            junction_row.update({"ID_Room": dic["ID"]})
            junction_row.update({"ID_Building": row['ID']})
            junction_dataset.append(junction_row)
            junction_row = {}

filename_csv = "Room.csv"
attributes = ['ID', 'Number']

with open(path + filename_csv, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(dataset)

jun_name = "Room_with_Building.csv"
att = ["ID_Room", "ID_Building"]

with open(path + jun_name, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, att, delimiter="|")
    writer.writeheader()
    writer.writerows(junction_dataset)