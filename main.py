import csv

with open("data/spacecrafts.csv") as fSpace:
    reader = csv.DictReader(fSpace)
    dataSpace = [r for r in reader]

with open("data/CargoList1.csv") as fParcel:
    reader = csv.DictReader(fParcel)
    dataParcel = [r for r in reader]

print(dataSpace[2]["nation"])
print(str(dataSpace))
print(str(dataParcel))

