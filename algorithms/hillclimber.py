import random
from copy import copy, deepcopy
from helperscripts import fillitup, helpers, updateship
from algorithms import annealinghelper

def hill_climber(inventory, repetitions, constraint):

    best_inventory = inventory
    solutions = [best_inventory]

    # simulated annealing parameters
    current_repetition = 1
    maxTemp = 100

    for _ in range(repetitions):
        # save initial inventory to compare manipulated inventory with
        inventory_pre = best_inventory
        inventory_mid = deepcopy(inventory)

        # determine which parcels are currently in which ship
        remaining_parcels = []
        occupied_parcels = []
        for parcel in inventory.dict_parcel:
            if parcel.location == 0:
                remaining_parcels.append(parcel.id)
            else:
                occupied_parcels.append(parcel.id)

        # get amount of parcels to remove
        remove_amount_parcels = random.randint(1,10)

        # ensure enough parcels occupied to remove
        while remove_amount_parcels > len(occupied_parcels):
            remove_amount_parcels = random.randint(1, 10)

        # loop as often as amount of parcels to remove
        for _ in range(remove_amount_parcels):

            # decide randomly which of the occupied parcels to remove
            parcel_index_to_remove = random.randint(0,len(occupied_parcels))
            if parcel_index_to_remove >= len(occupied_parcels):
                break
            else:
                parcel_id_to_remove = occupied_parcels[parcel_index_to_remove]

                # update parcel's location and ships current weight and volume
                for parcel in inventory_mid.dict_parcel:
                    if parcel.id is parcel_id_to_remove:
                        for ship in inventory_mid.dict_space:
                            if ship.id is parcel.location:
                                ship = updateship.update_ship(ship, parcel, "-")
                                break
                        parcel.location = 0
                        inventory_mid.parcel_amount -= 1
                        break

                # update lists of occupied and remaining parcels
                occupied_parcels.remove(parcel_id_to_remove)
                remaining_parcels.append(parcel_id_to_remove)

        inventory_mid.total_costs = inventory_mid.calculate_costs(constraint)

        # compare output inventory of random_algorithm.parcel_amount with earlier parcel_amount
        inventory_post = fillitup.fill_it_up(inventory_mid, constraint)

        # continue with hillclimber output if more parcels than before
        if inventory_post.parcel_amount > inventory_pre.parcel_amount:
            solutions.append(deepcopy(inventory_post))
            best_inventory = inventory_post

        # continue with hillclimber output if same amount of parcels but cheaper
        elif inventory_post.parcel_amount == inventory_pre.parcel_amount and inventory_post.total_costs < inventory_pre.total_costs:
            solutions.append(deepcopy(inventory_post))
            best_inventory = inventory_post

        else:
            # changes for simulated annealing
            temp = annealinghelper.decrease_temperature(maxTemp, repetitions, current_repetition)
            acceptance_chance = annealinghelper.calculate_acceptance_chance(inventory_pre.total_costs, inventory_post.total_costs, temp)
            print("ac", acceptance_chance)
            acceptance_request = random.uniform(0, 1)
            print("ar", acceptance_request)
            print(acceptance_request)
            if acceptance_request <= acceptance_chance:
                best_inventory = inventory_post
                print("accept")
            else:

                # de regel hieronder moet bij sim ann een tabje naar voren
                best_inventory = inventory_pre
                print("reject")

        # deze mag weg als geen sim ann
        current_repetition += 1

    return solutions
