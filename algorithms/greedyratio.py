import random
from algorithms import helpers
from operator import itemgetter
import time

def greedy_ratio(inventory):
    """Greedy algorithm based on the ratios of weight and volume per parcel, and
    suitable ships for those ratios."""

    # zorgen dat greedy met lege inventory begint

    dict_space = inventory.dict_space
    dict_parcel = inventory.dict_parcel

    # ship_counter = 0
    parcel_amount = 0
    parcel_weight_max = 269.3
    parcel_volume_max = 0.849

    # start weight and volume at zero and set to not full
    dict_space = [helpers.reset(element) for element in dict_space]

    # set location of parcels to zero
    dict_parcel = [helpers.resetParcel(element) for element in dict_parcel]

    ratio_array = []

    for element in dict_parcel:
        ratio_dict = {
        "id": element.id,
        "ratio": element.ratio
        }
        ratio_array.append(ratio_dict)

    new_array = sorted(ratio_array, key=itemgetter('ratio'))

    # for visualizing which parcels have high and low ratios
    order_array = []
    for element in new_array:
        id = element["id"]
        order_array.append(id)

    # fill spaceship 1 ratio-based
    order_place = 0

    while dict_space[0].full is False:
        element_id = order_array[order_place]

        time.sleep(1)
        yield dict_space[0].current_weight, 0
        dict_parcel[element_id].location = 0
        dict_space[0].current_weight += dict_parcel[element_id].weight
        dict_space[0].current_volume += dict_parcel[element_id].volume


        if (dict_space[0].current_weight >= dict_space[0].max_weight - parcel_weight_max or
                    dict_space[0].current_volume >= dict_space[0].max_volume - parcel_volume_max):
            dict_space[0].full = True

        order_array = order_array[order_place + 1:]

        parcel_amount += 1
    # fill spaceship 4 ratio-based
    while dict_space[3].full is False:
        order_place = len(order_array) -1
        element_id = order_array[order_place]

        time.sleep(1)
        yield dict_space[3].current_weight, 3
        dict_parcel[element_id].location = 3
        dict_space[3].current_weight += dict_parcel[element_id].weight
        dict_space[3].current_volume += dict_parcel[element_id].volume

        if (dict_space[3].current_weight >= dict_space[3].max_weight - parcel_weight_max or
                    dict_space[3].current_volume >= dict_space[3].max_volume - parcel_volume_max):
            dict_space[3].full = True

        order_array = order_array[:order_place]
        parcel_amount += 1

    # divide remaining cargo
    length_other_parcels = len(order_array)

    # make shuffled list
    shuffled_list = random.sample(range(length_other_parcels), k=length_other_parcels)

    # random divide cargo between spacechips 2 and 3
    while dict_space[1].full is False or dict_space[2].full is False:
        for i in range(1,3):
            if dict_space[i].full is True and i is 1:
                i += 1
            if dict_space[i].full is True and i is 2:
                i -= 1

            parcel_to_add = order_array[shuffled_list[0]]
            dict_parcel[parcel_to_add].location = i
            dict_space[i].current_weight += dict_parcel[parcel_to_add].weight
            dict_space[i].current_volume += dict_parcel[parcel_to_add].volume

            shuffled_list = shuffled_list[1:]

            if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
                        dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
                dict_space[i].full = True
            parcel_amount += 1

    # add last cargo to ships
    # shuffled_length = len(shuffled_list)
    for i in range(3):
        for ship in dict_space:
            for parcel in shuffled_list:
                # print(shuffled_list)
                if (ship.current_weight + dict_parcel[parcel].weight <= ship.max_weight and \
                        ship.current_volume + dict_parcel[parcel].volume <= ship.max_volume):

                    ship.current_weight += dict_parcel[parcel].weight
                    ship.current_volume += dict_parcel[parcel].volume

                    shuffled_list.remove(parcel)

                    dict_parcel[parcel + 1].location = ship.id

                    parcel_amount += 1

    print(visualizeParcelsPerShip(inventory))
    # ship1, ship2, ship3, ship4, noship = [], [], [], [], []
    #
    # for element in dict_parcel:
    #     if element.location is 0:
    #         noship.append(element.id + 1)
    #     elif element.location is 1:
    #         ship1.append(element.id + 1)
    #     elif element.location is 2:
    #         ship2.append(element.id + 1)
    #     elif element.location is 3:
    #         ship3.append(element.id + 1)
    #     elif element.location is 4:
    #         ship4.append(element.id + 1)

    # return inventory ipv hieronder

    return {"parcel_amount": parcel_amount, "weight1": dict_space[0].current_weight, \
                "weight2": dict_space[1].current_weight, "weight3": dict_space[2].current_weight, \
                    "weight4": dict_space[3].current_weight}
