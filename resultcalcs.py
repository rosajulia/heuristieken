import csv

# filename = "data/1random.csv"
# filename = "data/1randomhc.csv"
# filename = "data/1greedy.csv"
# filename = "data/1greedyhc.csv"
filename = "data/2random.csv"

with open(filename, "r") as infile:
    reader = csv.reader(infile, delimiter=",")
    next(reader, None)  # skip the headers 

    iterations = 0
    total_packages = 0
    max_packages = 0
    costs_list = []
    total_costs = 0

    for row in reader:

        iterations = int(row[8])
        total_packages += int(row[9])

        pack_temp = int(row[9])
        if pack_temp > max_packages:
            max_packages = pack_temp

        total_costs += float(row[10])

        costs_list.append(float(row[10]))
    
    print("Iterations of results: {}".format(iterations))
    print("Average packages: {}".format(total_packages / (iterations * 2)))
    print("Max packages: {}".format(max_packages))
    print("Average costs: {}".format(total_costs / (iterations * 2)))
    print("Minimum costs: {}".format(min(costs_list)))


