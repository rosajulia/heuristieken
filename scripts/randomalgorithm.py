import random

# create random solutions
def random_algorithm(dict_space, dict_parcel):

    ship_counter = 0
    parcel_amount = 0
    parcel_weight_max = 269.3
    parcel_volume_max = 0.849

    # make shuffled list
    shuffled_list = random.sample(range(100), k = 100)

    # start weight and volume at zero and set to not full
    for element in dict_space:
        element.current_weight = 0
        element.current_volume = 0
        element.full = False

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
        print("parcel number: ", end="")
        print(add_ID)

        # add parcel to ship
        dict_parcel[add_ID - 1].location = ship_counter

        # update spaceships current weight and volume
        dict_space[ship_counter].current_weight += dict_parcel[add_ID - 1].weight
        dict_space[ship_counter].current_volume += dict_parcel[add_ID - 1].volume

        # count parcels per solution
        parcel_amount += 1

        print(ship_counter)
        print(dict_space[ship_counter].current_weight)
        print(dict_space[ship_counter].current_volume)

        # note when ship is full
        if (dict_space[ship_counter].current_weight >= dict_space[ship_counter].max_weight - parcel_weight_max or
                    dict_space[ship_counter].current_volume >= dict_space[ship_counter].max_volume - parcel_volume_max):
            dict_space[ship_counter].full = True

    return parcel_amount
