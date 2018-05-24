Clean To do list:
-	Readme:
    # o	Defaults aangeven in overzichtje
    # o	Requirements.txt maken
    o	Ergens ff melden dat we html5 gebruiken (meer van dit soort dingen?)
        - in readme bij visualisatie doen (voor elk mapje readme maken)
    o	Upper en lower bounds (en state space?) ergens noemen
        - VRAGEN AAN BRAM MORGEN OF DAT MOET
    o	Aangeven voor welke subcases je welke command line arguments moet aanroepen (misschien zo doen dat je gewoon kan kopieëren?)
    o	Per algoritme een beschrijving van wat het doet
        - in readme bij elk mapje doen
    # o	Other mapje weggooien (?)
    o	Mapje experimentatie aanmaken”
        	Een beschrijving van het experiment/onderzoeksvraag
        	Grafiekjes
        	Conclusie die je eruit trekt
    o	Scripts mapje opdelen:
        	Dingen die voorbereidend zijn
        	Dingen die tijdens de algoritmes gebruikt worden

-	Code:
    o	Greedy opschonen naar kleinere functies
    o	Greedy checken op correcte scores
    o	Random opschonen naar kleinere functies
    o	Binpack opschonen naar kleinere functies?
    o	Alle andere ff bekijken
    o	Style:
        	Snakecase functienamen
        	[“ eruit voor .
        	== eruit voor is
        	Docstrings inhoudelijk checken
        	Docstrings aanvullen
        	Comments toevoegen/aanvullen/aanpassen
    o	Keuze laten maken voor wel of geen visualisatie
    o	Keuze laten maken voor wel of niet naar csv schrijven
    o	Reset functies verplaatsen van helpers naar inventory class
        	Aanroepen aanpassen
        	Readme aanpassen

-	Verder:
    o	Schip zonder lading (weight = 0) niet meerekenen in de kosten
        	Alleen als politieke constraint het toelaat
        	Eventueel 50 van allemaal aanmaken en dan steeds lege weggooien ipv nu “op maat aanmaken” in generateships
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
