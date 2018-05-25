#!/usr/bin/python

import sys
import datetime
from algorithms import randomalgorithm, greedyratio, hillclimber, binpackvariations
from data import dataloader
from classes import classes
from helperscripts import helpers
from prepscripts import generateships
from copy import copy, deepcopy
from visualisation import visual, graph, best_solutions

from flask import Flask, render_template, Response, jsonify
import time
import argparse

# necessary for this script: pip install matplotlib
# future ref: https://www.tutorialspoint.com/python/python_command_line_arguments.htm

app = Flask(__name__, template_folder="visualisation")


@app.route("/")
def main():
    # initialize command-line arguments
    parser = argparse.ArgumentParser(description='Calculate the optimal organisation of a cargolist in spaceships')
    parser.add_argument("-c", "-cargo", help='Cargolist: 1, 2, 3 [default: 1]', nargs='?', type=int, \
                        default='1', required=False)
    parser.add_argument("-s", "-ships", help="Use more ships than 4", action="store_true")
    parser.add_argument("-p", "-politics", help="Use political constraints", action="store_true")
    parser.add_argument("-a", "-algorithms", help='Algorithm: greedy, random, bin [default: greedy]', nargs='?', type=str, \
                        default='greedy', required=False)
    parser.add_argument("-b", "-bin_variation", help='Bin-packing variation: first, best, worst [default: first]', nargs='?', \
                        type=str, default='first', required=False)
    parser.add_argument("-hc", "-hillclimber", help="Use hillclimber", action="store_true")
    parser.add_argument("-hci", "-hc_iterations", help='Hillclimber iteration: int [default: 20]', nargs='?', default='20', \
                        type=int, required=False)
    parser.add_argument("-i", "-iterations", help="Iterations: int [default: 5]", nargs='?', default='5', type = int, \
                        required=False)
    args = parser.parse_args()

    # show values
    print("Algorithm: %s" % args.a)
    print("Iterations: %i" % int(args.i))
    print("Cargolist: %i" % int(args.c))
    print("More than 4 ships: %s" % args.s)
    print("Hillclimber: %s" % args.hc)
    print("Hillclimber iterations: %s" % int(args.hci))
    print("Political constraints: %s" % args.p)
    print("Bin variation: %s" % args.b)

    # load data
    ship_data = "data/spacecrafts.csv"
    cargo_data = "data/CargoList%s.csv" % args.c
    inventory = dataloader.load_data(ship_data, cargo_data)
    repetitions = int(args.i)
    repetition_hillclimber = int(args.hci)

    if args.s is False:
        inventory.dict_space = inventory.dict_space[:4]
    else:
        generateships.generateships(inventory, args.p)

    # start algorithm
    print('{}: Start algorithm...'.format(datetime.datetime.now().strftime("%H:%M:%S")))

    if args.a == "greedy":
        solutions = greedyratio.greedy_ratio(inventory, repetitions, args.p)
    elif args.a == "random":
        solutions = randomalgorithm.random_algorithm(inventory, repetitions, args.p)
    elif args.a == "bin":
        solutions = binpackvariations.binpack(inventory, args.b, repetitions, args.p)

    print('{}: Finished running {} times.'.format(datetime.datetime.now().strftime("%H:%M:%S"), args.i))

    # calculate best solution
    best_solution = best_solutions.solutions(solutions)

    result = best_solution[0]
    parcel_amount = best_solution[1]
    costs = best_solution[2]

    if args.hc is True:
        hillsolution = hillclimber.hill_climber(result, repetition_hillclimber, args.p)
        best_solution = hillsolution

    d = visual.visual(len(inventory.dict_space), result)

    # start visualisation with more than 4 ships
    if args.s is False:   
        return render_template("visual.html", d=d, parcel_amount=parcel_amount, costs=costs)
    else:
        return render_template("terminal.html", d=d, parcel_amount=parcel_amount, costs=costs)

if __name__ == "__main__":
    app.run(debug=True)
