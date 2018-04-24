import csv

class Spaceship():
    """Spaceship object with properties from CSV file."""
    def __init__(self, name, agency, mass, max_weigth, max_volume, base_cost, ftw):
        self.name = name
        self.agency = agency
        self.mass = mass
        self.max_weigth = max_weigth
        self.max_volume = max_volume
        self.base_cost = base_cost
        self.ftw = ftw

    def __str__(self):
        return "Spaceship name: {}.\nAgency: {}.\nMW: {}.\nMV: {}.\nBC: {}.\nF2W: {}.".format(self.name, self.agency, self.max_weigth, self.max_volume, self.base_cost, self.ftw)

with open("spacecrafts.csv") as fSpace:
    reader = csv.DictReader(fSpace)
    dataSpace = [r for r in reader]

print(dataSpace[2]["nation"])
print(str(dataSpace))

class Parcel():
    """Parcel object with properties from CSV file."""
    def __init__(self, id, weight, volume, location=0):
        self.id = id
        self.weight = weight
        self.volume = volume
        self.ratio = ratio
        self.location = location

with open("CargoList1.csv") as fParcel:
    reader = csv.DictReader(fParcel)
    dataParcel = [r for r in reader]

class Inventory():
    """Inventory."""
    def __init__(self, arg):
        self.arg = arg

# class ClassName(object):
#     """docstring for ."""
#     def __init__(self, arg):
#         super(, self).__init__()
#         self.arg = arg
