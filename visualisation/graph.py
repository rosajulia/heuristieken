import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def barchart_parcels(results_costs, results_parcels):
    """
    Plots barchart showing results parcel-based

    Take two arguments:

        results_costs: a list of the best costs provided by the function
        best_solutions.py

        results_parcels: a list of the best parcel amounts provided by the 
        function best_solutions.py
    
    Output:
        
        a linegraph showing the distribution of the maximum parcel amount and
        costs over all solutions. On the right y-axis you can see in blue the parcel amount
        in integers, and on the left y-axis you can see the corresponding costs in US dollars.
        The blue line represents the best parcel amount over all iterations and the red line the
        corresponding costs.
        The x-axis shows the iterations.

    """
def linegraph(results_costs, results_parcels): 
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('solution number')
    ax1.set_ylabel('costs', color=color)
    ax1.plot(results_costs, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('parcels', color=color) 
    ax2.plot(results_parcels, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout() 
    plt.savefig('static/graph.png')  
    plt.close()  