import random
from random import shuffle
from scripts import helpers
from operator import itemgetter
from copy import copy, deepcopy

def greedy_ratio(inventory, repetitions):
    """Greedy algorithm based on the ratios of weight and volume per parcel, and suitable ships for those ratios."""
    
    # initialize values for greedy algorithm
    solutions = []

    dict_space = inventory.dict_space
    length_dict_space = len(dict_space)

    dict_parcel = inventory.dict_parcel
    length_dict_parcel = len(dict_parcel)

    # sort spaceship based on weight to volume ratio
    dict_space = sorted(dict_space, key=lambda x: x.calculateRatio())

    # determine ship types in current selection with lowest and highest ratio
    lowest_ratio_type = dict_space[0].type
    highest_ratio_type = dict_space[len(dict_space) - 1].type

    # determine highest parcel weight and volume in cargo list
    parcel_weight_max = inventory.maxParcelWeightVolume()[0]
    parcel_volume_max = inventory.maxParcelWeightVolume()[1]

    # sort parcel list on weight to volume ratio
    sorted_parcel_dict = sorted(dict_parcel, key=lambda x: x.ratio)

    for _ in range(repetitions):

        parcel_amount = 0
        low_type_counter = 0
        high_type_counter = 0
        full_ships_counter = 0

        # start weight and volume of ships at zero and set to not full
        dict_space = [helpers.reset(element) for element in dict_space]

        # set location of parcels to zero
        dict_parcel = [helpers.resetParcel(element) for element in sorted_parcel_dict]

        # keep track of which parcels have been distributed already
        parcel_cursor = 0

        # determine how many ships of lowest- and highest ratio type
        for ship in dict_space:
            if ship.type is lowest_ratio_type:
                low_type_counter += 1
            elif ship.type is highest_ratio_type:
                high_type_counter += 1

        # fill lowest ratio ships until all are full
        while full_ships_counter != low_type_counter and parcel_amount != length_dict_parcel:

            for i in range(low_type_counter):

                if dict_space[i].full is False:
                    dict_parcel[parcel_cursor].location = dict_space[i].id
                    dict_space[i].current_weight += dict_parcel[parcel_cursor].weight
                    dict_space[i].current_volume += dict_parcel[parcel_cursor].volume
                    parcel_amount +=1

                    if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
                                dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
                        dict_space[i].full = True

                    parcel_cursor += 1

                for ship in dict_space:
                    if ship.type is lowest_ratio_type and ship.full is True:
                        full_ships_counter += 1

        # how many parcels from start of sorted list were distributed
        low_distributed_parcels = parcel_amount
        parcel_cursor = length_dict_parcel - 1

        # check whether not only one type of ship
        if low_type_counter != length_dict_space:

            full_ships_counter = 0

            # fill highest ratio ships until all are full
            while full_ships_counter != high_type_counter and parcel_amount != length_dict_parcel:

                for i in range(length_dict_space - high_type_counter, length_dict_space):
                    if dict_space[i].full is False:
                        dict_parcel[parcel_cursor].location = dict_space[i].id
                        dict_space[i].current_weight += dict_parcel[parcel_cursor].weight
                        dict_space[i].current_volume += dict_parcel[parcel_cursor].volume
                        parcel_amount += 1

                        if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
                                    dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
                            dict_space[i].full = True

                        parcel_cursor -= 1

                    for ship in dict_space:
                        if ship.type is highest_ratio_type and ship.full is True:
                            full_ships_counter += 1

        # how many parcels from end of sorted list were distributed
        high_distributed_parcels = parcel_amount - low_distributed_parcels

        # check if not only two types of ships were used
        if low_type_counter + high_type_counter != length_dict_space:

            full_ships_counter = 0

            number_of_remaining_ships = length_dict_space - low_type_counter - high_type_counter

            # collect all id's of remaining parcels
            remaining_parcel_indices = []
            for parcel in dict_parcel:
                index_to_save = dict_parcel.index(parcel)
                if index_to_save >= low_distributed_parcels and index_to_save < length_dict_parcel - high_distributed_parcels:
                    remaining_parcel_indices.append(index_to_save)

            # convert to randomly ordered list of remaining id's
            shuffle(remaining_parcel_indices)
            shuffled_parcel_indices = remaining_parcel_indices
            parcel_cursor = 0

            # fill remaining ships until all are full
            while full_ships_counter != number_of_remaining_ships and parcel_amount != length_dict_parcel:

                for i in range(low_type_counter, low_type_counter + number_of_remaining_ships):
                    if dict_space[i].full is False:

                        # pick (random) remaining id
                        if parcel_cursor >= len(shuffled_parcel_indices):
                            break
                        else:
                            parcel_index_to_add = shuffled_parcel_indices[parcel_cursor]

                        # find corresponding parcel and add it to ship
                        for parcel in dict_parcel:
                            if dict_parcel.index(parcel) is parcel_index_to_add:
                                dict_parcel[parcel_index_to_add].location = dict_space[i].id
                                dict_space[i].current_weight += dict_parcel[parcel_index_to_add].weight
                                dict_space[i].current_volume += dict_parcel[parcel_index_to_add].volume
                                parcel_amount += 1
                                parcel_cursor += 1

                        if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
                                    dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
                            dict_space[i].full = True

                    for ship in dict_space:
                        if ship.type != lowest_ratio_type and ship.type != highest_ratio_type and ship.full is True:
                            full_ships_counter += 1

        full_ships_counter = 0
        shuffled_parcel_indices = shuffled_parcel_indices[parcel_cursor:]
        parcel_cursor = 0

        for _ in range(len(shuffled_parcel_indices)):
            for ship in dict_space:
                if parcel_cursor >= len(shuffled_parcel_indices):
                    break
                else:
                    index  = shuffled_parcel_indices[parcel_cursor]
                if (ship.current_weight + dict_parcel[index].weight <= ship.max_weight and \
                        ship.current_volume + dict_parcel[index].volume <= ship.max_volume):

                    ship.current_weight += dict_parcel[index].weight
                    ship.current_volume += dict_parcel[index].volume

                    dict_parcel[index].location = ship.id
                    parcel_cursor += 1
                    parcel_amount += 1

        inventory.parcel_amount = parcel_amount
        inventory.total_costs = inventory.calculate_costs()
        solutions.append(deepcopy(inventory))

    return solutions