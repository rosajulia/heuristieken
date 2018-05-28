from copy import copy, deepcopy
from visualisation import visual, graph

def solutions(solutions):

    """
    Calculates best solution

    Take one argument:

        solutions: a list containing all solutions as Inventory
        class provided by the algorithm which was run. An exception on the rule
        is when the hillclimber is run, then solutions will only show the improved
        solutions when compared to the solutions ran with the normal algorithms. 
    
    Output:
        A tuple containing the best solution as Inventory
        class, the maximum parcel amount, and the minimum costs.
        
    """
    # create empty lists to store solution parameters
    costs_list = []
    parcel_amount_list = []
    costs_graph_list = []

    # collect all parcel amounts in list and determine highest
    for solution in solutions:
        parcel_amount_list.append(solution.parcel_amount)
        costs_graph_list.append(solution.total_costs)
    max_parcel_amount = max(parcel_amount_list)

    print(parcel_amount_list)

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
    
    # send lists to graph
    graph.linegraph(costs_graph_list, parcel_amount_list)

    print("Maximum amount of parcels in ship: {}".format(max_parcel_amount))
    print("Corresponding costs: {}". format(min_costs))

    return best_solutions[0], max_parcel_amount, min_costs
