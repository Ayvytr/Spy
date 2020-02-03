import numpy as np

if __name__ == '__main__':
    array = np.loadtxt('data', delimiter=',')
    print(array)

    # print(array.transpose())
    # print(array.swapaxes(1,0))
    # print(array.T)
    swap_array = array.swapaxes(1, 0)

    # np.savetxt('out', array, '%4d')

    # new_array = array[array > 100]
    # print(new_array)
    #
    # where_array = np.where(array > 11, True, False)
    # print(where_array)
    #
    # clip_array = np.clip(array, 10, 100)
    # print(clip_array)
    #
    # nan_array = np.isnan(array)
    # print(nan_array)
    #
    # nonzero_count = np.count_nonzero(array)
    # print(nonzero_count)

    vstack_array = np.vstack((array, swap_array))
    print(vstack_array)

    hstack_array = np.hstack((array, swap_array))
    print(hstack_array)

    eye = np.eye(3)
    print(eye)
