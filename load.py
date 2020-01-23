import numpy as np


def from_pgm(img_path):
    """
    For P5
    """
    with open(img_path, "rb") as f:
        text = f.read()
        raw_img = np.fromstring(text[17:], dtype=np.uint8).reshape(500, 500)
    return raw_img


# def from_pgm(img_path):
#     """
#     For P2
#     """
#     raw_img = np.loadtxt(img_path, skiprows=3, delimiter=' ',dtype=np.uint8).reshape((500, 500))
#     return raw_img
