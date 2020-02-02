import pandas

if __name__ == '__main__':
    array = pandas.Series([4, 7, -5, 3])
    # print(array)

    array2 = pandas.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
    print(array2)

    # print(array2['d'])

    print(array2[array2 > 0])

    print(array2 * 2)
