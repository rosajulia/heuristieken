import csv
from classes import classes

def load_data(ship_data, cargo_data):
    """Loads a csv file as an ordered dict.

    Usage:
    loaded_data = load_data('csv_data.csv')
    """

    ship_counter = 0
    parcel_counter = 0

    # open the csv file containing information about ships
    with open(ship_data) as csv_data:
        reader = csv.DictReader(csv_data)
        data_space = [r for r in reader]

    # create a list to hold spaceship objects
    list_space = []

    # hieronder splitsen met if obv meegegeven command-line argument over 4 of oneindig schepen
    # if 4:     (en anders jesse's nieuwe generateships.py aanroepen met constraints of niet)
    # create spaceship objects and append to the list
    for ship in data_space:
        spaceship_info = classes.Spaceship(ship_counter, ship["mass"], ship["payload mass"], ship["payload volume"], ship["base cost"], ship["ftw"])
        spaceship_info.current_weight = 0
        spaceship_info.current_volume = 0
        spaceship_info.full = False
        ship_counter += 1
        list_space.append(spaceship_info)

    # open the csv file containing cargo list
    with open(cargo_data) as parcel_data:
        reader = csv.DictReader(parcel_data)
        data_parcel = [r for r in reader]

    # create a list to hold all the parcel objects
    list_parcel = []

    # create parcel objects and append to the list
    for unit in data_parcel:
        parcel = classes.Parcel(parcel_counter, unit["weight (kg)"], unit["volume (m^3)"])
        parcel_counter += 1
        list_parcel.append(parcel)

    # store both lists
    data = [list_space, list_parcel]
    inventory = classes.Inventory(data[0], data[1])

    return inventory
