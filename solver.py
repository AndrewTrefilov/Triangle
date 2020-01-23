from draw_triangle import draw_triangle, add_noise
from save import to_pgm, save_output
from load import from_pgm
from filtration import median_filter, r_0
from line_detection import hough_line
from find_vertices import find_vertices
import random
import sys


if __name__ == "__main__":
    if sys.argv[1] == "-generate":
        to_pgm(add_noise(draw_triangle(), float(sys.argv[2])))
    if sys.argv[1] == "-restore":
        raw_img = from_pgm(sys.argv[2])
        count_black = raw_img[raw_img == 0].shape[0] / 250000

        if count_black < 0.68:
            filter_size = 'random'
        # elif count_black > 0.58 and count_black < 0.68:
        #     filter_size = 9
        elif count_black > 0.68 and count_black < 0.78:
            filter_size = 5
        elif count_black > 0.78 and count_black < 0.98:
            filter_size = 3
        else:
            filter_size = None

        if filter_size is None:
            y0, x0, y1, x1, y2, x2 = r_0(raw_img)
        elif filter_size == 'random':
            y0, x0, y1, x1, y2, x2 = tuple([random.uniform(0, 499) for _ in range(6)])
        else:
            accumulator, thetas, rhos = hough_line(median_filter(raw_img, filter_size))
            y0, x0, y1, x1, y2, x2 = find_vertices(accumulator, thetas, rhos)
        save_output(y0, x0, y1, x1, y2, x2)
        # print(y0, x0, y1, x1, y2, x2)
