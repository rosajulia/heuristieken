# Heuristieken
Rebecca de Feijter, Jesse Haenen, Julia Jelgerhuis <br />
Case: Space Freight <br />
http://heuristieken.nl/wiki/index.php?title=Space_Freight

## Main goal
Ship parcels to the International Space Station (ISS) using 4 spacecrafts.
Divide the parcels over the different ships to make it as cost efficient as possible.

## Structure of repository
Our repository consists of the following folders:
* Data: here you can find our cargolists and features of the spaceships
* Scripts: the algorithms
* Classes: here the spaceships classes are stored
* Calculations: calculation important for our algorithms are stored here
* Other: other files, like our to do list + division of tasks.

* Repository also contains a main.py file that will be used to run the program
  and call all other files

# Use of program
For data visualisation installing matplotlib is required (pip install matplotlib).
Usage of main.py: please add the amount of solutions you want to try as a command-line argument (integer). 
Output of main.py: a histogram showing the frequencies of the maximum amount of parcels per solution. 

Main.py loads data through scripts/dataloader.py and calculates solutions using scripts/randomalgorithm.py.
Dataloader uses classes/classes.py and data/CargoList1.csv & data/spacecrafts.csv.
