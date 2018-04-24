import csv
from classes import classes
from calculations import minmaxcosts

with open("data/spacecrafts.csv") as file_space:
    reader = csv.DictReader(file_space)
    data_space = [r for r in reader]

with open("data/CargoList1.csv") as file_parcel:
    reader = csv.DictReader(file_parcel)
    data_parcel = [r for r in reader]

print(data_space[0]["nation"])

cygnus = classes.Spaceship(1,1,1,1,1,1)
print(str(cygnus))
