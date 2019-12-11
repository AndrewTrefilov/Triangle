"""Модуль с алгоритмом Сяолиня"""


def ipart(x):
    """Целая часть"""
    return int(x)


def round_(x):
    """Округляем вверх"""
    return ipart(x + 0.5)


def fpart(x):
    """Дробная часть числа"""
    return x - int(x)


def rfpart(x):
    """Вычитаем из 1 дробную часть числа"""
    return 1 - fpart(x)


def colors(yend, xgap, BRIGHTNESS):
    """Интенсивность соседних пикселей"""
    c1 = int(rfpart(yend) * xgap * BRIGHTNESS)
    c2 = int(fpart(yend) * xgap * BRIGHTNESS)
    return c1, c2


def prepare_point(x, y, gradient, pixels, steep, BRIGHTNESS):
    """Обработка конечных точек"""
    xpxl = round_(x)
    yend = y + gradient * (xpxl - x)
    xgap = rfpart(x + 0.5)
    ypxl = ipart(yend)
    c1, c2 = colors(yend, xgap, BRIGHTNESS)
    if ypxl == 499:
        if steep:
            pixels.extend([(ypxl, xpxl, 255)])
        else:
            pixels.extend([(xpxl, ypxl, 255)])
    else:
        ypxl1_plus_1 = ypxl + 1
        if steep:
            pixels.extend([(ypxl, xpxl, c1), (ypxl1_plus_1, xpxl, c2)])
        else:
            pixels.extend([(xpxl, ypxl, c1), (xpxl, ypxl1_plus_1, c2)])
    return xpxl, yend


def xiao(x0, y0, x1, y1):
    """
    Алгоритм Сяолиня

    x0, y0: координаты первой точки
    x1, y1: координаты второй точки
    """
    BRIGHTNESS = 255
    pixels = []
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        x0, y0, x1, y1 = y0, x0, y1, x1

    if x0 > x1:
        x0, x1, y0, y1 = x1, x0, y1, y0

    dx = x1 - x0
    dy = y1 - y0
    if dx == 0:
        gradient = 1
    else:
        gradient = dy / dx

    # обработать начальную точку
    xpxl0, yend = prepare_point(x0, y0, gradient, pixels, steep, BRIGHTNESS)
    intery = yend + gradient

    # обработать конечную точку
    xpxl1, _ = prepare_point(x1, y1, gradient, pixels, steep, BRIGHTNESS)

    # основной цикл
    for x in range(xpxl0 + 1, xpxl1 - 1):
        ipart_intery = ipart(intery)
        if ipart_intery == 499:
            if steep:
                pixels.extend([(ipart(intery), x, 255)])
            else:
                pixels.extend([(x, ipart(intery), 255)])
        else:
            ipart_intery_plus_1 = ipart_intery + 1
            if steep:
                pixels.extend(
                    [
                        (ipart(intery), x, int(rfpart(intery) * BRIGHTNESS)),
                        (ipart_intery_plus_1, x, int(fpart(intery) * BRIGHTNESS)),
                    ]
                )
            else:
                pixels.extend(
                    [
                        (x, ipart(intery), int(rfpart(intery) * BRIGHTNESS)),
                        (x, ipart_intery_plus_1, int(fpart(intery) * BRIGHTNESS)),
                    ]
                )
        intery += gradient
    return pixels
