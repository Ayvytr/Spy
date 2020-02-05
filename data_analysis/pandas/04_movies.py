import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('movies.csv')
    print(df.head(1))
    print(df.info())

    china_data = df[df['Country'] == 'CN']

    # 分组
    # grouped = china_data.groupby(by='State/Province').count()['Brand']
    # print(grouped)

    # 按照多个条件进行分组，分组结果有多个索引
    grouped = df['Brand'].groupby(by=[df['Country'], df['State/Province']]).count()
    print(grouped)
