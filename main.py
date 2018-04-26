import csv
from classes import classes
# volgens mij hebben we deze niet echt hier nodig:
# from calculations import minmaxcosts
from scripts import randomalgorithm

# read spaceship data from csv into dict
with open("data/spacecrafts.csv") as file_space:
    reader = csv.DictReader(file_space)
    data_space = [r for r in reader]
    list_space = []

# attempt at creating class objects for all spaceships (works right now, but output is string-ish, see below)
# ship format is as following:
    # OrderedDict([('spacecraft', 'Cygnus'), ('nation', 'USA'), ('organisation', 'Nasa'), ('payload mass', '2000'), ('payload volume', '18.9'), ('mass', '7400'), ('base cost', '390'), ('ftw', '0.73')])
# spaceship format is as following: (output of class)
    # Spaceship name: 1
    # MW: 2000.0,
    # MV: 18.9,
    # BC: 390000000,
    # F2W: 0.73.
# NOTA BENE: id namen beginnen nu bij 1 en niet bij 0
counter = 1
for ship in data_space:
    spaceship = classes.Spaceship(counter, ship["mass"], ship["payload mass"], ship["payload volume"], ship["base cost"], ship["ftw"])
    counter += 1
    list_space.append(spaceship)
    # list_space format as follows:
        # [Spaceship name: 1
        # MW: 2000.0,
        # MV: 18.9,
        # BC: 390000000,
        # F2W: 0.73?, Spaceship name: 2
        # MW: 2400.0,
        # MV: 7.6,
        # BC: 175000000, (......)]


# read cargo data into dict
with open("data/CargoList1.csv") as file_parcel:
    reader = csv.DictReader(file_parcel)
    data_parcel = [r for r in reader]
    list_parcel = []

# attempt at creating class objects for all spaceships (works right now, but output is string-ish, see below)
# unit format is as follows:
    # OrderedDict([('parcel_ID', 'CL1#1'), ('weight (kg)', '159.5'), ('volume (m^3)', '0.516')])
# parcel format is as follows:
    # ID: 1,
    # Weight: 159.5,
    # Volume: 0.516,
    # Ratio: 309.1085271317829,
    # Location: 0?
counter2 = 1
for unit in data_parcel:
    parcel = classes.Parcel(counter2, unit["weight (kg)"], unit["volume (m^3)"])
    counter2 += 1
    list_parcel.append(parcel)
# list_parcel format as follows:
    # [ID: 1,
    # Weight: 159.5,
    # Volume: 0.516,
    # Ratio: 309.1085271317829,
    # Location: 0?, ID: 2,
    # Weight: 151.5,
    # Volume: 0.459, (.....)]



# hieronder zijn testprintjes
# print(data_space[0]["nation"])
#
# cygnus = classes.Spaceship(1,1,1,1,1,1)
# print(str(cygnus))

randomalgorithm.random_algorithm(list_space, list_parcel)
