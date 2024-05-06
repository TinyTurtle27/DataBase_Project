from random import randrange
import csv

filename = r'\Buildings.csv'
path = r"C:\Users\ORA PC\Desktop\Repos\DataBase_Project\CSV\CSV Files"
Delimiter = '|'

Rooms = {}
dataset = []
index = 1
size = 0

junction_row = {}
junction_dataset = []
realdataset = []

with open(path + filename, mode="r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=Delimiter)
    for row in reader:
        floors = randrange(2) + 2
        for floor in range(1, floors):
            lim = randrange(10) + 10
            for room_number in range(0, lim):
                Rooms.update({"ID": index}) # ID
                number = floor * 1000 + room_number
                Rooms.update({"Number": number}) # room number
                dataset.append(Rooms)
                index += 1
                Rooms = {}
        for roo in range(0, len(dataset)):
            dataset[roo].update({"ID_Building": row['ID']})
        realdataset.extend(dataset)
        dataset = []



filename_csv = r"\Room.csv"
attributes = ['ID', 'Number', 'ID_Building']

with open(path + filename_csv, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, attributes, delimiter="|")
    writer.writeheader()
    writer.writerows(realdataset)

# jun_name = "Room_with_Building.csv"
# att = ["ID_Room", "ID_Building"]
#
# with open(path + jun_name, 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, att, delimiter="|")
#     writer.writeheader()
#     writer.writerows(junction_dataset)