    # o	Simulated annealing schrijven
    #     	Toevoegen aan hillclimber:
    #         •	T (temperatuur) met decline functie
    #         •	0 en 1 zijn kosten van de pre en de post oplossing
    #         •	Als beter:
    # o	Accepteren
    #         •	Als niet beter:
    #             o	Annealing aan?
    #                 	Ja: f(0,1,T) geeft acceptatiegrens -> random getal genereren en kijken of accepted -> temperatuur aanpassen

import random
import math

def decrease_temperature(maxTemp, iterations, current_iteration):

    temp = maxTemp * current_iteration/iterations

    return temp

def calculate_acceptance_chance(previous_score, new_score, temp):

    score_difference = new_score - previous_score

    acceptance_chance = math.exp(score_difference / temp)

    return acceptance_chance


# temp = annealinghelper.decrease_temperature(temp, maxTemp, repetitions)
# acceptance_chance = annealinghelper.calculate_acceptance_chance(inventory_pre.parcel_amount, inventory_post.parcel_amount, temp)
#
# temp = annealinghelper.decrease_temperature(temp, maxTemp, repetitions)
# acceptance_chance = annealinghelper.calculate_acceptance_chance(inventory_pre.total_costs, inventory_post.total_costs, temp)
#
# maxTemp = 100
