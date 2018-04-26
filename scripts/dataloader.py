import csv

def load_data(filename):
    """Loads a csv file as an ordered dict.
    """
    with open(filename) as csv_data:
        reader = csv.DictReader(csv_data)
        dict_data = [r for r in reader]
        return dict_data
