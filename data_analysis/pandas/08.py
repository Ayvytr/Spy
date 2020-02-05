import pandas as pd

if __name__ == '__main__':
    dr = pd.date_range("20200101", "20200201", freq="H")
    print(dr)
