def updateship(ship, parcel, method):
    """
    This script updates the attributes of a ship when a parcel is stored in it.

    Returns an object of type Spaceship.

    Take three arguments:

        ship: Must contain object of type Spaceship.

        parcel: Must contain object of type Parcel.

        method: Must containt string argument.
            "+": Selecting this method will pack ships by ADDING parcels to the
            ship, and updating its current weight appropriately.

            "-": Selecting this method will unpack ships by REMOVING parcels 
            from the ship, and updating its current weight appropriately.
    """

    # store a copy of the current ship
    updated_ship = ship

    if method == "+":

        # update the properties of the current ship
        updated_ship.current_weight = updated_ship.current_weight + parcel.weight
        updated_ship.current_volume = updated_ship.current_volume + parcel.volume

        return updated_ship

    elif method == "-":

        # update the properties of the current ship
        updated_ship.current_weight = updated_ship.current_weight - parcel.weight
        updated_ship.current_volume = updated_ship.current_volume - parcel.volume

        return updated_ship

    else:
        raise TypeError("Method argument must be string: '+' or '-'")