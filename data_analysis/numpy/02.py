import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # array = np.arange(10)
    # print(array)

    # print(np.sqrt(array))
    # print(np.exp(array))

    points = np.arange(-5, 5, 0.01)
    print(points)
    xs, ys = np.meshgrid(points, points)
    # print(xs)
    # print(ys)

    z = np.sqrt(xs ** 2, ys ** 2)
    print(z)

    plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()

    plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
    plt.show()