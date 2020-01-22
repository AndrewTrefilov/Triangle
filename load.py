import numpy as np


# def from_pgm_P5(img_path):
#     with open(img_path, "r") as f:
#         text = f.read()
#         raw_img = np.fromstring(text[:17], dtype=np.uint8, sep=' ').reshape(500, 500)
#     print(raw_img.shape)
#     return raw_img

def from_pgm(img_path):
    raw_img = np.loadtxt(img_path, skiprows=3, delimiter=' ',dtype=np.uint8).reshape((500, 500))
    return raw_img

# def from_pgm(img_path):
#     raw_img = np.loadtxt(img_path, skiprows=3, delimiter=" ", dtype=np.uint8)
#     print(raw_ing.shape)#.reshape((500, 500))
#     return raw_img