import csv
from classes import classes
from statistics import mean
import upperbounds as bounds

def write_results(solutions, args):
    """
    This script writes results to a csv file. A result is defined as a fleet 
    with a parcel distribution. It logs all command line arguments that are used
    for that run of the program and its results.

    Takes one argument: a list of all input arguments provided in main.
    """

    infile = "data/results.csv"
    inventory_type = type(classes.Inventory(None, None))
    id_counter = 0

    with open(infile, 'a', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')

        # write header with column names
        writer.writerow(["sol_id", "cargolist", "ships", "constr", "algo", "b_var", "hc", "hc_n", "iter_n", "packages_n", "total_costs", "total_costs_pct", "mass_pct", "volume_pct"])

        # for every row in the solution
        for solution in solutions:

            # check if the solution is of type inventory
            if type(solution) == inventory_type:

                # store fleet of the solution
                fleet = solution.dict_space

                # parameter variables
                cargo = args[0]
                ships = args[1]
                constr = args[2]
                algo = args[3]
                b_var = args[4]
                hc = args[5]
                hc_n = args[6]
                iter_n = args[7]

                # result variables
                packages_n = solution.parcel_amount
                total_costs = solution.calculate_costs(constr)
                total_costs_pct = round((total_costs / bounds.calc_upperbound()) * 100, 2)
                mass_pct = round(mean([(ship.current_weight / ship.max_weight) * 100 for ship in fleet]), 2)
                volume_pct = round(mean([(ship.current_volume / ship.max_volume) * 100 for ship in fleet]), 2)


                # write evey row in the csv
                writer.writerow([id_counter, cargo, ships, constr, algo, b_var, hc, hc_n, iter_n, packages_n, total_costs, total_costs_pct, mass_pct, volume_pct])

                id_counter += 1