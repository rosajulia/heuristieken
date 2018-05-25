from helperscripts import updateship
from random import shuffle

def fill_low_ratio_ships(lowest_ratio_type, low_type_counter, length_dict_parcel, dict_space, dict_parcel, parcel_weight_max, parcel_volume_max):
    """Fills ships of the lowest ratio type in the current selection with parcels with the lowest ratios in the cargolist"""

    full_ships_counter = 0
    parcel_amount = 0

    # keep track of which parcels have been distributed already
    parcel_cursor = 0

    # fill lowest ratio ships until all are full or all parcels distributed
    while full_ships_counter != low_type_counter and parcel_amount != length_dict_parcel:

        # loop over ships with low ratio type
        for i in range(low_type_counter):

            # add parcel to ship if it fits
            if dict_space[i].full is False:
                dict_parcel[parcel_cursor].location = dict_space[i].id
                dict_space[i] = updateship.update_ship(dict_space[i], dict_parcel[parcel_cursor], "+")
                parcel_amount +=1

                # check if ship is almost full
                if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
                            dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
                    dict_space[i].full = True

                parcel_cursor += 1

            full_ships_counter = 0
            for ship in dict_space:
                if ship.type is lowest_ratio_type and ship.full is True:
                    full_ships_counter += 1

    return [dict_space, dict_parcel, parcel_amount]


def fill_high_ratio_ships(length_dict_space, length_dict_parcel, high_type_counter, parcel_amount, dict_space, dict_parcel, parcel_weight_max, parcel_volume_max, highest_ratio_type):
    """Fills ships of the highest ratio type in the current selection with parcels with the highest ratios in the cargolist"""

    full_ships_counter = 0
    parcel_cursor = length_dict_parcel - 1

    # fill highest ratio ships until all are full or all parcels are distributed
    while full_ships_counter != high_type_counter and parcel_amount != length_dict_parcel:

        # loop over high ratio ships
        for i in range(length_dict_space - high_type_counter, length_dict_space):

            # add parcel to ship if it fits
            if dict_space[i].full is False:
                dict_parcel[parcel_cursor].location = dict_space[i].id
                dict_space[i] = updateship.update_ship(dict_space[i], dict_parcel[parcel_cursor], "+")
                parcel_amount += 1

                # check if ship is almost full
                if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
                            dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
                    dict_space[i].full = True

                parcel_cursor -= 1

            full_ships_counter = 0
            for ship in dict_space:
                if ship.type is highest_ratio_type and ship.full is True:
                    full_ships_counter += 1

    return [dict_space, dict_parcel, parcel_amount]


def fill_middle_ratio_ships(dict_parcel, length_dict_parcel, low_distributed_parcels, high_distributed_parcels, length_dict_space, dict_space, parcel_amount, low_type_counter, high_type_counter, parcel_weight_max, parcel_volume_max, lowest_ratio_type, highest_ratio_type):
    """Fills ships with middle ratio types in the current selection with parcels with the middle ratios in the cargolist"""

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
    full_ships_counter = 0

    # fill remaining ships until all are full or parcels are all distributed
    while full_ships_counter != number_of_remaining_ships and parcel_amount != length_dict_parcel:

        # loop over remaining ships
        for i in range(low_type_counter, low_type_counter + number_of_remaining_ships):
            if dict_space[i].full is False:

                # pick (random) remaining parcel id
                if parcel_cursor >= len(shuffled_parcel_indices):
                    break
                else:
                    parcel_index_to_add = shuffled_parcel_indices[parcel_cursor]

                # find corresponding parcel and add it to ship
                for parcel in dict_parcel:
                    if dict_parcel.index(parcel) == parcel_index_to_add:
                        dict_parcel[parcel_index_to_add].location = dict_space[i].id
                        dict_space[i] = updateship.update_ship(dict_space[i], dict_parcel[parcel_index_to_add], "+")
                        parcel_amount += 1
                        parcel_cursor += 1

                # check if ship is almost full
                if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
                            dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
                    dict_space[i].full = True

            full_ships_counter = 0
            for ship in dict_space:
                if ship.type != lowest_ratio_type and ship.type != highest_ratio_type and ship.full is True:
                    full_ships_counter += 1

    # determine still remaining parcels
    shuffled_parcel_indices = shuffled_parcel_indices[parcel_cursor:]

    return [dict_space, dict_parcel, parcel_amount, shuffled_parcel_indices]


def squeeze_in_extra_parcels(shuffled_parcel_indices, dict_space, dict_parcel, parcel_amount):
    """Adds not yet distributed parcels to the ships in the inventory where possible"""

    parcel_cursor = 0

    # loop over remaining parcels
    for _ in range(len(shuffled_parcel_indices)):

        # add to ship where possible
        for ship in dict_space:
            if parcel_cursor >= len(shuffled_parcel_indices):
                break
            else:
                index  = shuffled_parcel_indices[parcel_cursor]
            if (ship.current_weight + dict_parcel[index].weight <= ship.max_weight and \
                    ship.current_volume + dict_parcel[index].volume <= ship.max_volume):

                ship = updateship.update_ship(ship, dict_parcel[index], "+")

                dict_parcel[index].location = ship.id
                parcel_cursor += 1
                parcel_amount += 1

    return [dict_space, dict_parcel, parcel_amount]
