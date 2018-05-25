# Algorithms
Folder contains all our algorithms.
The algorithms used are: a greedy/random algorithm, a random algorithm, a hillclimber, and an algorithm for bin-packing variations.

## binpackingvariations.py
    Algorithm for bin packing variations that adds an additional heuristic
    for packing the ships.</br>

    Returns list of inventory objects.</br>

    Takes three arguments:</br>

        *inventory: Must contain an inventory object that contains a list
        with ship objects and a list with parcel objects that need to be
        packed.

        *packing-variation: Specify heuristic to apply in the process of
        packing ships</br>

            "first" - First-fit decreasing:</br>
            Finds the first available ship in which the parcel can be placed.
            Parcels are sorted by volume (descending).</br>
</br>
            "best" - Best-fit decreasing:</br>
            Finds the ship in which the parcel can be placed and that has the
            least volume left after placing the parcel.
            Parcels are sorted by volume (descending).</br>
</br>
            "worst" - Worst-fit decreasing:</br>
            Finds the ship in which the parcel can be placed and that has
            the most volume left after placing the parcel.
            Parcels are sorted by volume (descending).</br>
</br>
        *constraint: Specify whether to apply the diplomatic constraint in
        generating a dict_space to carry the parcels. Takes boolean.</br>
</br>
            True: Applies diplomatic constraint when generating dict_space where
            the difference in the number of ship each nation sends cannot be
            larger than 1.</br>
</br>
            False: No constraints; dict_spaces will be generated at random.</br>

        *repetitions: Specify the number of times the algorithm will run. Takes
        nonnegative integer values.

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