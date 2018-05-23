# inventory
# > 
# sol id autoincrement
# algoritme type + parameters
# aantal pakketjes
# kosten
# percentage van upper bound
# percentage gevuld gewicht
# percentage gevuld gewicht
# pakketjes in ship

import csv
from classes import classes
from statistics import mean
import upperbounds as bounds

def writeresults(solutions, algorithm, cargolist_no, constraint):
    """
    Writes results to a csv file. A result is defined as a fleet with a parcel
    distribution. Writes the following attributes:
        - (CSV-specific) solution id
        - Algorithm type
        - Hill Climber
        - Simulated Annealing
        - Diplomatic constraint
        - Number of iterations
        - Cargolist
        - Number of packages
        - Total costs
        - Total costs (as % of upper bound)
        - Percentage mass filled
        - Percentage volume filled
        - Parcel distribution

    Takes one argument:
        inventory: Object of type inventory.
    """

    infile = "data/results.csv"
    inventory_type = type(classes.Inventory(None, None))
    id_counter = 0

    with open(infile, 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')

        # write header with column names
        writer.writerow("sol_id", "algo", "hc", "sa", "constr", "n_iter", "cargolist", "n_packages", "total_costs", "total_costs_p", "avg_mass_p", "avg_vol_p", "distr")

        # for every row in the solution
        for solution in solutions:

            # check if the solution is of type inventory
            if type(solution) == inventory_type:

                # save fleet in the solution
                fleet = solution.dict_space
                
                # hold variables to be written to csv
                sol_id = id_counter
                # ALGORITHM
                # CARGOLIST
                # NUMBER OF PACKAGES
                total_costs = solution.calculate_costs()
                total_costs_pct = total_costs / bounds.calc_upperbound()
                mass_filled_pct = mean([ship.current_weight for ship in fleet])
                volume_filled_pct = mean([ship.current_volume for ship in fleet])

                # write evey row in the csv
                writer.writerow(sol_id, total_costs, total_costs_pct,\
                                mass_filled_pct, volume_filled_pct)

                id_counter += 1







