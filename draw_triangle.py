"""Модуль для отрисовки треугольника и добавления шума"""

import random
import numpy as np
from xiao import xiao
from generate_verices import exam_vertices


def draw_triangle():
    """Отрисовка треугольника"""
    space = np.zeros([500, 500], dtype="uint8")
    vertices = exam_vertices()
    pairs_of_vertices = ((0, 1, 2, 3), (0, 1, 4, 5), (2, 3, 4, 5))
    for x0, y0, x1, y1 in pairs_of_vertices:
        pixels = xiao(vertices[x0], vertices[y0], vertices[x1], vertices[y1])
        for x, y, color in pixels:
            space[x, y] = color
    print(vertices)  # Потом удалить!!!!
    return space


def add_noise(space, P):
    """Добавление шума к изображению"""
    if P == 0:
        return space
    for x in range(500):
        for y in range(500):
            if random.uniform(0, 1) <= P:
                noise = random.randint(0, 255)
                space[x, y] = noise
    return space
