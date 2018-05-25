import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def barchart_parcels(results):
    """
    Plots barchart showing results parcel-based

    Take one argument:

        results: a list of the best Inventory instances 
        per iteration.
    
    Output:
        
        a barchart showing the distribution of the maximum parcel amount
        over all solutions. On the x-axis the frequency is displayed in 
        height of the chart, and on the y-axis you can see the parcel amount
        in integers.

    """
    # plot solutions in histogram
    plt.hist(results, color="red", align="right")
    plt.title = ("Solutions")
    plt.xlabel = ("Frequency")
    plt.ylabel = ("Amount of parcels")
    plt.savefig('static/graph_parcels.png')  
    plt.close()

def barchart_costs(results):
    print(results)
    # plot solutions in histogram
    # plt.hist(results, color="red", align="right")
    plt.plot(results)
    plt.title = ("Solutions")
    plt.xlabel = ("Frequency")
    plt.ylabel = ("Costs")
    plt.savefig('static/graph_costs.png')  
    plt.close()  
