# Algorithms
Folder contains all our algorithms.
The algorithms used are: a greedy/random algorithm, a random algorithm, a hillclimber, and an algorithm for bin-packing variations.

## binpackingvariations.py
In best_solutions.py, the best solution of an iteration is calculated.
This is done by selecting the solution with the highest amount of parcels stored,
and finding the lowest costs with this solution. Furthermore, the graph function is called here,
with all costs and all parcel amounts. Print statements show this results.</br>
* Input: solutions: a list containing all solutions as Inventory
        class provided by the algorithm which was run. An exception on the rule
        is when the hillclimber is run, then solutions will only show the improved
        solutions when compared to the solutions ran with the normal algorithms. <br/>
* Output: print statements in the terminal showing the highest parcel amount and lowest corresponding costs. Function returns a tuple containing the best solution from all the solutions (result), with the corresponding parcel amount and costs.

## randomalgorithm.py
 Randomly fills spaceships with a cargo list.</br>

    The first argument holds an object representing the format of a possible
    distribution of parcels over spaceships. The second argument indicates how
    often the algorithm should generate a solution.<br/>

    *Input:
            takes three input arguments: the class Inventory containing all information
            about the spaceships and parcels; the repetitions, how many iterations will be performed;
            constraint: whether or not there is a political constraint.</br>

    *Output: 
            returns a list of instances of the class Inventory, containing the solutions from 
            the algorithm. The solutions contain the total parcel amount and the costs. </br>

    Usage:</br>
    randomalgorithm.random_algorithm(inventory, repetitions, constraint)


## hillclimber.py
    Hillclimber algorithm with improves upon the solutions provided by the other algorithms.
    It accepts a new solutions when the parcel amount is higher. </br>

    *Input:
            takes three input arguments: the class Inventory containing all information
            about the spaceships and parcels; the repetitions, how many iterations will be performed;
            constraint: whether or not there is a political constraint.<.br>

    *Output: 
            returns a list of instances of the class Inventory, containing the solutions from 
            the algorithm which are better than the original provided solutions from the 
            other algorithms. The solutions contain the total parcel amount and the costs. 

    Usage: </br>
    hillclimber.hill_climber(inventory, repetitions, constraint)

## greedyratio.py
    Greedy algorithm based on the weight-to-volume ratio of spaceships and parcels,
    and the assumption that low ratio ships are suitable transport for low ratio parcels
    (and high ratio ships for high ratio parcels).</br>

    The algorithm first starts by dividing the spaceships ratio-based, using greedyhelper. 
    It will continue by filling the low-ratio spaceship and high-ratio spaceship with corresponding
    low- and high-ratio parcels. The other spaceships will be randomly filled. </br>

    *Input:
            takes three input arguments: the class Inventory containing all information
            about the spaceships and parcels; the repetitions, how many iterations will be performed;
            constraint: whether or not there is a political constraint.</br>

    *Output: 
            returns a list of instances of the class Inventory, containing the solutions from 
            the algorithm. The solutions contain the total parcel amount and the costs. </br>

    Usage: </br>
    greedyratio.greedy_ratio(inventory, repetitions, constraint)  