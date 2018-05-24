import random

def shiploader(ship, cargolist):
    """
    This script updates the cargolist by removing parcels that can be fitted in 
    the ship. This script does NOT store the locations of the parcels, nor does 
    it change the properties of a ship. It is ONLY used to generate a fleet of 
    spaceships that will be used in other algorithms.

    Returns a new list of objects of type Parcel.

    Takes two arguments:

        ship: Must contain an object of type Spaceship.

        cargolist: Must contain a list of objects of type Parcel.
    """

    temp_cargolist = cargolist
    weight_left = ship.max_weight
    volume_left = ship.max_volume
    full = False

    # repeat loop until the ship is full
    while full is False and len(temp_cargolist) > 0:

        print(len(temp_cargolist))

        # pick a random parcel from the list
        parcel = random.choice(temp_cargolist)

        if parcel.weight <= weight_left and parcel.volume <= volume_left: 

            weight_left -= parcel.weight
            volume_left -= parcel.volume

            temp_cargolist.remove(parcel)
        
        else:

            full = True

    return temp_cargolist
