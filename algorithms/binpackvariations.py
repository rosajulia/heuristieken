import operator
from scripts import generateships, shiploader

def binpack(inventory, packing_variation, constraint):
    """
    Algorithm for bin packing variations that adds an additional heuristic
    for packing the ships.

    Takes three command-line arguments:

        inventory: Must contain an inventory object that contains an array with ship objects and an array with parcel objects that need to      be packed.
        
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

        constraint: Specify whether to apply the diplomatic constraint in generating a fleet to carry the parcels. Takes boolean.

            True: Applies diplomatic constraint when generating fleet where the difference in the number of ship each nation sends cannot be larger than 1.

            False: No constraints; fleets will be generated at random.
    """
    
    # check for correct user input
    if constraint != type(True):
        raise TypeError("Expected boolean for arg contraint")

    # script for first-fit variation
    if packing_variation.lower() == "first":

        # store parcel attributes
        dict_parcel = sorted(inventory.dict_parcel, key=operator.attrgetter("volume"), reverse=True)

        # generate a list of ship objects that fits cargolsit
        fleet = generateships(ships, dict_parcel, constraint)

        # loop over every parcel in the cargolist
        for parcel in dict_parcel:

            # for every ship
            for ship in fleet:

                # try to fit the parcel in the first available ship
                if ship.current_volume + parcel.volume <= ship.max_volume:

                    # update the parcel and ship attribures
                    parcel.location = ship.id
                    ship = updateship(ship, parcel)

    # script for best-fit
    elif packing_variation.lower() == "best":

        # store parcel attributes and sort descending by volume
        dict_parcel = sorted(inventory.dict_parcel, key=operator.attrgetter("volume"), reverse=True)

        # generate a list of ship objects that fits cargolsit
        fleet = generateships(ships, dict_parcel, constraint)

        # loop over every parcel in the parcel dict
        for parcel in dict_parcel:

            # keep track of the LOWEST percentage of weight left
            lowest_ship_index = 0
            best_fit = 1

            # fit the parcel in the ship with the lowest percentage of weight left
            for i in range(len(fleet)):

                # calc the weight left as percentage of maximum
                weight_left = fleet[i].max_volume - (fleet[i].current_volume + parcel.volume) / ship.max_volume

                # find the best fit ship and store its index
                if weight_left < best_fit:
                    best_fit = weight_left
                    lowest_ship_index = i

            parcel.location = fleet[lowest_ship_index].id


#     elif packing_variation.lower() == "worst":
    
#     else:
#         raise TypeError("Define")
    

# def updateship(ship, parcel)
