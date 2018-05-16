import random
from scripts import helpers
import time

# create random solutions
def random_algorithm(dict_space, dict_parcel):
    """Randomly fills spaceships with a cargo list.
    The first argument holds a list of spaceship objects,
    the second argument holds a list of parcel objects.

    Usage:
    randomalgorithm.random_algorithm(loaded_data[0], loaded_data[1])
    randomalgorithm.random_algorithm(inventory)
    """

    ship_counter = 0
    parcel_amount = 0
    parcel_weight_max = 269.3
    parcel_volume_max = 0.849

    # make shuffled list
    shuffled_list = random.sample(range(100), k=100)

    # start weight and volume at zero and set to not full
    dict_space = [helpers.reset(element) for element in dict_space]

    # set location of parcels to zero
    dict_parcel = [helpers.resetParcel(element) for element in dict_parcel]

    # add parcel until limits are reached (until all ships are full)
    while (dict_space[0].full is False or dict_space[1].full is False or dict_space[2].full is False or dict_space[3].full is False):


        # only continue with ships that are not full
        while dict_space[ship_counter].full is True:
            if ship_counter is 3:
                ship_counter = 0
            else:
                ship_counter += 1
        

        # pick random parcel
        add_ID = shuffled_list.pop()
        # print("parcel number: ", end="")
        # print(add_ID)

        # add parcel to ship
        # checken: ID -1 op alle plekken kloppend?
        dict_parcel[add_ID - 1].location = ship_counter

        # update spaceships current weight and volume
        dict_space[ship_counter].current_weight += dict_parcel[add_ID - 1].weight
        dict_space[ship_counter].current_volume += dict_parcel[add_ID - 1].volume

        # count parcels per solution
        parcel_amount += 1

        # note when ship is almost full
        if (dict_space[ship_counter].current_weight >= dict_space[ship_counter].max_weight - parcel_weight_max or
                    dict_space[ship_counter].current_volume >= dict_space[ship_counter].max_volume - parcel_volume_max):

            for parcel_id in shuffled_list:

                if (dict_space[ship_counter].current_weight + dict_parcel[parcel_id - 1].weight <= dict_space[ship_counter].max_weight and \
                    dict_space[ship_counter].current_volume + dict_parcel[parcel_id - 1].volume <= dict_space[ship_counter].max_volume):

                    dict_space[ship_counter].current_weight += dict_parcel[parcel_id - 1].weight
                    dict_space[ship_counter].current_volume += dict_parcel[parcel_id - 1].volume

                    shuffled_list.remove(parcel_id)

                    dict_parcel[parcel_id - 1].location = ship_counter

                    parcel_amount += 1

                else:
                    continue

            dict_space[ship_counter].full = True

        time.sleep(1)
        yield dict_space[ship_counter].current_weight, ship_counter

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
    print("Ship 1: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: {}\n Ship 2: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: \
     {}\n Ship 3: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: {}\n Ship 4: {}\n CurWeight: {} CurVol: {}\n WeightLeft: {} Volume left: {}\n No ship \
    : {}".format(ship1, dict_space[0].current_weight, dict_space[0].current_volume, dict_space[0].max_weight - dict_space[0].current_weight,  \
    dict_space[0].max_volume - dict_space[0].current_volume, ship2, dict_space[1].current_weight, dict_space[1].current_volume, \
    dict_space[1].max_weight - dict_space[1].current_weight, dict_space[1].max_volume - dict_space[1].current_volume, ship3, \
    dict_space[2].current_weight, dict_space[2].current_volume, dict_space[2].max_weight - dict_space[2].current_weight, \
    dict_space[2].max_volume - dict_space[2].current_volume, ship4, dict_space[3].current_weight, dict_space[3].current_volume, dict_space[3].max_weight - dict_space[3].current_weight, dict_space[3].max_volume - dict_space[3].current_volume, noship))

    return {"parcel_amount": parcel_amount, "weight1": dict_space[0].current_weight, \
                "weight2": dict_space[1].current_weight, "weight3": dict_space[2].current_weight, \
                    "weight4": dict_space[3].current_weight}
