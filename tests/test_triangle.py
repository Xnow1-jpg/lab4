import unittest
import triangle


class TriangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        """Площадь при нулевой стороне или высоте должна быть 0."""
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area_unit_sides(self):
        """При a = 1 и h = 1 площадь равна 0.5."""
        res = triangle.area(1, 1)
        self.assertEqual(res, (1 * 1) / 2)

    def test_area_integer_sides(self):
        """Проверка площади для целочисленных значений a = 10, h = 5."""
        res = triangle.area(10, 5)
        self.assertEqual(res, (10 * 5) / 2)

    def test_perimeter_zero(self):
        """Периметр при a = 0, b = 0 и c = 0 должен быть 0."""
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_unit_sides(self):
        """При a = 1, b = 1 и c = 1 периметр равен 3."""
        res = triangle.perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_perimeter_integer_sides(self):
        """Проверка периметра для целочисленных сторон a = 3, b = 4, c = 5."""
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 3 + 4 + 5)