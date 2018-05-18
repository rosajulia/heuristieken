import math

class Spaceship():
    """Spaceship object with properties from CSV file."""
    def __init__(self, id, nation, mass, max_weight, max_volume, base_cost, ftw, current_weight=0, current_volume=0, full=False):
        self.id = int(id)
        self.nation = nation
        self.mass = int(mass)
        self.max_weight = float(max_weight)
        self.max_volume = float(max_volume)
        self.base_cost = int(base_cost) * 1000000
        self.ftw = float(ftw)
        self.current_weight = current_weight
        self.current_volume = current_volume
        self.full = full

    def returnShip(self):
        return {"id": self.id, "mass": self.mass, "max_weight": self.max_weight, "max_volume": self.max_volume, \
                     "base_cost": self.base_cost, "ftw": self.ftw, "current_weight": self.current_weight, \
                        "current_volume": self.current_volume}

class Parcel():
    """Parcel object with properties from CSV file."""
    def __init__(self, id, weight, volume, location=0):
        self.id = int(id)
        self.weight = float(weight)
        self.volume = float(volume)
        self.ratio = self.weight/self.volume
        self.location = int(location)

    def returnParcel(self):
        return {"id": self.id, "weight": self.weight, "volume": self.volume, "ratio": self.ratio, "location": self.location}

class Inventory(Spaceship, Parcel):
    """Inventory."""
    def __init__(self, dict_space, dict_parcel, solution_id = 0, parcel_amount = 0, total_costs = 0):
        self.solution_id = solution_id
        self.dict_space = dict_space
        self.dict_parcel = dict_parcel
        self.parcel_amount = parcel_amount
        self.total_costs = total_costs

    def maxParcelWeightVolume(self):
        weight_list = []
        volume_list = []
        for parcel in self.dict_parcel:
            weight_list.append(parcel.weight)
            volume_list.append(parcel.volume)
        return max(weight_list), max(volume_list)

    def calculate_fuel_costs(self, ship_id, ship_weight):
        self.ship_id = ship_id
        self.ship_weight = ship_weight

        self.fuel_weight = (self.dict_space[ship_id].mass + ship_weight) * \
                    self.dict_space[ship_id].ftw / (1 - self.dict_space[ship_id].ftw)

        self.fuel_costs = self.dict_space[ship_id].base_cost + math.ceil(self.fuel_weight * 1000) * 5
        return (self.fuel_costs)

    def return_inventory(self):
        return {"dict_space": self.dict_space, "dict_parcel": self.dict_parcel, "solution_id": self.solution_id, \
                    "parcel_amount": self.parcel_amount, "fuel_weight": self.fuel_weight, "fuel_costs": self.fuel_costs, \
                        "total_costs": self.total_costs}
