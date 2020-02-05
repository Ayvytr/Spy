import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('books.csv')

    print(df.info())

    # 不同年份书的数量
    # data1 = df[pd.notnull(df["original_publication_year"])]
    # grouped = data1.groupby(by="original_publication_year").count()["title"]
    # print(grouped)

    # 不同年份书的平均评分情况
    data1 = df[pd.notnull(df["original_publication_year"])]
    grouped = data1["average_rating"].groupby(by=data1['original_publication_year']).mean()
    print(grouped)

    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体

    _x = grouped.index
    _y = grouped.values

    plt.plot(range(len(_x)), _y)
    plt.xticks(list(range(len(_x)))[::10], _x[::10].astype(int), rotation=90)
    plt.show()

