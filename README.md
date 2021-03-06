# Heuristieken
Rebecca de Feijter, Jesse Haenen, Julia Jelgerhuis <br />
Case: Space Freight <br />
http://heuristieken.nl/wiki/index.php?title=Space_Freight </br>

# Main goal
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
* Algorithms: this is where our handwritten algorithms reside. Algorithms in this folder are: a random algorithm, a combinatorial greedy/random algorithm, a hillclimber, and an algorithm for binpacking variations.
* Helperscripts: the algorithms residing here are used to support the algorithms. In this folder you will find helper.py, in which several smaller functions are defined, and fillitup and updateship, which are used for the packing of the ships.
* Prepscripts: the functions in this folder play a role in the preparation of the fleet before the algorithms are ran. Generateships and shiploader are both files responsible for the generation of a fleet. Shipcost and upperbounds are functions important for the visualisation function writeresults.py.
* Calculations: calculations of for example the upper and lower bound of our score function (costs) are stored here.
* Visualisation: this folder contains our visualisation functions, graph.py supports a concise 
  visualisation of the outcome of the algorithms and visual.html, visual.py, visual.css, and terminal.html are used for a more elaborate visualisation.
 * Static: a folder requested by the Flask web application to store images. Graph.py will save the graph in this folder, which will later be used for html visualisation. 
You can see the readme's in the seperate folder for more information about the files residing there. 

## Questions and commands of case
The case Space Freight came with several questions to test your code. Below you will find these questions with their corresponding command line arguments. </br>
* a. Cargolist 1 with 4 ships (focus on parcel amount) --> python main.py 
* b. Cargolist 1 with 4 ships (focus on costs) --> python main.py 
* c. Cargolist 2 with 4 ships --> python main.py -c 2      
* d. Cargolist 3 with more ships (political constraints) --> python main.py -c 3 -s -p 
* e. Cargolist 3 with more ships (no political constraints) --> python main.py -c 3 -s </br>
Optional: *algorithms* and *hillclimber* are optional arguments, see Use of program to check the arguments.

# Use of program
**Input**<br />
Usage: main.py [-h] [-c [int]] [-s] [-p] [-a [str]] [-b [str]] [-hc] [-hci [int]] [-i [i]]<br />
<br />
Calculate the optimal organisation of a cargolist in spaceships<br />
<br />
optional arguments:<br />
  -h, --help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;show this help message and exit<br />
  -c, -cargo &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cargolist: 1, 2, 3 [int][default: 1]<br />
  -s, -ships &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use more ships than 4<br />
  -p, -politics &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use political constraints<br />
  -a, -algorithms &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;which algorithm: greedy, random, or bin [str][default: greedy]<br />
  -b, -bin_variation&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bin-packing variation: first, best, or worst [str][default: first]<br />
  -hc, -hillclimber&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use hillclimber<br />
  -hci, -hc_iterations&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hillclimber iterations: [int][default: 20]<br />
  -i, -iterations &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iterations [int][default: 5]<br />
  -w, -write_csv &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;write results to csv<br />
<br />
*Cargo* specifies which cargolist will be used to fill the ships. The *cargo* argument must be 1, 2 or 3. The default value for *cargo* is 1. <br />
*Ships* will determine whether a fixed amount of 4 ships will be used or whether an infinite amount of other ships can be purchased. There is no argument for *ships*, it will return true when called. <br />
*Politics* will specify if there are any political constraints to keep in consideration when running the code. This argument is only relevant when purchasing more ships than 4, so when argument *ships* is 'yes'. The *politics* argument takes no arguments and will return true when called. <br />
*Algorithms* will decide which algorithm is used to pack the ships as efficient as possible. The two options are a greedy algorithm and a random algorithm. *Algorithms* takes a string as argument: 'greedy' or 'random'. Default value for *algorithms* is greedy.<br />
*Bin variation* will pick a form a the bin-packing variation: first, best, or worst. Takes these three words as input argument. Default value for *bin_variation* is first.
*Hillclimber* specifies whether the extra hillclimber algorithm will be used in addition to the algorithms specified by *algorithms*. It takes no argument as input and will return true when called.<br />
*Hillclimber iterations* will determine how many times the hillclimber algorithm will run. It takes an integer as argument, with a default value of 20.<br />
*Iterations* will determine how many times the algorithms are run. It takes an integer as argument, with a default value of 5.<br />
*Write* will specify whether the results will be written to a csv file. *Write* will take no input arguments and will return true when called.<br/>
<br />
**Output**<br />
The output of the program will be mainly visualised in a Flask-based html server. The output will show the best solution provided. When the *ships* argument is 'no', progress bars will show how full all 4 ships are based on mass and volume. A table for all ships will be provided, showing which parcels are in the ships. A total result table will show how many parcels in total are packed and what the costs are for this solution. When *ships* argument is 'yes', only the two tables are provided. <br />
<br />
In addition to the web-based visualisation, a graph computed by matplotlib will show the distribution of the solutions in a histogram.

# Structure of main.py
- determine and check command-line arguments
- import csv's and create class (Parcel, Spaceship, Inventory) objects (-> csv's, dataloader.py & classes.py)
- call algorithm of choice (-> randomalgorithm.py/ greedyratio.py/ hillclimber.py)
- process outcome of algorithm and find best solution
- output information about best solution and visualisation
