from draw_triangle import draw_triangle, add_noise
from save import to_pgm, save_output
from load import from_pgm
from filtration import median_filter
from line_detection import hough_line
from find_vertices import find_vertices
import sys


if __name__ == "__main__":
    if sys.argv[1] == "-generate":
        to_pgm(add_noise(draw_triangle(), float(sys.argv[2])))
    if sys.argv[1] == "-restore":
        raw_img = from_pgm(sys.argv[2])
        accumulator, thetas, rhos = hough_line(median_filter(raw_img))
        y0, x0, y1, x1, y2, x2 = find_vertices(accumulator, thetas, rhos)
        save_output(y0, x0, y1, x1, y2, x2)
