from random import shuffle
from helperscripts import updateship

def fill_it_up(inventory, constraint):
    """
    This script looks at the inventory filled by generateships,
    and fills them until they are full.

    Returns a list of objects of type Spaceship.

    Takes two arguments:

        inventory: Must contain object of type inventory.

        constraint:
            True: Setting constraint to True will generate ships given that
            nations must send an equal number of ships. The difference in the
            number of ships each nation sends cannot be larger than one.

            False: Setting constraint to False will disregard any diplomatic
            constraints and will generate a fleet of ships at random.
    """

    dict_space = inventory.dict_space
    dict_parcel = inventory.dict_parcel
    parcel_amount = inventory.parcel_amount

    amount_remaining_parcels = 0
    remaining_parcel_indices = []
    for parcel in dict_parcel:
        if parcel.location is 0:
            amount_remaining_parcels += 1
            remaining_parcel_indices.append(dict_parcel.index(parcel))

    shuffle(remaining_parcel_indices)

    parcel_cursor = 0
    for _ in range(amount_remaining_parcels):
        parcel_cursor_counter = 0
        for ship in dict_space:
            if parcel_cursor >= amount_remaining_parcels:
                break
            else:
                index  = remaining_parcel_indices[parcel_cursor]
                if (ship.current_weight + dict_parcel[index].weight <= ship.max_weight and \
                        ship.current_volume + dict_parcel[index].volume <= ship.max_volume):

                    ship = updateship.update_ship(ship, dict_parcel[index], "+")

                    dict_parcel[index].location = ship.id
                    parcel_cursor += 1
                    parcel_cursor_counter += 1
                    parcel_amount += 1

                else:
                    continue
        if parcel_cursor_counter is 0:
            parcel_cursor += 1

    inventory.parcel_amount = parcel_amount
    inventory.total_costs = inventory.calculate_costs(constraint)

    return inventory
