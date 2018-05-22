"""
Calculates the 'cheapest' ships given that:
- there are no constraints on the availability of the ships
(i.e. any number of ships can be used any number of times)
- every ship is filled completely in terms of mass
- disregard volumes as influence on costs

Formula's:
fuel_weight = (Mass + Payload-mass) x FtW / (1-FtW) = F
fuel_costs = Base cost + math.ceil( fuel_weight x 1000 ) x 5
"""

import csv
import math

def calc_shipcost():

    results = []

    with open("data/spacecrafts.csv", "r") as spacecrafts:
        fleet = csv.reader(spacecrafts, delimiter=",")

        next(fleet, None)

        for ship in fleet:
            
            ship_fuel_weight = (float(ship[5]) + float(ship[3])) * float(ship[7]) / (1 - float(ship[7]))

            ship_trip_cost = float(ship[6]) + math.ceil(ship_fuel_weight * 1000) * 5

            total_mass = float(ship[3]) + float(ship[5])

            results.append(ship_trip_cost / total_mass)

    return results