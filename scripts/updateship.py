def updateship(ship, parcel):

    """
    Returns an updated ship with adjusted weight and volume.

    Take two arguments:

        ship: Must contain ship object with loaded attributes.

        parcel: Must contain parcel object with loaded attributes.
    """

    updated_ship = ship

    updated_ship.current_weight = updated_ship.current_weight - parcel.weight
    updated_ship.current_volume = updated_ship.current_volume - parcel.volume

    return updated_ship