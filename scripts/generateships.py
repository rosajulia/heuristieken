import random
from classes import classes
from scripts import shiploader
from copy import copy, deepcopy

def generateships(inventory, constraint):
    """
    This script generates a fleet of ships that is large enough to hold all
    packages.

    Returns a list of objects of type Spaceship.

    Takes two arguments:

        inventory: Must contain object of type inventory.

        constraint: 
            True: Setting constraint to True will generate ships given that 
            nations must send an equal number of ships. The difference in the 
            number of ships each nation sends cannot be larger than one. 
            
            False: Setting constraint to False will disregard any diplomatic 
            constraints and will generate a fleet of ships at random.
    """

    fleet = []
    ships = deepcopy(inventory.dict_space)
    temp_cargo = deepcopy(inventory.dict_parcel)
    ship_counter = 1

    # if any number of ships can be used
    if constraint is "False":

        # loop while there is still cargo left
        while len(temp_cargo) > 0:

            # pick a random ship from the list
            ship = deepcopy(random.choice(ships))
            ship.id  = ship_counter

            # fill that ship with parcels
            temp_cargo = shiploader.shiploader(ship, temp_cargo)

            # append the filled ship to the fleet list
            fleet.append(ship)

            ship_counter += 1
        
        inventory.dict_space = deepcopy(fleet)

        return inventory

    # if constraints are active
    else:

        # keep the score for the number of ships each nation has
        score_keeper = {}

        # make a dict to store scores for nations
        for ship in ships:

            # add condition because USA has two ships
            if ship.nation not in score_keeper:
                nation = ship.nation
                taken = False
                score_keeper[nation] = taken

        # loop while there is still cargo left
        while len(temp_cargo) > 0:

            # pick a random ship from the list
            ship = random.choice(ships)
            ship.id = ship_counter

            # keep picking a random ship while keeping scores even
            while score_keeper[ship.nation] == True:
                ship = random.choice(ships)

            # set the score keeper to taken
            score_keeper[ship.nation] = True

            # fill the ship with parcels
            temp_cargo = shiploader.shiploader(ship, temp_cargo)

            # append the filled ship to the fleet list
            fleet.append(ship)

            ship_counter += 1

            # check if all nations are even
            if False not in score_keeper.values():

                # reset the score keeper
                score_keeper = {nation:False for nation in score_keeper}

        inventory.dict_space = fleet
        
        return inventory

            