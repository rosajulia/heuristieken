"""
The theoretical upper bound for costs can be found when
every package in the list is transported seperately with
the most expensive ship in the fleet. 

The Verne ATV is the most expensive ship (1080) in terms of base 
costs, as well as the heaviest in terms of mass (20500). 
It's fuel to weight ratio is 0.72.

Formula's:
fuel_weight = (Mass + Payload-mass) x FtW / (1-FtW) = F
fuel_costs = Base cost + math.ceil( fuel_weight x 1000 ) x 5
"""

import csv
import math

def calc_upperbound(ship_mass, base_cost, ftw):
    
    total_cost = 0

    with open("data/CargoList3.csv", "r") as cl_3:
        reader = csv.reader(cl_3, delimiter=",")
        
        # skip header
        next(reader, None)

        # every parcel is transported in a seperate Verne ATV
        for row in reader:

            parcel_weight = float(row[1])

            fuel_weight = (base_cost + parcel_weight) * ftw / (1 - ftw)

            # round the weight up and multiple times 5 dollars
            trip_cost = base_cost + math.ceil(fuel_weight * 1000) * 5
            
            total_cost += trip_cost
        
    return total_cost