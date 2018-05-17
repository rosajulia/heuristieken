import random
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

    # for visualizing which parcels have high and low ratios
    order_array = []
    for element in new_array:
        id = element["id"]
        order_array.append(id)
    # print(order_array)


    # Cygnus met laagste weight/volume ratio pakketjes vullen
    order_place = 0

    while dict_space[0].full is False:
        element_id = order_array[order_place]
        dict_parcel[element_id].location = 0
        dict_space[0].current_weight += dict_parcel[element_id].weight
        dict_space[0].current_volume += dict_parcel[element_id].volume

        # print(element_id)
        # print(dict_parcel[element_id].location)

        if (dict_space[0].current_weight >= dict_space[0].max_weight - parcel_weight_max or
                    dict_space[0].current_volume >= dict_space[0].max_volume - parcel_volume_max):
            dict_space[0].full = True

        # print(dict_space[0].full)

        # print(order_array)
        order_array = order_array[order_place + 1:]
        # print(order_array)

        # order_place += 1
        parcel_amount += 1

    # Dragon met hoogste weight/volume ratio pakketjes vullen

    while dict_space[3].full is False:
        order_place = len(order_array) -1
        element_id = order_array[order_place]
        dict_parcel[element_id].location = 3
        dict_space[3].current_weight += dict_parcel[element_id].weight
        dict_space[3].current_volume += dict_parcel[element_id].volume

        if (dict_space[3].current_weight >= dict_space[3].max_weight - parcel_weight_max or
                    dict_space[3].current_volume >= dict_space[3].max_volume - parcel_volume_max):
            dict_space[3].full = True
        # print(order_array)
        order_array = order_array[:order_place]
        # print(order_array)
        # order_place -= 1
        parcel_amount += 1

    # straks alle pakketjes die nog locatie 4 hebben om en om verdelen over schip 1/2 en 2/3
    length_other_parcels = len(order_array)
    # order_place = int(length_other_parcels / 2)
    # print(len(order_array))
    # print(order_place)
    # place_increaser = 1

    # # De parcels die over zijn vanuit het midden van de gesorteerde list verdelen
    # while dict_space[1].full is False or dict_space[2].full is False:
        # for i in range(1,3):
        #     if dict_space[i].full is True and i is 1:
        #         i += 1
        #     if dict_space[i].full is True and i is 2:
        #         i -= 1
        #     print(order_array[order_place])
        #     element_id = order_array[order_place]
        #     dict_parcel[element_id].location = i
        #     dict_space[i].current_weight += dict_parcel[element_id].weight
        #     dict_space[i].current_volume += dict_parcel[element_id].volume
        #
        #     if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
        #                 dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
        #         dict_space[i].full = True
        #
        #     if i is 1:
        #         order_place += place_increaser
        #     else:
        #         order_place -= place_increaser
        #     place_increaser += 1
        #     parcel_amount += 1
        #     print(i)
        #     print(dict_space[i].current_weight)
        #     print(dict_space[i].current_volume)
        #     print(dict_space[i].full)


    #
    # make shuffled list
    shuffled_list = random.sample(range(length_other_parcels), k=length_other_parcels)
    # location_other_parcels = 0

    # de parcels die over zijn random verdelen
    while dict_space[1].full is False or dict_space[2].full is False:
        for i in range(1,3):
            if dict_space[i].full is True and i is 1:
                i += 1
            if dict_space[i].full is True and i is 2:
                i -= 1
            # print(shuffled_list[location_other_parcels])
            parcel_to_add = order_array[shuffled_list[0]]
            # print(parcel_to_add)
            dict_parcel[parcel_to_add].location = i
            dict_space[i].current_weight += dict_parcel[parcel_to_add].weight
            dict_space[i].current_volume += dict_parcel[parcel_to_add].volume

            # ipv dit gewoon eruit gooien en dan steeds 0
            # location_other_parcels += 1
            shuffled_list = shuffled_list[1:]

            if (dict_space[i].current_weight >= dict_space[i].max_weight - parcel_weight_max or
                        dict_space[i].current_volume >= dict_space[i].max_volume - parcel_volume_max):
                dict_space[i].full = True
            parcel_amount += 1


    # hier nog bij alle schepen proberen de overige pakketjes toe te voegen
    shuffled_length = len(shuffled_list)
    # print(shuffled_length)
    # print(shuffled_list)
    for i in range(3):
        for ship in dict_space:
            for parcel in shuffled_list:
                print(shuffled_list)
                if (ship.current_weight + dict_parcel[parcel].weight <= ship.max_weight and \
                        ship.current_volume + dict_parcel[parcel].volume <= ship.max_volume):

                    ship.current_weight += dict_parcel[parcel].weight
                    ship.current_volume += dict_parcel[parcel].volume

                    shuffled_list.remove(parcel)

                    dict_parcel[parcel + 1].location = ship.id

                    parcel_amount += 1




    ship1, ship2, ship3, ship4, noship = [], [], [], [], []

    for element in dict_parcel:
        if element.location is 0:
            ship1.append(element.id + 1)
        elif element.location is 1:
            ship2.append(element.id + 1)
        elif element.location is 2:
            ship3.append(element.id + 1)
        elif element.location is 3:
            ship4.append(element.id + 1)
        elif element.location is 4:
            noship.append(element.id + 1)


    # print("Ship 1: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: {}\n Ship 2: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: \
    #  {}\n Ship 3: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: {}\n Ship 4: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: {}\n No ship \
    # : {}".format(ship1, dict_space[0].current_weight, dict_space[0].current_volume, dict_space[0].max_weight - dict_space[0].current_weight,  \
    # dict_space[0].max_volume - dict_space[0].current_volume, ship2, dict_space[1].current_weight, dict_space[1].current_volume, \
    # dict_space[1].max_weight - dict_space[1].current_weight, dict_space[1].max_volume - dict_space[1].current_volume, ship3, \
    # dict_space[2].current_weight, dict_space[2].current_volume, dict_space[2].max_weight - dict_space[2].current_weight, \
    # dict_space[2].max_volume - dict_space[2].current_volume, ship4, dict_space[3].current_weight, dict_space[3].current_volume, dict_space[3].max_weight - dict_space[3].current_weight, dict_space[3].max_volume - dict_space[3].current_volume, noship))

    return {"parcel_amount": parcel_amount, "weight1": dict_space[0].current_weight, \
                "weight2": dict_space[1].current_weight, "weight3": dict_space[2].current_weight, \
                    "weight4": dict_space[3].current_weight}
        # return iets
