#!/usr/bin/env python
import random

# create 4 random solutions
def random_algorithm(dict_space, dict_parcel):

    ship_counter = 0
    parcel_amount = 0

    # start weight and volume at zero
    for element in dict_space:
        element.current_weight = 0
        element.current_volume = 0

    # add parcel till limits are reached
    while (dict_space[ship_counter].current_weight <= dict_space[ship_counter].max_weight and 
                dict_space[ship_counter].current_volume <= dict_space[ship_counter].max_volume):

        # pick random parcel
        add_ID = random.randint(1, 100)

        # add parcel to ship
        dict_parcel[add_ID - 1].location = ship_counter

        # update spaceships current weight and volume
        dict_space[ship_counter].current_weight += dict_parcel[add_ID - 1].weight
        dict_space[ship_counter].current_volume += dict_parcel[add_ID - 1].volume

        # count parcels per solution
        parcel_amount += 1

        print("Spaceship: ", end="")
        print(ship_counter)
        print("current_weight: ", end="")
        print(dict_space[ship_counter].current_weight)
        print("current_volume: ", end="")
        print(dict_space[ship_counter].current_volume)
        print("parcel amount: ", end="")
        print(parcel_amount)

        # iterate over ship to add parcel to
        # if ship_counter % 3 != 0:
        #     ship_counter += 1
        # else:
        #     ship_counter = 0
        if (ship_counter == 3):
            ship_counter = 0
        else:
            ship_counter += 1

    return parcel_amount