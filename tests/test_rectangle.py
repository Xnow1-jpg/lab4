import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        """Площадь при одной или двух нулевых сторонах должна быть 0."""
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area_unit_sides(self):
        """При a = 1 и b = 1 площадь равна 1."""
        res = rectangle.area(1, 1)
        self.assertEqual(res, 1)

    def test_area_integer_sides(self):
        """Проверка площади для целочисленных сторон a = 10, b = 5."""
        res = rectangle.area(10, 5)
        self.assertEqual(res, 10 * 5)

    def test_area_square(self):
        """Проверка площади квадрата a = b = 10."""
        res = rectangle.area(10, 10)
        self.assertEqual(res, 10 * 10)

    def test_perimeter_zero(self):
        """Периметр при a = 0 и b = 0 должен быть 0."""
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_unit_sides(self):
        """При a = 1 и b = 1 периметр равен 4."""
        res = rectangle.perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_perimeter_integer_sides(self):
        """Проверка периметра для целочисленных сторон a = 10, b = 5."""
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 2 * (10 + 5))