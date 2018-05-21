# Heuristieken
Rebecca de Feijter, Jesse Haenen, Julia Jelgerhuis <br />
Case: Space Freight <br />
http://heuristieken.nl/wiki/index.php?title=Space_Freight

## Main goal
Ship parcels to the International Space Station (ISS) using 6 different types of spacecrafts.
Divide the parcels over the different ships to make it as cost efficient as possible.

## Structure of repository
Our repository consists of the following files and folders:
* main.py: this file will run the program based on the entered command-line arguments, by calling all other files
  and functions.
* Data: here you can find csv's containing our cargolists and features of the spaceships, as well as a script 
  for loading those csv's.
* Classes: this folder contains the data structure that is the foundation of our program. Two classes - namely 
  Parcels and Spaceships - are used, as well as a class including all useful features of a suggested distribution of
  parcels over the ships; the Inventory class.
* Algorithms: this is where our handwritten algorithms reside, currently those are a random algorithm, a combinatorial greedy/random
  algorithm, and a hill climber algorithm.
* Scripts: the algorithms are supported by a series of files in this folder: graph.py supports a concise 
  visualisation of the outcome of the algorithms, visual.html is used for a more elaborate visualisation, helpers.py 
  contains several smaller functions, generateships.py & shiploader.py are used to create a varying fleet of ships.
* Calculations: calculations of for example the upper and lower bound of our score function (costs) are stored here.
* Other: other files, like our to do list + division of tasks.


# Use of program
For data visualisation installing matplotlib is required (pip install matplotlib).

At the moment:
Please add the amount of solutions you want to generate as a command-line argument (integer). 
Usage: python main.py integer
Automatically, cargolist 1 will be used and 4 ships will be generated (for which political constraint is irrelevant).
Output of main.py: a histogram showing the frequencies of the maximum amount of parcels per solution, as wel as
information in the terminal about the best solution found so far. 

Goal:
Adding more variables as command-line arguments:
- which cargolist to use
- whether only 4 ships can be used or as many as necessary
- wether political constraints should be considered
- which algorithm to use
- how often to run the algorithm (already in use)
Output: Visualisation in html with progress bars for weight and volume of ships in use for best solution found. (already working)

# Structure of main.py
- determine and check command-line arguments
- import csv's and create class (Parcel, Spaceship, Inventory) objects (-> csv's, dataloader.py & classes.py)
- call algorithm of choice (-> randomalgorithm.py/ greedyratio.py/ hillclimber.py)
- process outcome of algorithm and find best solution
- output information about best solution and visualisation
