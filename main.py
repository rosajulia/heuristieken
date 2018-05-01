#!/usr/bin/python

import sys
from scripts import randomalgorithm
from scripts import dataloader

# furute ref: https://www.tutorialspoint.com/python/python_command_line_arguments.htm

def main():
    ship_data = "data/spacecrafts.csv"
    cargo_data = "data/CargoList1.csv"

    loaded_data = dataloader.load_data(ship_data, cargo_data)

if __name__ == "__main__":
   main()
