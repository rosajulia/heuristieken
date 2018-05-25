import csv
import math

def calc_upperbound():
    """
    This script used to calculate the most expensive way to transport packages
    in the third cargolist.

    The theoretical upper bound for costs can be found when every package in the
    list is transported seperately with the most expensive ship in the fleet. 

    The Verne ATV is the most expensive ship (1080) in terms of base costs, 
    as well as the heaviest in terms of mass (20500). It's fuel to weight ratio 
    is 0.72.

    Returns the upper bound of costs to transport the entire cargolist.

    Formulas:
    fuel_weight = (Mass + Payload-mass) x FtW / (1-FtW)
    costs = Base cost + math.ceil(fuel_weight x 1000) x 5
    """
    
    # verne atv attributes needed for the formula
    total_cost = 0
    mass = 20500
    base_cost = 1080
    ftw = 0.72

    with open("data/CargoList3.csv", "r") as cl_3:
        reader = csv.reader(cl_3, delimiter=",")
        
        # skip header
        next(reader, None)

        # every parcel is transported in a seperate Verne ATV
        for row in reader:

            parcel_weight = float(row[1])

            fuel_weight = (mass + parcel_weight) * ftw / (1 - ftw)

            # round the weight up and multiple times 5 dollars
            trip_cost = base_cost + math.ceil(fuel_weight * 1000) * 5
            
            total_cost += trip_cost
        
    return total_cost