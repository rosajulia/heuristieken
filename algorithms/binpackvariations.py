import operator
from helperscripts import updateship as us
from helperscripts import helpers

def binpack(inventory, packing_variation, repetitions):
    """
    Algorithm for bin packing variations that adds an additional heuristic
    for packing the ships.

    Returns list of inventory objects.

    Takes three arguments:

        inventory: Must contain an inventory object that contains a list
        with ship objects and a list with parcel objects that need to be
        packed.

        packing-variation: Specify heuristic to apply in the process of
        packing ships

            "first" - First-fit decreasing:
            Finds the first available ship in which the parcel can be placed.
            Parcels are sorted by volume (descending).

            "best" - Best-fit decreasing:
            Finds the ship in which the parcel can be placed and that has the
            least volume left after placing the parcel.
            Parcels are sorted by volume (descending).

            "worst" - Worst-fit decreasing:
            Finds the ship in which the parcel can be placed and that has
            the most volume left after placing the parcel.
            Parcels are sorted by volume (descending).

        constraint: Specify whether to apply the diplomatic constraint in
        generating a dict_space to carry the parcels. Takes boolean.

            True: Applies diplomatic constraint when generating dict_space where
            the difference in the number of ship each nation sends cannot be
            larger than 1.

            False: No constraints; dict_spaces will be generated at random.

        repetitions: Specify the number of times the algorithm will run. Takes
        nonnegative integer values.
    """

    # # check for correct user input
    # if type(constraint) != bool:
    #     raise TypeError("Expected boolean for arg constraint")

    solutions = []
    parcel_amount = 0

    for _ in range(repetitions):

        dict_space = inventory.dict_space
        dict_parcel = inventory.dict_parcel

        dict_space = [helpers.reset(element) for element in dict_space]
        dict_parcel = [helpers.resetParcel(element) for element in dict_parcel]

        # script for first-fit variation
        if packing_variation.lower() == "first":

            # store parcel attributes
            dict_parcel = sorted(dict_parcel, key=operator.attrgetter("volume"), reverse=True)

            # loop over every parcel in the cargolist
            for parcel in dict_parcel:

                # for every ship
                for ship in dict_space:

                    # try to fit the parcel in the first available ship
                    if ship.current_volume + parcel.volume <= ship.max_volume:
                        if ship.current_weight + parcel.weight <= ship.max_weight:

                            # update the parcel and ship attribures
                            parcel.location = ship.id
                            ship = us.update_ship(ship, parcel, "+")
                            parcel_amount += 1

            inventory.parcel_amount = parcel_amount
            inventory.total_costs = inventory.calculate_costs()
            solutions.append(inventory)

            return solutions

        # script for best-fit
        elif packing_variation.lower() == "best":

            # store parcel attributes and sort descending by volume
            dict_parcel = sorted(dict_parcel, key=operator.attrgetter("volume"), reverse=True)

            # loop over every parcel in the parcel dict
            for parcel in dict_parcel:

                # keep track of the LOWEST percentage of weight left
                best_fit_index = 0
                best_fit = 1

                # fit parcel in the ship with the lowest percentage of weight left
                for i in range(len(dict_space)):

                    # if the parcel fits in the ship
                    if dict_space[i].current_volume + parcel.volume <= dict_space[i].max_volume:
                        if dict_space[i].current_weight + parcel.weight <= dict_space[i].max_weight:

                            # calc the weight left as percentage of maximum
                            weight_left = dict_space[i].max_volume - (dict_space[i].current_volume + parcel.volume) / dict_space[i].max_volume

                            # check if that ship is a better fit
                            if weight_left < best_fit:

                                # store the best fit
                                best_fit = weight_left
                                best_fit_index = i

                # update the parcel and ship attributes
                parcel.location = dict_space[best_fit_index].id
                dict_space[best_fit_index] = us.update_ship(dict_space[best_fit_index], parcel, "+")
                parcel_amount += 1

            inventory.parcel_amount = parcel_amount
            inventory.total_costs = inventory.calculate_costs()
            solutions.append(inventory)

            return solutions

        # script for best-fit
        elif packing_variation.lower() == "worst":

            # store parcel attributes and sort descending by volume
            dict_parcel = sorted(dict_parcel, key=operator.attrgetter("volume"), reverse=True)

            # loop over every parcel in the parcel dict
            for parcel in dict_parcel:

                # keep track of the HIGHEST percentage of weight left
                worst_fit_index = 0
                worst_fit = 0

                # fit parcel in the ship with the highest percentage of weight left
                for i in range(len(dict_space)):

                    # if the parcel fits in the ship
                    if dict_space[i].current_volume + parcel.volume <= dict_space[i].max_volume:

                        if dict_space[i].current_weight + parcel.weight <= dict_space[i].max_weight:

                            # calc the weight left as percentage of maximum
                            weight_left = dict_space[i].max_volume - (dict_space[i].current_volume + parcel.volume) / dict_space[i].max_volume

                            # check if that ship is a worse fit
                            if weight_left > worst_fit:

                                # store the worst fit
                                worst_fit = weight_left
                                worst_fit_index = i

                # update the parcel and ship attributes
                parcel.location = dict_space[worst_fit_index].id
                dict_space[worst_fit_index] = us.update_ship(dict_space[worst_fit_index], parcel, "+")
                parcel_amount += 1

            inventory.parcel_amount = parcel_amount
            inventory.total_costs = inventory.calculate_costs()
            solutions.append(inventory)

            return solutions

        else:
            # error handler for incorrect argument packing_variation
            raise TypeError("Enter 'first', 'best' or 'worst' for command line arg packing_variation.")
