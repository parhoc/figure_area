import math
from typing import Callable, Iterable

INPUT_MASSAGE = 'Введите длины сторон фигуры через пробелы\n'


def circle_area(radius: float) -> float:
    """
    Высчитывает площадь круга по формуле `S = pi * radius**2`.

    Parameters
    ----------
    radius : float
        Радиус круга.

    Returns
    -------
    area : float
    """
    return math.pi * radius**2


def is_circle(parameters: Iterable) -> bool:
    """
    Проверяет возможен ли круг с данными параметрами.

    Параметры круга должны содержать только радиус.

    Parameters
    ----------
    parameters : iterable
        Параметры для проверки.

    Returns
    -------
    bool
    """
    return len(parameters) == 1


def is_triangle(parameters: Iterable) -> bool:
    """
    Проверяет возможен ли треугольник с данными параметрами.

    Фигура является треугольником если суммы любых двух сторон больше
    чем третья сторана.

    Parameters
    ----------
    parameters : iterable
        Параметры для проверки.

    Returns
    -------
    bool
    """
    return (len(parameters) == 3
            and parameters[0] + parameters[1] > parameters[2]
            and parameters[0] + parameters[2] > parameters[1]
            and parameters[1] + parameters[2] > parameters[0])


def triangle_area(a: float, b: float, c: float) -> float:
    """
    Высчитывает площадь треугольника по формуле Герона.

    Parameters
    ----------
    a, b, c : float
        Длины сторон треугольника.

    Returns
    -------
    area : float
    """
    s = (a + b + c)/2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


# я не понимаю зачем нужны проверка на прямоугольность треугольника,
# ведь площадь можно вычислить и без этого, но проверку можно сделать так
def is_right_triangle(a: float, b: float, c: float) -> bool:
    """
    Проверяет является ли треугольник прямоугольным на основе теоремы Пифагора.

    Parameters
    ----------
    a, b, c : float
        Длины сторон треугольника.

    Returns
    -------
    bool
    """
    catheti = [a, b, c]
    hypotenuse = max(catheti)
    catheti.remove(hypotenuse)
    return math.isclose(hypotenuse**2, catheti[0]**2 + catheti[1]**2)


# Пары функций площади и соответствующей проверки типа фигуры
FIGURE_FUNCTIONS = (
    (circle_area, is_circle),
    (triangle_area, is_triangle),
)


def get_area_function(parameters: Iterable) -> Callable:
    """
    Возвращает функцию площади основываясь на параметрах.

    Parameters
    ----------
    parameters : iterable
        Параметры фигуры.

    Returns
    -------
    area_function : callable
    """
    for area_function, validation_function in FIGURE_FUNCTIONS:
        if validation_function(parameters):
            return area_function


def figure_area(*parameters: float) -> float | None:
    """
    Высчитывате площадь фигуры.

    Требуемые параметры зависят от фигуры:
    * круг: радиус;
    * треугольник: три стороны.

    Parameters
    ----------
    *parameters : float
        Параметры фигуры.

    Returns
    -------
    area : float | None
        Возвращет None если даны не верные параметры.
    """
    if not parameters:
        return
    try:
        if min(parameters) < 0:
            print('Длина не может быть отрицательной')
            return
    except TypeError:
        print('Все параметры должны быть числами')
        return
    area_function = get_area_function(parameters)
    if area_function is None:
        print('Невозможно определить тип фигуры')
        return
    return area_function(*parameters)


if __name__ == '__main__':
    parameters = [float(side) for side in input(INPUT_MASSAGE).split()]
    print(figure_area(*parameters))
