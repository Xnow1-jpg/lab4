import unittest
import math
import circle


class CircleTestCase(unittest.TestCase):

    def test_area_zero(self):
        """Площадь при r = 0 должна быть 0.0."""
        self.assertAlmostEqual(circle.area(0), 0.0)

    def test_area_unit_radius(self):
        """При r = 1 площадь равна pi."""
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_area_integer_radius(self):
        """Проверка площади для r = 3."""
        res = math.pi * 9
        self.assertAlmostEqual(circle.area(3), res)

    def test_area_float_radius(self):
        """Проверка площади для вещественного радиуса r = 2.5."""
        res = math.pi * 2.5 * 2.5
        self.assertAlmostEqual(circle.area(2.5), res)

    def test_perimeter_zero(self):
        """Периметр (длина окружности) при r = 0 должен быть 0.0."""
        self.assertAlmostEqual(circle.perimeter(0), 0.0)

    def test_perimeter_unit_radius(self):
        """При r = 1 длина окружности равна 2 * pi."""
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)

    def test_perimeter_integer_radius(self):
        """Проверка длины окружности для r = 5."""
        res = 2 * math.pi * 5
        self.assertAlmostEqual(circle.perimeter(5), res)

    def test_perimeter_float_radius(self):
        """Проверка длины окружности для r = 1.5."""
        res = 2 * math.pi * 1.5
        self.assertAlmostEqual(circle.perimeter(1.5), res)