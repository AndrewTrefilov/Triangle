def to_pgm(space):
    handle = open("image.pgm", "wb")
    pgmHeader = "P5" + "\n" + str(500) + "  " + str(500) + "  " + str(255) + "\n"
    handle.write(pgmHeader.encode())
    space.tofile(handle)
