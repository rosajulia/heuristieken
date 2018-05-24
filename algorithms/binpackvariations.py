import operator
from scripts import generateships as gs
from scripts import updateship as us

def binpack(inventory, packing_variation, constraint):
    """
    Algorithm for bin packing variations that adds an additional heuristic
    for packing the ships.

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
            Finds the ship in which the parcel can be placed and that has
            the least volume left after placing the parcel.
            Parcels are sorted by volume (descending).
            
            "worst" - Worst-fit decreasing:
            Finds the ship in which the parcel can be placed and that has
            the most volume left after placing the parcel.
            Parcels are sorted by volume (descending).

        constraint: Specify whether to apply the diplomatic constraint in 
        generating a fleet to carry the parcels. Takes boolean.

            True: Applies diplomatic constraint when generating fleet where the 
            difference in the number of ship each nation sends cannot be larger 
            than 1.

            False: No constraints; fleets will be generated at random.
    """
    
    # check for correct user input
    if type(constraint) != bool:
        raise TypeError("Expected boolean for arg contraint")

    dict_space = inventory.dict_space
    dict_parcel = inventory.dict_parcel

    # script for first-fit variation
    if packing_variation.lower() == "first":

        # store parcel attributes
        dict_parcel = sorted(dict_parcel, key=operator.attrgetter("volume"), 
            reverse=True)

        # generate a list of ship objects that fits cargolsit
        fleet = gs.generateships(dict_space, dict_parcel, constraint)

        # loop over every parcel in the cargolist
        for parcel in dict_parcel:

            # for every ship
            for ship in fleet:

                # try to fit the parcel in the first available ship
                if ship.current_volume + parcel.volume <= ship.max_volume:
                    if ship.current_weight + parcel.weight <= ship.max_weight:

                        # update the parcel and ship attribures
                        parcel.location = ship.id
                        ship = us.updateship(ship, parcel)

    # script for best-fit
    elif packing_variation.lower() == "best":

        # store parcel attributes and sort descending by volume
        dict_parcel = sorted(dict_parcel, key=operator.attrgetter("volume"), 
            reverse=True)

        # generate a list of ship objects that fits cargolsit
        fleet = gs.generateships(dict_space, dict_parcel, constraint)

        # loop over every parcel in the parcel dict
        for parcel in dict_parcel:

            # keep track of the LOWEST percentage of weight left
            best_fit_index = 0
            best_fit = 1

            # fit parcel in the ship with the lowest percentage of weight left
            for i in range(len(fleet)):

                # if the parcel fits in the ship
                if fleet[i].current_volume + parcel.volume <= \
                    fleet[i].max_volume:

                    if fleet[i].current_weight + parcel.weight <= \
                        fleet[i].max_weight:

                        # calc the weight left as percentage of maximum
                        weight_left = fleet[i].max_volume - \
                        (fleet[i].current_volume + parcel.volume) / \
                            fleet[i].max_volume

                        # check if that ship is a better fit
                        if weight_left < best_fit:

                            # store the best fit
                            best_fit = weight_left
                            best_fit_index = i

            # update the parcel and ship attributes
            parcel.location = fleet[best_fit_index].id
            fleet[best_fit_index] = us.updateship(fleet[best_fit_index], parcel)

    # script for best-fit
    elif packing_variation.lower() == "worst":

        # store parcel attributes and sort descending by volume
        dict_parcel = sorted(dict_parcel, key=operator.attrgetter("volume"), \
            reverse=True)

        # generate a list of ship objects that fits cargolsit
        fleet = gs.generateships(dict_space, dict_parcel, constraint)

        # loop over every parcel in the parcel dict
        for parcel in dict_parcel:

            # keep track of the HIGHEST percentage of weight left
            worst_fit_index = 0
            worst_fit = 0

            # fit parcel in the ship with the highest percentage of weight left
            for i in range(len(fleet)):

                # if the parcel fits in the ship
                if fleet[i].current_volume + parcel.volume <= \
                    fleet[i].max_volume:

                    if fleet[i].current_weight + parcel.weight <= \
                        fleet[i].max_weight:

                        # calc the weight left as percentage of maximum
                        weight_left = fleet[i].max_volume - \
                            (fleet[i].current_volume + parcel.volume) / \
                            fleet[i].max_volume

                        # check if that ship is a worse fit
                        if weight_left > worst_fit:

                            # store the worst fit
                            worst_fit = weight_left
                            worst_fit_index = i

            # update the parcel and ship attributes
            parcel.location = fleet[worst_fit_index].id
            fleet[worst_fit_index] = us.updateship(fleet[worst_fit_index], \
                parcel)
    
    else:

        # error handler for incorrect argument packing_variation
        raise TypeError("Enter 'first', 'best' or 'worst' for command line arg \
                         packing_variation.")
