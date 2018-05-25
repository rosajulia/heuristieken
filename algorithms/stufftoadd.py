Clean To do list:
-	Readme:

    o   volgorde iterations enzo kan logischer
    o	Upper en lower bounds (en state space?) ergens noemen
        - VRAGEN AAN BRAM MORGEN OF DAT MOET
    o	Per algoritme een beschrijving van wat het doet
        - in readme bij elk mapje doen
    o	Mapje experimentatie aanmaken”
        	Een beschrijving van het experiment/onderzoeksvraag
        	Grafiekjes
        	Conclusie die je eruit trekt

-	Code:
    o	Hillclimber checken op correcte scores
    o	Binpack opschonen naar kleinere functies?
    o	Style:
        	Snakecase functienamen
        	[“ eruit voor .
        	== eruit voor is
        	Docstrings inhoudelijk checken
        	Docstrings aanvullen
        	Comments toevoegen/aanvullen/aanpassen
    o	Keuze laten maken voor wel of niet naar csv schrijven
    o	Reset functies verplaatsen van helpers naar inventory class
        	Aanroepen aanpassen
        	Readme aanpassen

-	Verder:
    o	Schip zonder lading (weight = 0) niet meerekenen in de kosten
        	Alleen als politieke constraint het toelaat
    o	Csv verhaal aanroepen vanuit main
        	Obv command line yes or no
        	Files die nu los staan in mapje zetten
    o	Hillclimber parametriseren met verschillende aantallen pakketjes te removen
    o	Simulated annealing schrijven
        	Toevoegen aan hillclimber:
            •	T (temperatuur) met decline functie
            •	0 en 1 zijn kosten van de pre en de post oplossing
            •	Als beter:
    o	Accepteren
            •	Als niet beter:
                o	Annealing aan?
                    	Ja: f(0,1,T) geeft acceptatiegrens -> random getal genereren en kijken of accepted -> temperatuur aanpassen
    o	Experimentatie bedenken, checken bij Bram, en doen
    o   Calculations opschonen
