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
    first_vertices = f"{x0} {y0}"
    second_vertices = f"{x1} {y1}"
    third_vertices = f"{x2} {y2}"
    with open("output.txt", "w") as fid:
        fid.writelines(first_vertices)
    with open("output.txt", "a") as fid:
        fid.writelines(second_vertices)
    with open("output.txt", "a") as fid:
        fid.writelines(third_vertices)
