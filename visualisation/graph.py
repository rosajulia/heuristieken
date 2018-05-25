import matplotlib.pyplot as plt
import os

def barchart_parcels(results):
    # plot solutions in histogram
    plt.hist(results, color="red", align="right")
    plt.title = ("Solutions")
    plt.xlabel = ("Frequency")
    plt.ylabel = ("Amount of parcels")
    plt.savefig('static/graph_parcels.png')  
    plt.close()  

def barchart_costs(results):
    # plot solutions in histogram
    plt.hist(results, color="red", align="right")
    plt.title = ("Solutions")
    plt.xlabel = ("Frequency")
    plt.ylabel = ("Costs")
    plt.savefig('static/graph_costs.png')  
    plt.close()  