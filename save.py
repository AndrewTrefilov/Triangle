import numpy as np

# def to_pgm_P5(space):
#     handle = open("image.pgm", "wb")
#     pgmHeader = "P5" + "\n" + str(500) + "  " + str(500) + "  " + str(255) + "\n"
#     handle.write(pgmHeader.encode())
#     space.tofile(handle)


def to_pgm(space):
    handle = open("image.pgm", "wb")
    pgmHeader = "P2" + "\n" + str(500) + " " + str(500) + "\n" + str(255) + "\n"
    np.savetxt('image.pgm', space, header=pgmHeader, newline=' ', comments='', delimiter=' ', fmt='%d')


def save_output(x0, y0, x1, y1, x2, y2):
    vertices = [f"{x0:.3f} {y0:.3f}\n",
                f"{x1:.3f} {y1:.3f}\n",
                f"{x2:.3f} {y2:.3f}"]
    with open("output.txt", "w") as file:
        file.writelines(vertices)
