    o	Simulated annealing schrijven
        	Toevoegen aan hillclimber:
            •	T (temperatuur) met decline functie
            •	0 en 1 zijn kosten van de pre en de post oplossing
            •	Als beter:
    o	Accepteren
            •	Als niet beter:
                o	Annealing aan?
                    	Ja: f(0,1,T) geeft acceptatiegrens -> random getal genereren en kijken of accepted -> temperatuur aanpassen


def decrease_temperature(temp, iterations):

    return temp

def calculate_acceptance_chance(previous_score, new_score, temp):

    return acceptance_chance
