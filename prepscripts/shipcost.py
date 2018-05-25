import csv
import math

def calc_shipcost():
    """
    This script calculates the costs of every ship given that:
        - there are no constraints on the availability of the ships
        (i.e. any number of ships can be used any number of times)
        - every ship is filled completely in terms of mass
        - disregard volumes as influence on costs

    Returns a list, per spaceship, of the the costs of one trip for every kg of 
    mass the ship can transport.

    Formulas:
    fuel_weight = (Mass + Payload-mass) x FtW / (1-FtW)
    costs = Base cost + math.ceil(fuel_weight x 1000) x 5
    """

    results = []

    # open the spacecrafts csv file
    with open("data/spacecrafts.csv", "r") as spacecrafts:
        fleet = csv.reader(spacecrafts, delimiter=",")

        # skip header
        next(fleet, None)

        # for every ship in the fleet
        for ship in fleet:
            
            # calculate the weight of the fuel
            ship_fuel_weight = (float(ship[5]) + float(ship[3])) * \
                                float(ship[7]) / (1 - float(ship[7]))

            # calculate the costs of one trip
            ship_trip_cost = float(ship[6]) + \
                             math.ceil(ship_fuel_weight * 1000) * 5

            # calculate the total mass of the ship
            total_mass = float(ship[3]) + float(ship[5])

            results.append(ship_trip_cost / total_mass)

    return results