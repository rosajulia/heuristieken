import random
from classes import classes
import isfull, shiploader

def generateships(ships, cargolist, constraint):
    """
    !!UPDATE DOCSTRING!!

    Takes one command-line argument of type boolean to:
        - False for no constraints
        - True for constraints

    constraint: setting constraints to True will generate ships given that 
    nations must send an equal number of ships. The difference in the number of 
    ships each nation sends cannot be larger than one.
    """

    # check for correct user input
    if constraint != type(True):
        raise TypeError("Expected boolean for arg constraint")

    temp_cargo = cargolist
    fleet = []

    # if any number of ships can be used
    if constraint == False:

        # loop while there is still cargo left
        while len(temp_cargo) > 0:

            # pick a random ship from the list
            ship = random.choice(ships)

            # fill that ship with parcels
            temp_cargo = shiploader(ship, temp_cargo)

            # append the filled ship to the fleet list
            fleet.append(ship)
        
        return fleet

    # if constraints are active
    else:

        # keep the score for the number of ships each nation has
        score_keeper = {}

        # make a dict to store scores for nations
        for ship in ships:

            # add condition because USA has two ships
            if ship["nation"] not in score_keeper:
                country = ship["nation"]
                taken = False
                score_keeper[country] = taken

        # loop while there is still cargo left
        while len(temp_cargo) > 0:

            # pick a random ship from the list
            ship = random.choice(ships)

            # keep picking a random ship while keeping scores even
            while score_keeper[ship["nation"]] == True:
                ship = random.choice(ships)

            # set the score keeper to taken
            score_keeper["nation"] = True

            # fill the ship with parcels
            temp_cargo = shiploader(ship, temp_cargo)

            # append the filled ship to the fleet list
            fleet.append(ship)

            # check if all nations are even
            if False not in score_keeper.values():

                # reset the score keeper
                score_keeper = {nation:False for nation in score_keeper}
        
        return fleet

            