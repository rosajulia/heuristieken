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


# create 4 random solutions
def random_algorithm(self, dict_space, dict_parcel):

    for i in range(4):
        ship_counter = 1
        parcel_amount = 0
        current_weight = 0
        current_volume = 0
        
        # continue adding parcels until reach of maximum payload mass or volume
        while (current_weight <= dict_space[i]["max_weight"]) and (current_volume <= dict_space[i]["max_volume"]):

            # choose random parcel id to add to ship
            add_ID = dict_parcel[(random.randint(0,100))]["parcel_ID"]

            # change location of parcel to correct ship
            dict_parcel[add_ID]["location"] = ship_counter

            # OR array/list of parcels in 4 ships

            # update spaceships current mass and volume
            current_weight += dict_parcel[add_ID]["weight"]
            current_volume += dict_parcel[add_ID]["volume"]

            # keep track of amount of parcels in current solution
            parcel_amount += 1

            # itirate over ship to add parcel to
            if (ship_counter == 4):
                ship_counter = 1
            else:
                ship_counter += 1

        # display locations of loaded parcels
        print({"parcel_amount" : parcel_amount})
        print("locations:")
        for parcel in parcels:
            if (parcel.location != 0):
                print({parcel.id : parcel.location})


