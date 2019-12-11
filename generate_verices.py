"""Модуль для генерации вершин"""

import random
from math import acos, degrees, sqrt


def generate_vertices():
    """Генерация позиций вершин треугольника"""
    return [random.uniform(0, 499) for _ in range(6)]


def get_sides(vertices):
    """Вычисление длин сторон треугольника"""
    pairs_of_vertices = ((0, 1, 2, 3), (0, 1, 4, 5), (2, 3, 4, 5))
    sides = []

    def get_side(vertices, x0, y0, x1, y1):
        return sqrt(
            (vertices[x0] - vertices[x1]) ** 2 + (vertices[y0] - vertices[y1]) ** 2
        )

    for x0, y0, x1, y1 in pairs_of_vertices:
        sides.append(get_side(vertices, x0, y0, x1, y1))
    return sides


def get_angles(sides):
    """Вычисление углов треугольника"""
    pairs_of_sides = ((0, 1, 2), (2, 1, 0), (0, 2, 1))
    angles = []

    def get_angle(sides, s_1, s_2, s_3):
        return degrees(
            acos(
                (
                    sides[s_1] * sides[s_1]
                    + sides[s_2] * sides[s_2]
                    - sides[s_3] * sides[s_3]
                )
                / (2.0 * sides[s_1] * sides[s_2])
            )
        )

    for s_1, s_2, s_3 in pairs_of_sides:
        angles.append(get_angle(sides, s_1, s_2, s_3))
    return angles


def exam_vertices():
    """Проверка сгенерированных вершин"""
    vertices = generate_vertices()
    sides = get_sides(vertices)
    angles = get_angles(sides)

    min_side = min(sides)
    min_angle = min(angles)

    while (min_side < 100) | (min_angle < 30):
        # print('bad')
        return exam_vertices()
    # print('ok')
    return vertices
