from copy import copy, deepcopy


def reset(element):
    """
    Script that resets certain attributes of element.

    Returns an object of type Spaceship.

    Takes one argument:

        element: Must contain object of type Spaceship.
    """
    
    # reset attributes to default state
    element.current_weight = 0
    element.current_volume = 0
    element.full = False

    return element


def resetParcel(element):
    """
    Script that resets certain attributes of element.

    Returns an object of type Parcel.

    Takes one argument:

        element: Must contain object of type Parcel.
    """

    # reset attributes to default state
    element.location = 0

    return element


def visualizeParcelsPerShip(inventory):
    """
    This script is used to print lists of parcel id's per ship, as well as 
    parcel id's that are not stored in a spaceship.

    Returns a list of objects of type dict containing the contents of every
    ship.

    Take one argument:

        inventory: Must contain object of type Inventory.
    """

    # make an empty list
    dict_space_list = []

    # for every ship in the fleet
    for ship in inventory.dict_space:

        # save the id
        ship_id = ship.id

        # make an empty list to store the parcels
        ship_list = []

        # append all the parcel ids to the correct ship
        for parcel in inventory.dict_parcel:

            # only if the location of the parcel corresponds with the ship id
            if parcel.location is ship_id:
                ship_list.append(parcel.id + 1)
        
        # create a dict object with correct attributes
        ship_dict = {"id": ship_id,
                     "type": ship.type,
                     "current weight": ship.current_weight,
                     "current_volume": ship.current_volume,
                     "content": ship_list}

        # append the ship to the master list
        dict_space_list.append(deepcopy(ship_dict))

    return dict_space_list
