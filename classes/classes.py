class Spaceship():
    """Spaceship object with properties from CSV file."""
    def __init__(self, id, mass, max_weight, max_volume, base_cost, ftw, current_weight=0, current_volume=0):
        self.id = int(id)
        self.mass = int(mass)
        self.max_weight = float(max_weight)
        self.max_volume = float(max_volume)
        self.base_cost = int(base_cost) * 1000000
        self.ftw = float(ftw)
        self.current_weight = current_weight
        self.current_volume = current_volume

    def tryShip(self):
        return {"id": self.id, "mass": self.mass, "max_weight": self.max_weight, "max_volume": self.max_volume, "base_cost": self.base_cost, "ftw": self.ftw, "current_weight": self.current_weight, "current_volume": self.current_volume}

class Parcel():
    """Parcel object with properties from CSV file."""
    def __init__(self, id, weight, volume, location=0):
        self.id = int(id)
        self.weight = float(weight)
        self.volume = float(volume)
        self.ratio = self.weight/self.volume
        self.location = int(location)

    def tryParcel(self):
        return {"id": self.id, "weight": self.weight, "volume": self.volume, "ratio": self.ratio, "location": self.location}

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

    # hierbij moet in main dan nog een functie die zegt dat je deze functies per schip aan moet roepen en dan bij elkaar optellen
