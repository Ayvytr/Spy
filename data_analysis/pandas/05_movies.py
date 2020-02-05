import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('movies.csv')
    top10_data = df.groupby('Country').count()['Brand'].sort_values(ascending=False)[:10]

    _x = top10_data.index
    _y = top10_data.values

    plt.bar(range(len(_x)), _y)
    plt.xticks(range(len(_x)), _x)
    plt.show()
