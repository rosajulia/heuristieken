#!/usr/bin/python

import sys
import datetime
from scripts import randomalgorithm, dataloader, graph, greedyratio
from classes import classes

from flask import Flask, render_template, Response
import time

# necessary for this script: pip install matplotlib
# furute ref: https://www.tutorialspoint.com/python/python_command_line_arguments.htm

app = Flask(__name__, template_folder="scripts")

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
    cargo_data = "data/CargoList1.csv"
    inventory = dataloader.load_data(ship_data, cargo_data)

    # start greedy algorithm
    for _ in range(int(sys.argv[1])):
        print('{}: Start greedy algorithm...'.format(datetime.datetime.now().strftime("%H:%M:%S")))
        
        generator = greedyratio.greedy_ratio(inventory.dict_space, inventory.dict_parcel)

        # initialize generator for visualisation
        def generate():
            weight = 0

            while weight <= 100:
                yield "data:" + str(weight) + "\n\n"
                weight = weight + next(generator)[0] / 2000 * 100

        return Response(generate(), mimetype= 'text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
