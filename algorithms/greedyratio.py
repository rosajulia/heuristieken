import random
from helperscripts import helpers, updateship, greedyhelper
from operator import itemgetter
from copy import copy, deepcopy

def greedy_ratio(inventory, repetitions, constraint):
    """Greedy algorithm based on the weight-to-volume ratio of spaceships and parcels,
    and the assumption that low ratio ships are suitable transport for low ratio parcels
    (and high ratio ships for high ratio parcels)."""

    # create list for final return of solutions
    solutions = []
    solution_id = 0

    dict_space = inventory.dict_space
    length_dict_space = len(dict_space)

    dict_parcel = inventory.dict_parcel
    length_dict_parcel = len(dict_parcel)

    # sort spaceship based on weight to volume ratio
    dict_space = sorted(dict_space, key=lambda x: x.calculateRatio())

    # sort parcel list based on weight to volume ratio
    sorted_parcel_dict = sorted(dict_parcel, key=lambda x: x.ratio)

    # determine ship types with lowest and highest ratio in current selection
    lowest_ratio_type = dict_space[0].type
    highest_ratio_type = dict_space[len(dict_space) - 1].type

    # determine highest parcel weight and volume in cargo list
    parcel_weight_max = inventory.maxParcelWeightVolume()[0]
    parcel_volume_max = inventory.maxParcelWeightVolume()[1]

    # determine amount of ships of lowest and highest ratio type
    low_type_counter = 0
    high_type_counter = 0
    for ship in dict_space:
        if ship.type is lowest_ratio_type:
            low_type_counter += 1
        elif ship.type is highest_ratio_type:
            high_type_counter += 1

    # create solution
    for _ in range(repetitions):

        # start weight and volume of ships at zero and set to not full
        dict_space = [helpers.reset(element) for element in dict_space]

        # set location of parcels to zero
        dict_parcel = [helpers.resetParcel(element) for element in sorted_parcel_dict]

        # fill low ratio ships
        low_filled = greedyhelper.fill_low_ratio_ships(lowest_ratio_type, low_type_counter, length_dict_parcel, dict_space, dict_parcel, parcel_weight_max, parcel_volume_max)
        dict_space = low_filled[0]
        dict_parcel = low_filled[1]
        parcel_amount = low_filled[2]

        # determine amount of distributed parcels with low ratios
        low_distributed_parcels = parcel_amount

        # check whether not only one type of ship in selection
        if low_type_counter != length_dict_space:

            # fill high ratio ships
            high_filled = greedyhelper.fill_high_ratio_ships(length_dict_space, length_dict_parcel, high_type_counter, parcel_amount, dict_space, dict_parcel, parcel_weight_max, parcel_volume_max, highest_ratio_type)
            dict_space = high_filled[0]
            dict_parcel = high_filled[1]
            parcel_amount = high_filled[2]

        # determine amount of distributed parcels with high ratios
        high_distributed_parcels = parcel_amount - low_distributed_parcels

        # check if not only two types of ships in selection
        if low_type_counter + high_type_counter != length_dict_space:

            # fill middle ratio ships
            middle_filled = greedyhelper.fill_middle_ratio_ships(dict_parcel, length_dict_parcel, low_distributed_parcels, high_distributed_parcels, length_dict_space, dict_space, parcel_amount, low_type_counter, high_type_counter, parcel_weight_max, parcel_volume_max, lowest_ratio_type, highest_ratio_type)
            dict_space = middle_filled[0]
            dict_parcel = middle_filled[1]
            parcel_amount = middle_filled[2]
            shuffled_parcel_indices = middle_filled[3]

        # squeeze in some extra parcels if possible
        add_extra_parcels = greedyhelper.squeeze_in_extra_parcels(shuffled_parcel_indices, dict_space, dict_parcel, parcel_amount)
        dict_space = add_extra_parcels[0]
        dict_parcel = add_extra_parcels[1]
        parcel_amount = add_extra_parcels[2]

        # update solution and add to solutions list for final return
        inventory.solution_id = solution_id
        inventory.parcel_amount = parcel_amount
        inventory.total_costs = inventory.calculate_costs(constraint)
        solutions.append(deepcopy(inventory))

        solution_id += 1

    return solutions
