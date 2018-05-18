#!/usr/bin/python

import sys
import datetime
from algorithms import randomalgorithm
from scripts import graph, greedyratio
from data import dataloader
from classes import classes

# necessary for this script: pip install matplotlib
# furute ref: https://www.tutorialspoint.com/python/python_command_line_arguments.htm

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py integer")
        sys.exit(1)

    # load data
    ship_data = "data/spacecrafts.csv"
    cargo_data = "data/CargoList1.csv"
    inventory = dataloader.load_data(ship_data, cargo_data)

    print('{}: Start random algorithm...'.format(datetime.datetime.now().strftime("%H:%M:%S")))

    # make list of solutions
    solutions = []
    costs = 0

    for i in range(int(sys.argv[1])):
        # result = randomalgorithm.random_algorithm(inventory.dict_space, inventory.dict_parcel)
        result = randomalgorithm.random_algorithm(inventory)
        # calculate total costs
        weight = [result.get("weight1"), result.get("weight2"), result.get("weight3"), result.get("weight4")]

        for ship in range(len(inventory.dict_space)):
            costs += inventory.calculate_fuel_costs(ship, weight[ship])

        # append solutions to list
        solutions.append(classes.Inventory(inventory.dict_space, inventory.dict_parcel, \
                            i, result.get("parcel_amount"), costs))

    # calculate best solution parcel-wise
    best_parcel = (max([solution.parcel_amount for solution in solutions]))
    for solution in solutions:
        if solution.parcel_amount == best_parcel:
            best_parcel_costs = solution.total_costs

    # calculate best solution cost-wise
    best_costs = (min([solution.total_costs for solution in solutions]))
    for solution in solutions:
        if solution.total_costs == best_costs:
            best_costs_parcels = solution.parcel_amount


    print('{}: Finished running {} times.'.format(datetime.datetime.now().strftime("%H:%M:%S"), sys.argv[1]))

    print("Maximum amount of parcels in ship: {}".format(best_parcel))
    print("Corresponding costs: {}". format(best_parcel_costs))

    print("The lowest costs of all solutions: {}".format(best_costs))
    print("Corresponding amount of parcels moved: {}".format(best_costs_parcels))

    # plot solutions in histogram
    graph.barchart([solution.parcel_amount for solution in solutions])

if __name__ == "__main__":
    main()
