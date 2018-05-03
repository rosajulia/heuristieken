from scripts import helpers

def greedy_ratio(dict_space, dict_parcel):
    """Greedy algorithm based on the ratios of weight and volume per parcel, and
    suitable ships for those ratios."""

    ship_counter = 0
    parcel_counter = 0

    # start weight and volume at zero and set to not full
    dict_space = [helpers.reset(element) for element in dict_space]

    # set location of parcels to zero
    dict_parcel = [helpers.resetParcel(element) for element in dict_parcel]
