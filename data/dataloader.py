import csv
from classes import classes

def load_data(ship_data, cargo_data):
    """
    This script loads csv files containing information on the different 
    spaceships and cargo lists.

    Returns an object of type Inventory.

    Take two arguments:

        ship_data: Path to csv file containing the spaceship data.

        cargo_data: Path to csv file containing the cargolist data.
    """

    ship_counter = 1
    parcel_counter = 0

    # open the csv file containing cargo list
    with open(cargo_data) as parcel_data:
        reader = csv.DictReader(parcel_data)

        # write the csv rows to a list
        data_parcel = [r for r in reader]

    # create a list to hold all the parcel objects
    list_parcel = []

    # create parcel objects and append to the list
    for unit in data_parcel:
        parcel = classes.Parcel(parcel_counter, unit["weight (kg)"], unit["volume (m^3)"])
        parcel_counter += 1
        list_parcel.append(parcel)

    # open the csv file containing information about ships
    with open(ship_data) as csv_data:
        reader = csv.DictReader(csv_data)
        data_space = [r for r in reader]

    # create a list to hold spaceship objects
    list_space = []

    # create spaceship objects and append to the list
    for ship in data_space:
        spaceship_info = classes.Spaceship(ship_counter, ship["type"], ship["nation"], ship["mass"], ship["payload mass"], ship["payload volume"], ship["base cost"], ship["ftw"])
        spaceship_info.current_weight = 0
        spaceship_info.current_volume = 0
        spaceship_info.full = False
        ship_counter += 1
        list_space.append(spaceship_info)

    # store both lists
    data = [list_space, list_parcel]
    inventory = classes.Inventory(data[0], data[1])

    return inventory
