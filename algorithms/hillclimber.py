import random
from copy import copy, deepcopy
from scripts import fillitup, helpers

def hill_climber(inventory, repetitions):

    best_inventory = inventory
    print(best_inventory)

    for _ in range(repetitions):

        # keep track of how many manipulations have been performed
        # repetition_counter = current_repetition
        # print(repetition_counter)

        # save initial inventory to compare manipulated inventory with
        inventory_pre = best_inventory
        # print(inventory_pre.solution_id)
        inventory_mid = deepcopy(inventory)

        # determine which parcels are currently in which ship
        remaining_parcels = []
        occupied_parcels = []
        for parcel in inventory.dict_parcel:
            if parcel.location == 0:
                remaining_parcels.append(parcel.id)
            else:
                occupied_parcels.append(parcel.id)

        # print(len(occupied_parcels), len(remaining_parcels))


        # get amount of parcels to remove
        # (misschien wat verschillende getallen proberen en gemiddelde berekenen om te kijken wat het beste werkt?)
        remove_amount_parcels = random.randint(1,10)

        # ensure enough parcels occupied to remove
        while remove_amount_parcels > len(occupied_parcels):
            remove_amount_parcels = random.randint(1, 10)

        # loop as often as amount of parcels to remove
        for _ in range(remove_amount_parcels):

            # decide randomly which of the occupied parcels to remove
            parcel_index_to_remove = random.randint(0,len(occupied_parcels))
            # print(len(occupied_parcels), occupied_parcels)
            if parcel_index_to_remove >= len(occupied_parcels):
                break
            else:
                parcel_id_to_remove = occupied_parcels[parcel_index_to_remove]

                # update parcel's location and ships current weight and volume
                for parcel in inventory_mid.dict_parcel:
                    if parcel.id is parcel_id_to_remove:
                        for ship in inventory_mid.dict_space:
                            if ship.id is parcel.location:
                                ship.current_weight -= parcel.weight
                                ship.current_volume -= parcel.volume
                                break
                        parcel.location = 0
                        inventory_mid.parcel_amount -= 1
                        break

                # update lists of occupied and remaining parcels
                occupied_parcels.remove(parcel_id_to_remove)
                remaining_parcels.append(parcel_id_to_remove)

        inventory_mid.total_costs = inventory_mid.calculate_costs()
        # print("midcosts", inventory_mid.total_costs)

        # print("mid")
        # sol = helpers.visualizeParcelsPerShip(inventory_mid)
        # for element in sol:
        #     print(element)
        # call random_algorithm to fill with current situation as starting point
        # compare output inventory of random_algorithm.parcel_amount with earlier parcel_amount
        inventory_post = fillitup.fill_it_up(inventory_mid)
        # print("typeinvpost", type(inventory_post))

        # continue with hillclimber output if more parcels than before
        if inventory_post.parcel_amount > inventory_pre.parcel_amount:
            # repetition_counter += 1
            best_inventory = inventory_post
            # if repetition_counter < repetitions:
            #     # print("again1", inventory_post.parcel_amount, inventory_pre.parcel_amount)
            #     # sol = helpers.visualizeParcelsPerShip(inventory_post)
            #     # for element in sol:
            #     #     print(element)
            #     return hill_climber(inventory_post, repetitions, repetition_counter)
            # else:
            #     print("retpost1")
            #     return inventory_post

        # continue with hillclimber output if same amount of parcels but cheaper
        elif inventory_post.parcel_amount == inventory_pre.parcel_amount and inventory_post.total_costs < inventory_pre.total_costs:
            # repetition_counter += 1
            best_inventory = inventory_post
            # if repetition_counter < repetitions:
            #     # print("again2", inventory_post.parcel_amount, inventory_pre.parcel_amount)
            #     # sol = helpers.visualizeParcelsPerShip(inventory_post)
            #     # for element in sol:
            #     #     print(element)
            #     return hill_climber(inventory_post, repetitions, repetition_counter)
            # else:
            #     print("retpost2")
            #     return inventory_post

        else:
            best_inventory = inventory_pre
            # repetition_counter += 1
            # if repetition_counter < repetitions:
            #     # print("againpre", inventory_post.parcel_amount, inventory_pre.parcel_amount)
            #     # sol = helpers.visualizeParcelsPerShip(inventory_pre)
            #     # for element in sol:
            #     #     print(element)
            #     return hill_climber(inventory_pre, repetitions, repetition_counter)
            # else:
            #     print("retpre")
            #     # print(type(inventory_pre))
            #     # print(inventory_pre.solution_id)
            #     return inventory_pre

    return best_inventory


        # als geen pakketjes in schip --> niet meetellen in kosten
        # hillclimber met pakketjes vs hillclimber met de vloot

        # zorgen dat je hillclimber kan aanroepen met een inventory als beginpunt


        # hillclimber
            # use remainder of shuffles list from greedy
            # change in greedy:
                # instead of pop, add to other list (occupied parcels)
                # include these lists? or recreate in hillclimber based on parcel locations
            # choose:
                # random amount to remove
                # random parcel id's to remove
            # chosen numbers
                # --> change location to 0
                # --> add numbers to remainder list
                # --> adjust current weights and volumes
            # fill randomly until full (reuse code of other algorithms)
                # --> change parcel locations
                # --> add numbers to occupied list
                # --> adjust current weights and volumes
            # consider outcome costs
                # higher ==> use this inventory as new starting point
                # lower ==> ignore and start over from current best starting point

            # should return inventory
