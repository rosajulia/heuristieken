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
    ship1, ship2, ship3, ship4, noship = [], [], [], [], []
    dict_parcel = inventory.dict_parcel
    dict_space = inventory.dict_space
    for element in dict_parcel:
        if element.location is 0:
            noship.append(element.id + 1)
        elif element.location is 1:
            ship1.append(element.id + 1)
        elif element.location is 2:
            ship2.append(element.id + 1)
        elif element.location is 3:
            ship3.append(element.id + 1)
        elif element.location is 4:
            ship4.append(element.id + 1)
    return "Ship 1: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: {}\n Ship 2: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: \
     {}\n Ship 3: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: {}\n Ship 4: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: {}\n No ship \
    : {}".format(ship1, dict_space[0].current_weight, dict_space[0].current_volume, dict_space[0].max_weight - dict_space[0].current_weight,  \
    dict_space[0].max_volume - dict_space[0].current_volume, ship2, dict_space[1].current_weight, dict_space[1].current_volume, \
    dict_space[1].max_weight - dict_space[1].current_weight, dict_space[1].max_volume - dict_space[1].current_volume, ship3, \
    dict_space[2].current_weight, dict_space[2].current_volume, dict_space[2].max_weight - dict_space[2].current_weight, \
    dict_space[2].max_volume - dict_space[2].current_volume, ship4, dict_space[3].current_weight, dict_space[3].current_volume, dict_space[3].max_weight - dict_space[3].current_weight, dict_space[3].max_volume - dict_space[3].current_volume, noship)
