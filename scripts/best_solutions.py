from copy import copy, deepcopy
from visualisation import visual

def solutions(solutions):

    """
    Calculates best solution

    Take one argument:

        solutions: List of instances of Inventory class as result
        from on of the algorithms.
    """

    # create empty lists to store solution parameters
    costs_list = []
    parcel_amount_list = []


    # collect all parcel amounts in list and determine highest
    for solution in solutions:
        print(solution.parcel_amount)
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
    # print(len(costs_list), costs_list)
    min_costs = min(costs_list)
    # print("mcl", min_costs, type(min_costs))

    # save solution(s) with lowest cost
    best_solutions = []
    for solution in parcel_checked_solutions:
        if solution.total_costs is min_costs:
            best_solutions.append(deepcopy(solution))

    print("Maximum amount of parcels in ship: {}".format(max_parcel_amount))
    print("Corresponding costs: {}". format(min_costs))

    return best_solutions[0], max_parcel_amount, min_costs


