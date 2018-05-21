#!/usr/bin/python

import sys
import datetime
from algorithms import randomalgorithm
from scripts import graph, greedyratio, helpers
from data import dataloader
from classes import classes
from copy import copy, deepcopy

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

    costs = 0
    costs_list = []
    parcel_amount_list = []

    repetitions = int(sys.argv[1])

    # hier een ifje om te splitsen per algoritme obv command-line arguments

    solutions = randomalgorithm.random_algorithm(inventory, repetitions)

    # collect all parcel amounts in list and determine highest
    for solution in solutions:
        parcel_amount_list.append(solution.parcel_amount)
    max_parcel_amount = max(parcel_amount_list)

    # continue with solutions with max parcel amount
    parcel_checked_solutions = []
    for solution in solutions:
        if solution.parcel_amount is max_parcel_amount:
            parcel_checked_solutions.append(deepcopy(solution))

    # collect all costs of remaining solutions in list and determine lowest
    for solution in parcel_checked_solutions:
        costs_list.append(solution.total_costs)
    min_costs = min(costs_list)

    # save solution(s) with lowest cost
    best_solutions = []
    for solution in parcel_checked_solutions:
        if solution.total_costs is min_costs:
            best_solutions.append(deepcopy(solution))

    print('{}: Finished running {} times.'.format(datetime.datetime.now().strftime("%H:%M:%S"), sys.argv[1]))

    print("Maximum amount of parcels in ship: {}".format(max_parcel_amount))
    print("Corresponding costs: {}". format(min_costs))

    # visualize which ships contain which parcels in best solution(s)
    for solution in best_solutions:
        print(helpers.visualizeParcelsPerShip(solution))

    # plot parcel amounts of all found solutions in histogram
    graph.barchart([solution.parcel_amount for solution in solutions])

if __name__ == "__main__":
    main()
