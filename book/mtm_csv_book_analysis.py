import re

import pandas as pd
import numpy as np


def main():
    df = pd.read_csv("book.csv", index_col="Unnamed: 0")
    # print(df)
    # print(df.describe())
    # print(df.info())

    # df = df.set_index("index")
    df.dropna(inplace=True)
    df = df.drop(columns=["detail", "img"])
    # print(df.info())
    # print(df)

    # regex
    # str = "全10本情商高就是说话让人舒服 "
    # str2 = "全10册 别输在不会表达上 沟通的艺术 微表情 微动作 心理学 别让拖延毁了你 好好说话 书籍,全10册 "
    # print(re.findall(r"[^[\d]+[册|本]]", str))
    # print(re.findall(r"[\d]+[册|本]", str2))

    # useless = df[df["title"].str.contains(r"[\d]+[册|本]", regex=True)]
    # print(useless)
    # for i in useless.index.tolist():
    #     df.drop(index=i, inplace=True)

    useful = df[~df["title"].str.contains(r"[\d]+[册|本]", regex=True)]
    # 根据评分和评价人数降序排列，取前10条数据
    useful.sort_values(by=["score", "raging_no"], ascending=False, inplace=True)
    useful = useful[:10]
    print(useful)
    # print(df)
    useful.to_csv("useful.csv")

if __name__ == '__main__':
    main()
