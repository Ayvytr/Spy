from matplotlib import pyplot as plt
from matplotlib import font_manager

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体

    # y1: 小明
    # y2: 小花
    y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
    y2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    x = range(11, 31)

    # plt.figure(figsize=(20, 8), dpi = 80)

    plt.plot(x, y1, label="小明", color='red', linestyle=':')
    plt.plot(x, y2, label="小花", color='purple', linestyle='--')

    _xtick_labels = ["{}岁".format(i) for i in x]
    plt.xticks(x, _xtick_labels)
    plt.yticks((range(0, 9)))

    plt.title("小明，小花男女朋友走势表")

    plt.xlabel("年龄")
    plt.ylabel("男/女朋友个数")

    plt.grid(alpha=0.5, linestyle=':')

    plt.legend(loc='upper left')

    plt.show()
