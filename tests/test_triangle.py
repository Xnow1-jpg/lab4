import unittest
import triangle


# Константы
VALID_A = 3
VALID_B = 4
VALID_C = 5
VALID_H = 6
ZERO_VAL = 0
NEGATIVE_VAL = -3
STRING_VAL = "side"


class TriangleTestCase(unittest.TestCase):

    # 1. Положительные значения
    def test_area_positive(self):
        """Проверка площади для положительных основания и высоты."""
        res = triangle.area(VALID_A, VALID_H)
        self.assertAlmostEqual(res, (VALID_A * VALID_H) / 2)

    def test_perimeter_positive(self):
        """Проверка периметра для положительных сторон."""
        res = triangle.perimeter(VALID_A, VALID_B, VALID_C)
        self.assertEqual(res, VALID_A + VALID_B + VALID_C)

    # 2. Отрицательные значения (сторона и высота не могут быть отрицательными)
    def test_area_negative(self):
        """Сторона или высота не могут быть отрицательными: ожидается ValueError."""
        with self.assertRaises(ValueError):
            triangle.area(NEGATIVE_VAL, VALID_H)

    def test_perimeter_negative(self):
        """Стороны не могут быть отрицательными: ожидается ValueError."""
        with self.assertRaises(ValueError):
            triangle.perimeter(NEGATIVE_VAL, VALID_B, VALID_C)

    # 3. Передача строки
    def test_area_string(self):
        """Передача строки вместо числа должна вызывать TypeError."""
        with self.assertRaises(TypeError):
            triangle.area(STRING_VAL, VALID_H)

    def test_perimeter_string(self):
        """Передача строки вместо числа должна вызывать TypeError."""
        with self.assertRaises(TypeError):
            triangle.perimeter(VALID_A, STRING_VAL, VALID_C)

    # 4. Граничные значения (ноль)
    def test_area_zero(self):
        """Площадь при нулевой высоте равна 0.0."""
        res = triangle.area(VALID_A, ZERO_VAL)
        self.assertAlmostEqual(res, 0.0)

    def test_perimeter_zero(self):
        """Периметр при нулевых сторонах равен 0."""
        res = triangle.perimeter(ZERO_VAL, ZERO_VAL, ZERO_VAL)
        self.assertEqual(res, 0)