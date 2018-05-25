import random
from scripts import helpers, updateship
import time
from copy import copy, deepcopy

# create random solutions
def random_algorithm(inventory, repetitions):
    """Randomly fills spaceships with a cargo list.
    The first argument holds an object representing the format of a possible
    distribution of parcels over spaceships. The second argument indicates how
    often the algorithm should generate a solution.

    Usage:
    randomalgorithm.random_algorithm(inventory, repetitions)
    """

    solutions = []
    solution_id = 0
    for _ in range(repetitions):

        dict_parcel = inventory.dict_parcel
        dict_space = inventory.dict_space
        amount_of_ships = len(dict_space)
        amount_of_parcels = len(dict_parcel)
        parcel_weight_max = inventory.maxParcelWeightVolume()[0]
        parcel_volume_max = inventory.maxParcelWeightVolume()[1]

        inventory.solution_id = solution_id

        # which of the ships is currently being filled
        ship_counter = 1

        # keep track of amount of parcels per solution
        parcel_amount = 0

        # make shuffled list
        shuffled_list = random.sample(range(len(dict_parcel)), k=len(dict_parcel))

        # start weight and volume of ships at zero and set to not full
        dict_space = [helpers.reset(element) for element in dict_space]

        # set location of parcels to zero
        dict_parcel = [helpers.resetParcel(element) for element in dict_parcel]

        # add parcel until limits are reached (until all ships are full)
        full_ships_counter = 0
        while full_ships_counter != amount_of_ships and parcel_amount != amount_of_parcels:

            # only continue filling with ships that are not full
            while dict_space[ship_counter - 1].full is True:
                if ship_counter is amount_of_ships:
                    ship_counter = 1
                else:
                    ship_counter += 1

            if len(shuffled_list) < 1:
                break
            else:
                # pick random parcel
                add_ID = shuffled_list.pop()

            # add parcel to ship
            dict_parcel[add_ID - 1].location = dict_space[ship_counter - 1].id

            # update spaceships current weight and volume
            dict_space[ship_counter - 1] = updateship.update_ship(dict_space[ship_counter - 1], dict_parcel[add_ID - 1], "+")

            # count parcels per solution
            parcel_amount += 1

            # note when ship is almost full
            if (dict_space[ship_counter - 1].current_weight >= dict_space[ship_counter - 1].max_weight - parcel_weight_max or
                        dict_space[ship_counter - 1].current_volume >= dict_space[ship_counter - 1].max_volume - parcel_volume_max):

                # try to squeeze another parcel in
                for parcel_id in shuffled_list:

                    if (dict_space[ship_counter - 1].current_weight + dict_parcel[parcel_id - 1].weight <= dict_space[ship_counter - 1].max_weight and \
                        dict_space[ship_counter - 1].current_volume + dict_parcel[parcel_id - 1].volume <= dict_space[ship_counter - 1].max_volume):

                        dict_space[ship_counter - 1] = updateship.update_ship(dict_space[ship_counter - 1], dict_parcel[parcel_id - 1], "+")

                        shuffled_list.remove(parcel_id)

                        dict_parcel[parcel_id - 1].location = dict_space[ship_counter - 1].id

                        parcel_amount += 1

                # set ship to full
                dict_space[ship_counter - 1].full = True

            # keep track of how many ships are full
            full_ships_counter = 0
            for ship in dict_space:
                if ship.full is True:
                    full_ships_counter += 1

        # give unique solution_id
        solution_id += 1

        # add parcel amount and total costs to solution (inventory object)
        inventory.parcel_amount = parcel_amount
        inventory.total_costs = inventory.calculate_costs()

        # collect all solutions in list for returning
        solutions.append(deepcopy(inventory))


    return solutions
