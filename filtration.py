import numpy as np


def r_0(raw_img):
    point_1, point_2 = np.zeros(2), np.zeros(2)
    point_1[1] = np.where(raw_img != 0)[0][0]
    point_1[0] = np.where(raw_img != 0)[1][0]
    point_2[0] = np.where(raw_img != 0)[1][-1]
    point_2[1] = np.where(raw_img != 0)[0][-1]

    not_null = np.zeros([np.where(raw_img != 0)[0].shape[0], 2])
    for i in range(np.where(raw_img != 0)[0].shape[0]):
        not_null[i] = np.array(
            [np.where(raw_img != 0)[1][i], np.where(raw_img != 0)[0][i]]
        )

    difference = np.zeros(not_null.shape[0])
    for i in range(not_null.shape[0]):
        difference[i] = (
            np.abs(
                (point_2[1] - point_1[1]) * not_null[i][0]
                - (point_2[0] - point_1[0]) * not_null[i][1]
                + point_2[0] * point_1[1]
                - point_2[1] * point_1[0]
            )
            / ((point_2[1] - point_1[1]) ** 2 + (point_2[0] - point_1[0]) ** 2) ** 0.5
        )
    point_3 = not_null[np.argmax(difference)]

    points = np.zeros([3, 2])
    points[0] = point_1
    points[1] = point_2
    points[2] = point_3
    return (
        points[0][0],
        points[0][1],
        points[1][0],
        points[1][1],
        points[2][0],
        points[2][1],
    )


def median_filter(space, filter_size):
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
