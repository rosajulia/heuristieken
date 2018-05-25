import csv
from classes import classes
from statistics import mean
import upperbounds as bounds

def writeresults(solutions, cargo, ships, constr, algo, b_var, hc, hc_n, iter_n):
# def writeresults(solutions, args):

    """
    This script writes results to a csv file. A result is defined as a fleet 
    with a parcel distribution. It logs all command line arguments that are used
    for that run of the program and its results.
    Takes eight arguments:
    """

    infile = "data/results.csv"
    inventory_type = type(classes.Inventory(None, None))
    id_counter = 0

    with open(infile, 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')

        # write header with column names
        writer.writerow("sol_id", "cargolist", "ships", "constr", "algo", "b_var", "hc", "hc_n", "iter_n", "packages_n", "total_costs", "total_costs_pct", "mass_pct", "volume_pct")

        # for every row in the solution
        for solution in solutions:

            # check if the solution is of type inventory
            if type(solution) == inventory_type:

                # store fleet of the solution
                fleet = solution.dict_space

                # result variables
                packages_n = solution.parcel_amount
                total_costs = solution.calculate_costs()
                total_costs_pct = total_costs / bounds.calc_upperbound()
                mass_pct = mean([ship.current_weight for ship in fleet])
                volume_pct = mean([ship.current_volume for ship in fleet])

                # write evey row in the csv
                writer.writerow(id_counter, cargo, ships, constr, algo, b_var, hc, hc_n, iter_n, packages_n, total_costs, total_costs_pct, mass_pct, volume_pct)

                id_counter += 1