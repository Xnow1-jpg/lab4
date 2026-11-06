import unittest
import square


class SquareTestCase(unittest.TestCase):

    def test_area_zero(self):
        """Площадь при нулевой стороне должна быть 0."""
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_unit_sides(self):
        """При a = 1 площадь равна 1."""
        res = square.area(1)
        self.assertEqual(res, 1)

    def test_area_integer_sides(self):
        """Проверка площади для целочисленной стороны a = 10."""
        res = square.area(10)
        self.assertEqual(res, 10 * 10)

    def test_perimeter_zero(self):
        """Периметр при a = 0 должен быть 0."""
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_unit_sides(self):
        """При a = 1 периметр равен 4."""
        res = square.perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_integer_sides(self):
        """Проверка периметра для целочисленной стороны a = 10."""
        res = square.perimeter(10)
        self.assertEqual(res, 4 * 10)