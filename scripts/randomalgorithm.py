#!/usr/bin/env python
# wat is er random?
# - random id van pakketje tussen 0 en 100
#   - kan alleen pseudorandom want als een pakketje al ergens in zit is het 'bezet'
#   - of mag je nog wisselen later? dan wel random misschien, of random uit de bezette pakketjes
# - random spaceship om het in te stoppen
#   - bij max bereikt meteen niet meer suggereren?
#   - of bij max bereik nog mogen wisselen
# - random factor in de berekening naar een distribution
# - random combi van 4*21 of iets daaromheen
# constraints:
# - maximaal volume en gewicht
# - loose of strict?
# optimaliseren:
# - combi van pakketjes die dichtst bij de max komt

import random

# create 4 random solutions
def random_algorithm(dict_space, dict_parcel):

    # for i in range(6):
    ship_counter = 0
    parcel_amount = 0

    # continue adding parcels until reach of maximum payload mass or volume
    # kan zijn dat de manier van indexeren hier anders moet want nu is het niet subscriptable volgens python
    while (dict_space[ship_counter].current_weight <= dict_space[ship_counter].max_weight and dict_space[ship_counter].current_volume <= dict_space[ship_counter].max_volume):

        # choose random parcel id to add to ship
        # check whether 99 or 100 (also depends on id numbers in cargo list)
        add_ID = random.randint(1, 100)

        # change location of parcel to correct ship
        # -1 zodat je de goeie uit de lijst pakt
        dict_parcel[add_ID - 1].location = ship_counter
        # OR array/list of parcels in 4 ships

        # update spaceships current mass and volume
        dict_space[ship_counter].current_weight += dict_parcel[add_ID - 1].weight
        dict_space[ship_counter].current_volume += dict_parcel[add_ID - 1].volume

        # keep track of amount of parcels in current solution
        parcel_amount += 1

        print("Spaceship: ", end="")
        print(ship_counter)
        print("current_weight: ", end="")
        print(dict_space[ship_counter].current_weight)
        print("current_volume: ", end="")
        print(dict_space[ship_counter].current_volume)
        print("parcel amount: ", end="")
        print(parcel_amount)

        # itirate over ship to add parcel to
        if (ship_counter == 3):
            ship_counter = 0
        else:
            ship_counter += 1

    return parcel_amount

    # display locations of loaded parcels
    # print({"parcel_amount" : parcel_amount})
    # print("locations:")
    # # for parcel in parcels:
    #     if (parcel.location != 0):
    #         print({parcel.id : parcel.location})
