import matplotlib
from matplotlib import pyplot

if __name__ == '__main__':
    x = range(0, 20, 2)
    temperature = [15, 30, 20, 22, 50, 10, 13, 16, 40, 39]

    # 设置图片大小
    # pyplot.figure(figsize=(16,9), dpi=80)

    # x轴刻度
    pyplot.xticks(range(0, 20, 5))

    pyplot.yticks(range(min(temperature), max(temperature) + 1, 5))

    # 绘制
    pyplot.plot(x, temperature)

    # 保存
    pyplot.savefig('plot')

    pyplot.show()
