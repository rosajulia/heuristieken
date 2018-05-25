from helperscripts import helpers

def visual(ships, best_solution):

    """
    Returns visualisation for best solution as calculated in main

    Take two arguments:

        ships: amount of ships
        best_solution: List of instances of Inventory class containing best solutions.
    """
    # visualize which ships contain which parcels in best solution(s)
    solution_statement = helpers.visualizeParcelsPerShip(best_solution)

    # create dict for visualisation
    d = {}
    for i in range(ships):
        current_weight = best_solution.dict_space[i].current_weight
        current_volume = best_solution.dict_space[i].current_volume

        max_weight = best_solution.dict_space[i].max_weight
        max_volume = best_solution.dict_space[i].max_volume

        weight = current_weight / max_weight * 100
        volume = current_volume / max_volume * 100

        weight_send = format(weight, '.2f')
        volume_send = format(volume, '.2f')

        # store results in dict
        d["weight" + str(i)] = weight_send
        d["volume" + str(i)] = volume_send
        d["total_amount" + str(i)] = len(solution_statement[i]["content"])
        d["parcels" + str(i)] = solution_statement[i]["content"]
    return d
