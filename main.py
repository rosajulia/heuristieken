import csv
from classes import classes

with open("data/spacecrafts.csv") as fSpace:
    reader = csv.DictReader(fSpace)
    dataSpace = [r for r in reader]

with open("data/CargoList1.csv") as fParcel:
    reader = csv.DictReader(fParcel)
    dataParcel = [r for r in reader]

print(dataSpace[0]["nation"])

cygnus = classes.Spaceship(1,1,1,1,1,1)
print(str(cygnus))