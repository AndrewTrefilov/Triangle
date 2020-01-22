import numpy as np


def median_filter(space, filter_size=None):
    count_black = space[space == 0].shape[0] / 250000

    if count_black > 0.581 and count_black < 0.68:
        filter_size = 7
    elif count_black > 0.681 and count_black < 0.78:
        filter_size = 5
    elif count_black > 0.781 and count_black < 0.98:
        filter_size = 3
        
    if filter_size is None:
        return space
    indexer = filter_size // 2
    median = (filter_size * filter_size) // 2

    filter_space = np.zeros([500, 500], dtype="uint8")

    list_coor = range(0, 500 - 2 * indexer)
    list_filtersize = range(filter_size)

    for x in list_coor:
        x_plus_indexer = x + indexer
        for y in list_coor:
            temp = []
            for fx in list_filtersize:
                x_plus_fx = x + fx
                for fy in list_filtersize:
                    temp.append(space[x_plus_fx, y + fy])
            temp.sort()
            filter_space[x_plus_indexer, y + indexer] = temp[median]
    return filter_space
