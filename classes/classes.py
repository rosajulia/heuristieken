import csv

class Spaceship():
    """Spaceship object with properties from CSV file."""
    def __init__(self, name, agency, max_weigth, max_volume, base_cost, ftw):
        self.name = name
        self.agency = agency
        self.max_weigth = max_weigth
        self.max_volume = max_volume
        self.base_cost = base_cost
        self.ftw = ftw

    def __str__(self):
        return "Spaceship name: {}.\nAgency: {}.\nMW: {}.\nMV: {}.\nBC: {}.\nF2W: {}.".format(self.name, self.agency, self.max_weigth, self.max_volume, self.base_cost, self.ftw)
	
with open("spacecrafts.csv") as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

print(data[1]["nation"])

# class Parcel():
#     """Parcel object with properties from CSV file."""
#     def __init__(self, weight, volume, location=0):
#         self.weight = weight
#         self.volume = volume
#         self.ratio = ratio
#         self.location = location
#
# class Inventory():
#     """Inventory."""
#     def __init__(self, arg):
#         self.arg = arg
#     def 