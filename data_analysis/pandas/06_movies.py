import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体

    df = pd.read_csv('movies.csv')
    df = df[df['Country']=='CN']
    print(df.head(1))

    top10_data = df.groupby('City').count()['Brand'].sort_values(ascending=False)[:50]

    _x = top10_data.index
    _y = top10_data.values

    # plt.bar(range(len(_x)), _y, width=0.3, color='orange')
    plt.barh(range(len(_x)), _y, height=0.3, color='orange')
    # plt.xticks(range(len(_x)), _x, rotation=90)
    plt.yticks(range(len(_x)), _x)
    plt.show()
