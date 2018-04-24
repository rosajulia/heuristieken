class Spaceship():
    """Spaceship object with properties from CSV file."""
    def __init__(self, id, mass, max_weigth, max_volume, base_cost, ftw):
        self.id = id
        self.mass = mass
        self.max_weigth = max_weigth
        self.max_volume = max_volume
        self.base_cost = base_cost
        self.ftw = ftw

    def __str__(self):
        return "Spaceship name: {}.\nMW: {}.\nMV: {}.\nBC: {}.\nF2W: {}.".format(self.id, self.max_weigth, self.max_volume, self.base_cost, self.ftw)

class Parcel():
    """Parcel object with properties from CSV file."""
    def __init__(self, id, weight, volume, ratio, location=0):
        self.id = id
        self.weight = weight
        self.volume = volume
        self.ratio = ratio
        self.location = location

    def __str__(self):
        return "ID: {}.\nWeight: {}.\nVolume: {}.\nRatio: {}.\nLocation: {}.".format(self.id, self.weight, self.volume, self.ratio, self.location)

class Inventory():
    """Inventory."""
    def __init__(self, id_space, dict_space, dict_parcel, ftw):
        self.id_space = id_space
        self.dict_space = dict_space
        self.dict_parcel = dict_parcel
        self.ftw = ftw
    
    def calculate_fuel_weight(self):
        return (self.dict_space[self.id_space]["mass"] + self.dict_space[self.id_space]["max_weight"] * self.dict_space[self.id_space]["ftw"] / (1 - self.dict_space[self.id_space]["ftw"]))
    
    def calculate_fuel_costs(self):
        return self.dict_space[self.id_space]["base_cost"] + self.ftw * 100 * 5
