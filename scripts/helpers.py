from copy import copy, deepcopy


def reset(element):
    """Resets attributes of the ships."""
    element.current_weight = 0
    element.current_volume = 0
    element.full = False

    return element

def resetParcel(element):
    """Resets location of parcels."""
    element.location = 0

    return element

def visualizeParcelsPerShip(inventory):
    """Prints lists of parcel id's per ship, as well as remaining parcel id's."""
    dict_space_list = []
    for ship in inventory.dict_space:
        ship_id = ship.id
        ship_list = []
        for parcel in inventory.dict_parcel:
            if parcel.location is ship_id:
                ship_list.append(parcel.id + 1)
        ship_dict = {"id": ship_id,
                     "type": ship.type,
                     "content": ship_list}
        dict_space_list.append(deepcopy(ship_dict))

    return dict_space_list
