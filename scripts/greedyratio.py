from scripts import helpers
from operator import itemgetter

def greedy_ratio(dict_space, dict_parcel):
    """Greedy algorithm based on the ratios of weight and volume per parcel, and
    suitable ships for those ratios."""

    ship_counter = 0
    parcel_amount = 0
    parcel_weight_max = 269.3
    parcel_volume_max = 0.849

    # start weight and volume at zero and set to not full
    dict_space = [helpers.reset(element) for element in dict_space]

    # set location of parcels to zero
    dict_parcel = [helpers.resetParcel(element) for element in dict_parcel]

    # ratio weight/Volume
    # ship 1 105.82
    # ship 2 315.79
    # ship 3 371.43
    # ship 4 600

    ratio_array = []

    for element in dict_parcel:
        ratio_dict = {
        "id": element.id,
        "ratio": element.ratio
        }
        ratio_array.append(ratio_dict)

    new_array = sorted(ratio_array, key=itemgetter('ratio'))

    order_array = []
    for element in new_array:
        id = element["id"]
        order_array.append(id)

    print(order_array)


    # Cygnus met laagste weight/volume ratio pakketjes vullen
    order_place = 0

    while dict_space[0].full is False:
        element_id = order_array[order_place]
        dict_parcel[element_id].location = 0
        dict_space[0].current_weight += dict_parcel[element_id].weight
        dict_space[0].current_volume += dict_parcel[element_id].volume

        if (dict_space[0].current_weight >= dict_space[0].max_weight - parcel_weight_max or
                    dict_space[0].current_volume >= dict_space[0].max_volume - parcel_volume_max):
            dict_space[0].full = True

        order_array.pop(order_array[order_place])

        order_place += 1
        parcel_amount += 1

    # Dragon met hoogste weight/volume ratio pakketjes vullen
    order_place = len(order_array) -1

    while dict_space[3].full is False:
        element_id = order_array[order_place]
        dict_parcel[element_id].location = 3
        dict_space[3].current_weight += dict_parcel[element_id].weight
        dict_space[3].current_volume += dict_parcel[element_id].volume

        if (dict_space[3].current_weight >= dict_space[3].max_weight - parcel_weight_max or
                    dict_space[3].current_volume >= dict_space[3].max_volume - parcel_volume_max):
            dict_space[3].full = True

        order_array.pop(order_array[order_place])

        order_place -= 1
        parcel_amount += 1

    # straks alle pakketjes die nog locatie 4 hebben om en om verdelen over schip 1/2 en 2/3

    order_place = 0
    new_dict_space = dict_space[1:3]

    while dict_space[1].full is False or dict_space[2].full is False:
        for i in range(1,3):
            if dict_space[i].full is True and i is 1:
                i += 1
            if dict_space[i].full is True and i is 2:
                i -= 1
            element_id = order_array[order_place]
            dict_parcel[element_id].location = i
            dict_space[i].current_weight += dict_parcel[element_id].weight
            dict_space[i].current_volume += dict_parcel[element_id].volume

            if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
                        dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
                dict_space[i].full = True
            order_place += 1
        parcel_amount += 1

        # return iets
