import pandas as pd


def load_data(file):

    data = pd.read_csv(file, header=0)
    df = pd.DataFrame(data)

    return df


if __name__ == '__main__':

    df = load_data('../cargo_data/CargoList1.csv')

    print(df)
