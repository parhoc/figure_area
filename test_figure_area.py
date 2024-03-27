import math

import pytest

from figure_area import figure_area


@pytest.mark.parametrize(
    'parameters, area',
    (
        ((3, 4, 5), 6),
        ((3,), math.pi * 3**2),
    ),
)
def test_figure_area(parameters, area):
    """Проверка корректности вычисления площади."""
    assert math.isclose(figure_area(*parameters), area)


@pytest.mark.parametrize(
    'parameters',
    (
        (1, 1, 1000),  # невозможный треугольник
        (1, 2, 3, 4),  # не поддерживаемая фигура
        (1, 'a', 2),  # не числовые параметры
        (1, 2),  # не поддерживаемая фигура
        (1, 2, -1),  # отрицательная длина
    ),
)
def test_figure_area_negative(parameters):
    """Проверка, что функция обрабатывает не правильные входные данные."""
    assert figure_area(*parameters) is None
