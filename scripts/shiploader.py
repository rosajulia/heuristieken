import random

def shiploader(ship, cargolist):
    """
    This script is used to update the cargolist.
    Randomly fills ship object with parcels from 
    cargolist.

    Returns an updated cargolist with all non-taken
    parcels remaining.
    """

    temp_cargolist = cargolist
    weight_left = ship.max_weight
    volume_left = ship.max_volume
    full = False

    # repeat loop until the ship is full
    while not full:

        # pick a random parcel from the list
        parcel = random.choice(cargolist)

        if parcel.weight <= weight_left and parcel.volume <= volume_left:

            weight_left -= parcel.weight
            volume_left -= parcel.volume

            temp_cargolist.remove(parcel)
        
        else:

            full = True

    return temp_cargolist
