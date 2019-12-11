from draw_triangle import draw_triangle, add_noise
from save import to_pgm
import sys

if __name__ == "__main__":
    if sys.argv[1] == "-generate":
        to_pgm(add_noise(draw_triangle(), float(sys.argv[2])))
