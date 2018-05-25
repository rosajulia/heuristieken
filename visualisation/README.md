# Visualisation
Folder contains all files responsible for the visualisation of our results. 
The visualisation of our project is both web-based as print-statement based, and will only show the best solutions of an iteration.

## best_solutions.py
In best_solutions.py, the best solution of an iteration is calculated.
This is done by selecting the solution with the highest amount of parcels stored,
and finding the lowest costs with this solution. Furthermore, the graph function is called here,
with all costs and all parcel amounts. Print statements show this results.</br>
* Input: solutions: a list containing all solutions as Inventory
        class provided by the algorithm which was run. An exception on the rule
        is when the hillclimber is run, then solutions will only show the improved
        solutions when compared to the solutions ran with the normal algorithms. <br/>
* Output: print statements in the terminal showing the highest parcel amount and lowest corresponding costs. Function returns a tuple containing the best solution from all the solutions (result), with the corresponding parcel amount and costs.

## graph.py
In this function, a linegraph of costs and parcel amounts is initialised. This graph is made by using matplotlib as library.
Matplotlib is used with an non-interactive backend, Agg, because we use png's to store our graphs (ref: https://matplotlib.org/faq/howto_faq.html).
The graph is stored in an png and will eventually be loaded into our html visualisation.

## visual.py
Generates a dict containing the information needed for our html file. The dict stores the weight, volume, parcel amount, and parcel id of 
the best solution per ship, with help from a helper function called visualizeParcelsPerShip in helpers.py.
The function returns the dict. 

## visual.html & terminal.html
The html file for our visualisation. Jinja2 is used, because we use a Flask-based web environment. With help of Jinja, progress bars per ship are generated with the corresponding weight and volume percentages. Two tables are displayed, one showing the total results (parcel-, and cost-wise) and a table showing the weight, volume, parcel amount, and parcels per ship. Terminal.html shows the same, without the progress bars, because here we use more ships than 4. 

## writeresults.py
This script writes results to a csv file. A result is defined as a fleet 
    with a parcel distribution. It logs all command line arguments that are used
    for that run of the program and its results. It outputs a results.csv file in the data folder.

