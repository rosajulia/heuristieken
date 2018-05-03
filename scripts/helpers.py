def reset(element):
    """Resets attributes of the ships."""
    element.current_weight = 0
    element.current_volume = 0
    element.full = False

    return element

def resetParcel(element):
    """Resets location of parcels."""
    element.location = 4

    return element
