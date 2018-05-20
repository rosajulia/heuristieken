import random

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


def hill_climber(inventory):

    #     save the parcel distribution in list of dicts: or create new one with new id?
    # current_distribution = []
    remaining_parcels = []
    occupied_parcels = []

    # kan ook als: ?
    inventory_pre = inventory
    inventory_mid = inventory_pre

    for parcel in inventory.dict_parcel:
        # parcel_id_location = {parcel.id: parcel.location} # moeten er aanhalingstekens bij de key?
        # current_distribution.append(parcel_id_location)
        if parcel.location == 0:
            remaining_parcels.append(parcel.id)
        else:
            occupied_parcels.append(parcel.id)
    # current_parcel_amount = inventory.parcel_amount
    # current_costs = inventory.total_costs

    # get amount of parcels to remove (misschien wat verschillende getallen proberen en gemiddelde berekenen om te kijken wat het beste werkt?)
    remove_amount_parcels = randint(1, 10)

    # loop as often as amount of parcels to remove
    for _ in range(remove_amount_parcels):

        # decide randomly which of the occupied parcels to remove
        parcel_to_remove = randint(0,len(occupied_parcels))
        parcel_id_to_remove = occupied_parcels[parcel_to_remove].id # klopt nog niet

        # update current weight and volume of ship parcel resided in
        inventory_mid.dict_space[inventory_mid.dict_parcel[parcel_id_to_remove - 1].location].current_weight -= inventory_mid.dict_parcel[parcel_id_to_remove - 1].weight
        inventory_mid.dict_space[inventory_mid.dict_parcel[parcel_id_to_remove - 1].location].current_volume -= inventory_mid.dict_parcel[parcel_id_to_remove - 1].volume

        # update parcel location and lists of occupied and remaining parcels
        inventory_mid.dict_parcel[parcel_id_to_remove - 1].location = 0
        occupied_parcels.remove(parcel_to_remove)
        remaining_parcels.append(inventory_mid.dict_parcel[parcel_id_to_remove].id)

    # call random_algorithm to fill with current situation as starting point
    # compare output inventory of random_algorithm.parcel_amount with earlier parcel_amount
    inventory_post = randomalgorithm.random_algorithm(inventory_mid)

    # continue with hillclimber output if more parcels than before
    if inventory_post.parcel_amount > inventory_pre.parcel_amount:
        return inventory_post

    # continue with hillclimber output if same amount of parcels but cheaper
    elif inventory_post.parcel_amount == inventory_pre.parcel_amount and inventory_post.total_costs < inventory_pre.total_costs:
        return inventory_post

    else:
        return



        # als geen pakketjes in schip --> niet meetellen in kosten
        # hillclimber met pakketjes vs hillclimber met de vloot
