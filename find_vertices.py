from math import cos, sin
import numpy as np


def trash(accumulator, thetas, rhos):
    maxi = accumulator[np.argmax(accumulator, axis=0), np.arange(180)]
    max_split_idx = np.zeros(6, dtype=int)
    for idx, array in enumerate(np.array_split(maxi, 6)):
        max_split_idx[idx] = idx * 30 + np.argmax(array)
    max_split_idx = max_split_idx[(maxi[max_split_idx]).argsort()[-3:]]
    max_count = maxi[max_split_idx][(maxi[max_split_idx]).argsort()[-3:]]
    
    thetas_0 = thetas[max_split_idx[0]]
    thetas_1 = thetas[max_split_idx[1]]
    thetas_2 = thetas[max_split_idx[2]]
    
    # Добавил еще ноль, так как соседние ро могут быть одинаковые o_O
    rhos_0 = float(
        rhos[np.where(accumulator[:, max_split_idx[0]] == max_count[0])[0]][0]
    )
    rhos_1 = float(
        rhos[np.where(accumulator[:, max_split_idx[1]] == max_count[1])[0]][0]
    )
    rhos_2 = float(
        rhos[np.where(accumulator[:, max_split_idx[2]] == max_count[2])[0]][0]
    )
    return thetas_0, thetas_1, thetas_2, rhos_0, rhos_1, rhos_2


def get_xy(rhos_first, thetas_first, rhos_second, thetas_second):
    sin_thetas_first = sin(thetas_first)
    sin_thetas_second = sin(thetas_second)

    d = rhos_first / sin_thetas_first
    c = rhos_second / sin_thetas_second
    b = -cos(thetas_first) / sin_thetas_first
    a = -cos(thetas_second) / sin_thetas_second
    x = (d - c) / (a - b)
    y = a * x + c
    return y, x


def find_vertices(accumulator, thetas, rhos):
    thetas_0, thetas_1, thetas_2, rhos_0, rhos_1, rhos_2 = trash(
        accumulator, thetas, rhos
    )
    y0, x0 = get_xy(rhos_0, thetas_0, rhos_1, thetas_1)
    y1, x1 = get_xy(rhos_1, thetas_1, rhos_2, thetas_2)
    y2, x2 = get_xy(rhos_0, thetas_0, rhos_2, thetas_2)
    return x0, y0, x1, y1, x2, y2
