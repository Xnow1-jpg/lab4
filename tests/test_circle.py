import unittest
import math
import circle


# Константы
VALID_RADIUS = 5
ZERO_RADIUS = 0
NEGATIVE_RADIUS = -5
STRING_RADIUS = "five"


class CircleTestCase(unittest.TestCase):

    # 1. Положительные значения
    def test_area_positive(self):
        """Проверка площади для положительного радиуса."""
        res = circle.area(VALID_RADIUS)
        self.assertAlmostEqual(res, math.pi * VALID_RADIUS * VALID_RADIUS)

    def test_perimeter_positive(self):
        """Проверка длины окружности для положительного радиуса."""
        res = circle.perimeter(VALID_RADIUS)
        self.assertAlmostEqual(res, 2 * math.pi * VALID_RADIUS)

    # 2. Отрицательные значения (длина стороны/радиус не могут быть отрицательными)
    def test_area_negative(self):
        """Радиус не может быть отрицательным: функция должна возвращать ошибку."""
        with self.assertRaises(ValueError):
            circle.area(NEGATIVE_RADIUS)

    def test_perimeter_negative(self):
        """Радиус не может быть отрицательным: функция должна возвращать ошибку."""
        with self.assertRaises(ValueError):
            circle.perimeter(NEGATIVE_RADIUS)

    # 3. Передача строки
    def test_area_string(self):
        """Передача строки вместо числа должна вызывать TypeError."""
        with self.assertRaises(TypeError):
            circle.area(STRING_RADIUS)

    def test_perimeter_string(self):
        """Передача строки вместо числа должна вызывать TypeError."""
        with self.assertRaises(TypeError):
            circle.perimeter(STRING_RADIUS)

    # 4. Граничные значения (ноль)
    def test_area_zero(self):
        """Площадь при нулевом радиусе равна 0.0."""
        res = circle.area(ZERO_RADIUS)
        self.assertAlmostEqual(res, 0.0)

    def test_perimeter_zero(self):
        """Периметр при нулевом радиусе равен 0.0."""
        res = circle.perimeter(ZERO_RADIUS)
        self.assertAlmostEqual(res, 0.0)