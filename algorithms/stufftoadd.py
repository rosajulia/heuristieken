# command-line arguments
    # welke cargolist
    # 4 of oneindig schepen
    # constraints of niet
    # welk algoritme
    # hoe vaak

# inventory
    # moet daar niet iets anders in, in classes?

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


# greedy suitable for variety of ships:
    # add ratio of ships to class
    # sort list of generated ships based on ratio
    # sort cargolist on ratio
    # consider lowest type of ship
        # loop over (or back and forth) ships of type with lowest ratio
        # fill with lowest ratio parcels
        # same for highest
        # decide whether to do the same with next lowest ratio ships and next highest ratio ships
        # randomly divide oarcels over middle ships
    # start hill climbing (or something else)

    # greedy should return an object of type inventory?
        # (random ook)
        # inventory id?


# generate random ships (considering constraint or not)
    # first couple of rounds can be looped instead of random
    # upon creating ship, fill randomly with parcels until full
    # create new ship and repeat until all parcel location != 0
    # to consider restraint: keep track of counter per nation
# either:
    # clear all parcel locations and fill again but now with greedyratio
    # or climb hill with current random outcome as starting point



# experimentatie
    # wat is invloed van ftw?
