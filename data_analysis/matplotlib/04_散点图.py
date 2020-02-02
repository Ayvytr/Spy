from matplotlib import pyplot as plt

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体

    y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22,
           22, 22, 23]
    y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11,
            13, 12, 13, 6]

    # print(len(y_3), len(y_10))
    x_3 = range(1, 32)
    x_10 = range(51, 82)

    plt.scatter(x_3, y_3, label="3月份")
    plt.scatter(x_10, y_10, label="10月份")

    _x = list(x_3) + list(x_10)
    _xticks_labels = ["3月{}日".format(i) for i in x_3]
    _xticks_labels += ["10月{}日".format(i - 50) for i in x_10]
    plt.xticks(_x[::3], _xticks_labels[::3], rotation=45)

    plt.xlabel("时间")
    plt.ylabel("温度")
    plt.title("标题")

    plt.legend(loc='upper left')

    plt.show()
