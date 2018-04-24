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

with open("spacecrafts.csv") as f_space:
    reader = csv.DictReader(f_space)
    data_space = [r for r in reader]

# remove first line of data_space
print(data_space)

class Parcel():
    """Parcel object with properties from CSV file."""
    def __init__(self, id, weight, volume, location=0):
        self.id = id
        self.weight = weight
        self.volume = volume
        self.ratio = ratio
        self.location = location

    def __str__(self):
        return "ID: {}.\nWeight: {}.\nVolume: {}.\nRatio: {}.\nLocation: {}.".format(self.id, self.weight, self.volume, self.ratio, self.locaion)

with open("CargoList1.csv") as f_parcel:
    reader = csv.DictReader(f_parcel)
    data_parcel = [r for r in reader]

class Inventory():
    """Inventory."""
    def __init__(self, id_space, dict_space, dict_parcel):
        self.id_space = id_space
        self.dict_space = dict_space
        self.dict_parcel = dict_parcel
    def calculate_fuel_weight(self):
        fuel_weight = (dict_space[id_space]["mass"] + dict_space[id_space]["max_weight"] * dict_space[id_space]["ftw"] / (1 - dict_space[id_space]["ftw"]))
    def calculate_fuel_costs(self):
        fuel_cost = dict_space[id_space]["base_cost"] + roundup(fuel_weight * 100) * 5
