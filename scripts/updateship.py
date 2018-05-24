def updateship(ship, parcel):
    """
    This script updates the attributes of a ship when a parcel is stored in it.

    Returns an object of type Spaceship.

    Take two arguments:

        ship: Must contain object of type Spaceship.

        parcel: Must contain object of type Parcel.
    """

    # store a copy of the current ship
    updated_ship = ship

    # update the properties of the current ship
    updated_ship.current_weight = updated_ship.current_weight - parcel.weight
    updated_ship.current_volume = updated_ship.current_volume - parcel.volume

    return updated_ship