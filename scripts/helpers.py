def reset(element):
    """Resets attributes of the ships.
    """
    element.current_weight = 0
    element.current_volume = 0
    element.full = False

    return element
