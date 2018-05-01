class Spaceship():
    """Spaceship object with properties from CSV file."""
    def __init__(self, id, mass, max_weight, max_volume, base_cost, ftw, current_weight, current_volume):
        # hier heb ik ints en floats van gemaakt zodat je er straks mee kunt rekenen (waren strings maar misschien straks niet meer nodig)
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

    # heb dit in repr veranderd (was str) en wat punten naar komma's en een vraagteken (om eventueel te splitten)
    # def __repr__(self):
    #     return "Spaceship name: {}\nMW: {},\nMV: {},\nBC: {},\nF2W: {}?".format(self.id, self.max_weight, self.max_volume, self.base_cost, self.ftw)

    # heb dit in repr veranderd (was str) en wat punten naar komma's en een vraagteken (om eventueel te splitten)
    # def __repr__(self):
    #     return "Spaceship name: {}\nMW: {},\nMV: {},\nBC: {},\nF2W: {}?".format(self.id, self.max_weight, self.max_volume, self.base_cost, self.ftw)
    #
    # # hieronder is poging tot subscriptable object maken, maar daarmee krijg je als je print de locaties van de objecten
    # def output(self):
    #     return str({'id': self.id, 'MW': self.max_weight, 'MV': self.max_volume, 'BC': self.base_cost, 'F2W': self.ftw })

class Parcel():
    """Parcel object with properties from CSV file."""
    def __init__(self, id, weight, volume, location=0):
        # hier heb ik ints en floats van gemaakt zodat je er straks mee kunt rekenen (waren strings maar misschien straks niet meer nodig)
        self.id = int(id)
        self.weight = float(weight)
        self.volume = float(volume)
        self.ratio = self.weight/self.volume
        self.location = int(location)

    def tryParcel(self):
        return {"id": self.id, "weight": self.weight, "volume": self.volume, "ratio": self.ratio, "location": self.location}

    # heb dit in repr veranderd (was str) en wat punten naar komma's en een vraagteken (om eventueel te splitten)
    # def __repr__(self):
    #     return "ID: {},\nWeight: {},\nVolume: {},\nRatio: {},\nLocation: {}?".format(self.id, self.weight, self.volume, self.ratio, self.location)

    # hieronder is poging tot subscriptable object maken, maar daarmee krijg je als je print de locaties van de objecten
    # def output(self):
    #     return str({'ID': self.id, 'Weight': self.weight, 'Volume': self.volume, 'Ratio': self.ratio, 'Location': self.location})

class Inventory():
    """Inventory."""
    # volgens mij mag ftw hier uit want dat is voor ieder ship anders en haal je uit dict space(?)
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
