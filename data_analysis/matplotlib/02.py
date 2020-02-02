import random

from matplotlib import pyplot, font_manager
import matplotlib

if __name__ == '__main__':
    # matplotlib.rc("font", family='Microsoft YaHei')
    # font = font_manager.FontProperties(fname='c:/windows/fonts/MSYH.ttc')
    pyplot.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
    pyplot.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

    x = range(0, 120)
    y = [random.randint(-20, 40) for i in range(120)]

    pyplot.plot(x, y)

    xticks_labels = ["10点{}分".format(i) for i in range(60)]
    xticks_labels += ["11点{}分".format(i) for i in range(60)]
    pyplot.xticks(list(x)[::3], xticks_labels[::3], rotation=45)

    pyplot.figure(figsize=(20, 8), dpi=80)
    pyplot.savefig('temperature')

    pyplot.show()

