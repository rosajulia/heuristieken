import matplotlib.pyplot as plt

def barchart(results):
    
    # plot solutions in histogram
    plt.hist(results, range=(0, 100), align='mid')
    plt.title = ("Solutions")
    plt.xlabel = ("Frequency")
    plt.ylabel = ("Amount of parcels")
    plt.show()