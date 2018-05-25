from scripts import helpers

def visual(ships, best_solution):

    """
    Returns visualisation for best solution as calculated in main

    Take one argument:

        solutions: List of instances of Inventory class containing best solutions.
    """
    # visualize which ships contain which parcels in best solution(s)
    solution_statement = helpers.visualizeParcelsPerShip(best_solution)
    # for element in solution_statement:
    #     print(element)

    # create dict for progress bars
    if ships == "no":
        d = {}
        for i in range(4):
            current_weight = best_solution.dict_space[i].current_weight
            current_volume = best_solution.dict_space[i].current_volume

            max_weight = best_solution.dict_space[i].max_weight
            max_volume = best_solution.dict_space[i].max_volume

            weight = current_weight / max_weight * 100
            volume = current_volume / max_volume * 100

            weight_send = format(weight, '.2f')
            volume_send = format(volume, '.2f')

            d["weight" + str(i)] = weight_send
            d["volume" + str(i)] = volume_send
            d["total_amount" + str(i)] = len(solution_statement[i]["content"])
            d["parcels" + str(i)] = solution_statement[i]["content"]
            # d["total_parcels"] = best_solution[1]
            # d["total_costs"] = best_solution[2]

        return d
    else:
        return
