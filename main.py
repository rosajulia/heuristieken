#!/usr/bin/python

import sys
from scripts import randomalgorithm
from scripts import dataloader

# furute ref: https://www.tutorialspoint.com/python/python_command_line_arguments.htm

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py integer")
        sys.exit(1)
    
    ship_data = "data/spacecrafts.csv"
    cargo_data = "data/CargoList1.csv"

    loaded_data = dataloader.load_data(ship_data, cargo_data)
    amount_list = []
    
    for i in range(int(sys.argv[1])):
        amount_list.append(randomalgorithm.random_algorithm(loaded_data[0], loaded_data[1]))
        print("Amount of packages stored: ", end="") 
        print(amount_list)

if __name__ == "__main__":
   main()
