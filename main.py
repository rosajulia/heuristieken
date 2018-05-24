#!/usr/bin/python

import sys
import datetime
from algorithms import randomalgorithm, greedyratio, hillclimber, binpackvariations
from data import dataloader
from classes import classes
from scripts import graph, helpers, best_solutions, generateships
from copy import copy, deepcopy
from visualisation import visual

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
    parser.add_argument('-c', "-cargo", help='Cargolist: 1, 2, 3 [default: 1]', nargs='?', default='1', required=False)
    parser.add_argument('-s', "-ships", help='More than 4 ships: yes or no [default: no]', nargs='?', default='no', required=False)
    parser.add_argument('-p', "-politics", help='Political constraints: true or false [default: false]', nargs='?', default='False', required=False)
    parser.add_argument('-a', "-algorithms", help='Algorithm: greedy, random, bin [default: greedy]', nargs='?', default='greedy', required=False)
    parser.add_argument('-b', "-bin_variation", help='Bin-packing variation: first, best, worst [default: first]', nargs='?', default='first', required=False)
    parser.add_argument('-hc', "-hillclimber", help='Hillclimber: yes or no [default: yes]', nargs='?', default='no', required=False)
    parser.add_argument('-hci', "-hc_iterations", help='Hillclimber iteration: int [default: 20]', nargs='?', default='20', required=False)
    parser.add_argument('-i', "-iterations", help="Iterations: int [default: ", nargs='?', default='5', required=False)
    args = parser.parse_args()
    
    # show values
    print("Cargolist: %i" % int(args.c))
    print("More than 4 ships: %s" % args.s)
    print("Political constraints: %s" % bool(args.p))
    print("Bin variation: %s" % args.b)
    print("Algorithm: %s" % args.a)
    print("Hillclimber: %s" % args.hc)
    print("Hillclimber iterations: %s" % int(args.hci))
    print("Iterations: %i" % int(args.i))
    
    # load data
    ship_data = "data/spacecrafts.csv"
    cargo_data = "data/CargoList%s.csv" % args.c
    inventory = dataloader.load_data(ship_data, cargo_data)
    repetitions = int(args.i)
    repetition_hillclimber = int(args.hci)

    if args.s == "no":
        inventory.dict_space = inventory.dict_space[:4]
    else:
        generateships.generateships(inventory, args.p)

    # start algorithm
    print('{}: Start algorithm...'.format(datetime.datetime.now().strftime("%H:%M:%S")))

    if args.a is "greedy":
        solutions = greedyratio.greedy_ratio(inventory, repetitions)
    elif args.a is "random":
        solutions = randomalgorithm.random_algorithm(inventory, repetitions)
    else:
        solutions = binpackvariations.binpack(inventory, args.b, args.p, repetitions)

    print('{}: Finished running {} times.'.format(datetime.datetime.now().strftime("%H:%M:%S"), args.i))

    # calculate best solution
    best_solution = best_solutions.solutions(solutions)
    best_solution = best_solution[0]
    parcel_amount = best_solution[1]
    costs = best_solution[2]

    if args.hc == "yes":
        hillsolution = hillclimber.hill_climber(best_solution, repetition_hillclimber)
        best_solution = hillsolution

    # start visualisation with more than 4 ships
    if args.s == "no":   
        d = visual.visual(args.s, best_solution)
        return render_template("visual.html", d=d, parcel_amount=parcel_amount, costs=costs)
    else:
        d = visual.visual(args.s, best_solution)
        return render_template("terminal.html")

if __name__ == "__main__":
    app.run(debug=True)