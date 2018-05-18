#!/usr/bin/python

import sys
import datetime
from algorithms import randomalgorithm, greedyratio
from data import dataloader
from visualisation import graph
from classes import classes

from flask import Flask, render_template, Response
import time

# necessary for this script: pip install matplotlib
# furute ref: https://www.tutorialspoint.com/python/python_command_line_arguments.htm

app = Flask(__name__, template_folder="visualisation")

@app.route("/")
def index():
    return render_template("visual.html")

@app.route('/progress')
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py integer")
        sys.exit(1)

    # load data
    ship_data = "data/spacecrafts.csv"

    # hieronder de 1 aanpassen naar bijbehorend command-line argument
    cargo_data = "data/CargoList1.csv"

    # dataloader aanroepen met 4/oneindig en wel/geen constraints
    inventory = dataloader.load_data(ship_data, cargo_data)

    # create list for solutions
    solutions = []
    costs = 0

    # hier ofwel random, ofwel greedy, ofwel hillclimber aanroepen met aantal keer

    # start greedy algorithm (command-line argument nog aanpassen!)
    # deze for loop moet in het algoritme niet erbuiten (vooral vanwege hillclimber)
    for _ in range(int(sys.argv[1])):
        print('{}: Start greedy algorithm...'.format(datetime.datetime.now().strftime("%H:%M:%S")))

        # de generator slaat de geyielde waardes op
        generator = greedyratio.greedy_ratio(inventory)

        for result in generator:
            try:
                result = next(generator)
                print(result[0])
            except:
                print("error")
                break

        exit(1)

        # result = next(generator)
        #
        # # calculate total costs
        # result_weight = [result.get("weight1"), result.get("weight2"), result.get("weight3"), result.get("weight4")]
        #
        # for ship in range(len(inventory.dict_space)):
        #     costs += inventory.calculate_fuel_costs(ship, result_weight[ship])
        #
        # # append solutions to list
        # solutions.append(classes.Inventory(inventory.dict_space, inventory.dict_parcel, \
        #                     i, result.get("parcel_amount"), costs))



        # initialize generator for visualisation
        def generate():
            weight = 0

            while weight <= 100:
                yield "data:" + str(weight) + "\n\n"
                weight = weight + next(generator)[0] / 2000 * 100
            print(next(generator)[1])
        # stuur de response van functie generate door naar html, waar javascript er shit mee gaat doen
        return Response(generate(), mimetype= 'text/event-stream')

    # # calculate best solution parcel-wise
    # best_parcel = (max([solution.parcel_amount for solution in solutions]))
    # for solution in solutions:
    #     if solution.parcel_amount == best_parcel:
    #         best_parcel_costs = solution.total_costs
    #
    # # calculate best solution cost-wise
    # best_costs = (min([solution.total_costs for solution in solutions]))
    # for solution in solutions:
    #     if solution.total_costs == best_costs:
    #         best_costs_parcels = solution.parcel_amount
    #
    #
    # print('{}: Finished running {} times.'.format(datetime.datetime.now().strftime("%H:%M:%S"), sys.argv[1]))
    #
    # print("Maximum amount of parcels in ship: {}".format(best_parcel))
    # print("Corresponding costs: {}". format(best_parcel_costs))
    #
    # print("The lowest costs of all solutions: {}".format(best_costs))
    # print("Corresponding amount of parcels moved: {}".format(best_costs_parcels))
    #
    # # plot solutions in histogram
    # graph.barchart([solution.parcel_amount for solution in solutions])

if __name__ == '__main__':
    app.run(debug=True)
