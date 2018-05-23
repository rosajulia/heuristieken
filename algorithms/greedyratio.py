import random
from random import shuffle
from scripts import helpers
from operator import itemgetter
from copy import copy, deepcopy

def greedy_ratio(inventory, repetitions):
    """Greedy algorithm based on the ratios of weight and volume per parcel, and suitable ships for those ratios."""


    print("ik run nu greedy")
    # print(inventory.dict_space[0].id)

    # id_list = []
    # for parcel in inventory.dict_parcel:
    #     id_list.append(parcel.id)
    # print(inventory.dict_parcel[0].id)
    # print(id_list)
    # pakjes sorteren
    # schepen sorteren
    solutions = []

    dict_space = inventory.dict_space
    length_dict_space = len(dict_space)

    dict_parcel = inventory.dict_parcel
    length_dict_parcel = len(dict_parcel)
    # print(dict_space)

    # sort spaceship based on weight to volume ratio
    dict_space = sorted(dict_space, key=lambda x: x.calculateRatio())
    # print(dict_space)

    # determine ship types in current selection with lowest and highest ratio
    lowest_ratio_type = dict_space[0].type
    highest_ratio_type = dict_space[len(dict_space) - 1].type

    # determine highest parcel weight and volume in cargo list
    parcel_weight_max = inventory.maxParcelWeightVolume()[0]
    parcel_volume_max = inventory.maxParcelWeightVolume()[1]

    # id_list = []
    # for parcel in dict_parcel:
    #     id_list.append(parcel.id)
    # print(id_list)

    # sort parcel list on weight to volume ratio
    sorted_parcel_dict = sorted(dict_parcel, key=lambda x: x.ratio)
    # for parcel in sorted_parcel_array:
    #     id_list.append(parcel.id)
    # print(id_list)

    # id_list = []
    # for parcel in sorted_parcel_dict:
    #     id_list.append(parcel.id)
    # print(inventory.dict_parcel[0].id)
    # print(id_list)


    for _ in range(repetitions):

        parcel_amount = 0
        low_type_counter = 0
        high_type_counter = 0
        full_ships_counter = 0

        # start weight and volume of ships at zero and set to not full
        dict_space = [helpers.reset(element) for element in dict_space]

        # set location of parcels to zero
        dict_parcel = [helpers.resetParcel(element) for element in sorted_parcel_dict]

        # print(dict_space)

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
                # run with dict_space, i, dict_parcel, parcel_cursor, parcel_amount?
                # and return all of those again?

                if dict_space[i].full is False:
                    dict_parcel[parcel_cursor].location = dict_space[i].id
                    # print(dict_space[i].id)
                    dict_space[i].current_weight += dict_parcel[parcel_cursor].weight
                    dict_space[i].current_volume += dict_parcel[parcel_cursor].volume
                    parcel_amount +=1
                    # print("pa1", parcel_amount)
                    # print(dict_parcel[parcel_cursor].id)

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
                        # print("pa2", parcel_amount)
                        # print(dict_parcel[parcel_cursor].id)

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
                    # print(index_to_save, parcel.id)
                    remaining_parcel_indices.append(index_to_save)

            # convert to randomly ordered list of remaining id's
            # print(remaining_parcel_indices)
            shuffle(remaining_parcel_indices)
            # print(remaining_parcel_indices)
            shuffled_parcel_indices = remaining_parcel_indices
            # print(shuffled_parcel_indices)
            parcel_cursor = 0

            # fill remaining ships until all are full
            while full_ships_counter != number_of_remaining_ships and parcel_amount != length_dict_parcel:

                for i in range(low_type_counter, low_type_counter + number_of_remaining_ships):
                    if dict_space[i].full is False:

                        # pick (random) remaining id
                        if parcel_cursor >= len(shuffled_parcel_indices):
                            break
                        else:
                            # print(parcel_cursor, shuffled_parcel_indices[parcel_cursor], parcel_amount)
                            parcel_index_to_add = shuffled_parcel_indices[parcel_cursor]

                        # find corresponding parcel and add it to ship
                        for parcel in dict_parcel:
                            if dict_parcel.index(parcel) is parcel_index_to_add:
                                dict_parcel[parcel_index_to_add].location = dict_space[i].id
                                dict_space[i].current_weight += dict_parcel[parcel_index_to_add].weight
                                dict_space[i].current_volume += dict_parcel[parcel_index_to_add].volume
                                parcel_amount += 1
                                # print("pa3", parcel_amount)
                                # print(dict_parcel[parcel_index_to_add].id, dict_space[i].id)
                                parcel_cursor += 1

                        if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
                                    dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
                            dict_space[i].full = True



                    for ship in dict_space:
                        if ship.type != lowest_ratio_type and ship.type != highest_ratio_type and ship.full is True:
                            full_ships_counter += 1


        full_ships_counter = 0
        shuffled_parcel_indices = shuffled_parcel_indices[parcel_cursor:]
        # print("lspi", len(shuffled_parcel_indices))
        parcel_cursor = 0

        for _ in range(len(shuffled_parcel_indices)):
            for ship in dict_space:
                index  = shuffled_parcel_indices[parcel_cursor]
                if (ship.current_weight + dict_parcel[index].weight <= ship.max_weight and \
                        ship.current_volume + dict_parcel[index].volume <= ship.max_volume):

                    ship.current_weight += dict_parcel[index].weight
                    ship.current_volume += dict_parcel[index].volume

                    dict_parcel[index].location = ship.id
                    parcel_cursor += 1
                    parcel_amount += 1
                    # print("pa4", parcel_amount)
                    # print(parcel_cursor, dict_parcel[index].id, ship.id)

                else:
                    continue

        inventory.parcel_amount = parcel_amount
        inventory.total_costs = inventory.calculate_costs()
        solutions.append(deepcopy(inventory))

    return solutions



                    # while dict_space[0].full is False:
                    #     element_id = order_array[order_place]
                    #
                    #     dict_parcel[element_id].location = dict_space[0].id
                    #     dict_space[0].current_weight += dict_parcel[element_id].weight
                    #     dict_space[0].current_volume += dict_parcel[element_id].volume
                    #
                    #
                    #     if (dict_space[0].current_weight >= dict_space[0].max_weight - parcel_weight_max or
                    #                 dict_space[0].current_volume >= dict_space[0].max_volume - parcel_volume_max):
                    #         dict_space[0].full = True
                    #
                    #     order_array = order_array[order_place + 1:]
                    #
                    #     parcel_amount += 1

                    # # fill spaceship 4 ratio-based
                    # while dict_space[3].full is False:
                    #     order_place = len(order_array) -1
                    #     element_id = order_array[order_place]
                    #
                    #     dict_parcel[element_id].location = dict_space[3].id
                    #     dict_space[3].current_weight += dict_parcel[element_id].weight
                    #     dict_space[3].current_volume += dict_parcel[element_id].volume
                    #
                    #     if (dict_space[3].current_weight >= dict_space[3].max_weight - parcel_weight_max or
                    #                 dict_space[3].current_volume >= dict_space[3].max_volume - parcel_volume_max):
                    #         dict_space[3].full = True
                    #
                    #     order_array = order_array[:order_place]
                    #     parcel_amount += 1

                            # # divide remaining cargo
                            # length_other_parcels = len(order_array)
                            #
                            # # make shuffled list
                            # shuffled_list = random.sample(range(length_other_parcels), k=length_other_parcels)
                            #
                            # # random divide cargo between spacechips 2 and 3
                            # while dict_space[1].full is False or dict_space[2].full is False:
                            #     for i in range(1,3):
                            #         if dict_space[i].full is True and i is 1:
                            #             i += 1
                            #         if dict_space[i].full is True and i is 2:
                            #             i -= 1
                            #
                            #         parcel_to_add = order_array[shuffled_list[0]]
                            #         dict_parcel[parcel_to_add].location = dict_space[i].id
                            #         dict_space[i].current_weight += dict_parcel[parcel_to_add].weight
                            #         dict_space[i].current_volume += dict_parcel[parcel_to_add].volume
                            #
                            #         shuffled_list = shuffled_list[1:]
                            #
                            #         if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
                            #                     dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
                            #             dict_space[i].full = True
                            #         parcel_amount += 1
        #
        #
        # # add last cargo to ships
        # # shuffled_length = len(shuffled_list)
        # for i in range(3):
        #     for ship in dict_space:
        #         for parcel in shuffled_list:
        #             # print(shuffled_list)
        #             if (ship.current_weight + dict_parcel[parcel].weight <= ship.max_weight and \
        #                     ship.current_volume + dict_parcel[parcel].volume <= ship.max_volume):
        #
        #                 ship.current_weight += dict_parcel[parcel].weight
        #                 ship.current_volume += dict_parcel[parcel].volume
        #
        #                 shuffled_list.remove(parcel)
        #
        #                 dict_parcel[parcel + 1].location = ship.id
        #
        #                 parcel_amount += 1
