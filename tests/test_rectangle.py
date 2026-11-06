import unittest
import rectangle


# Константы
VALID_A = 10
VALID_B = 5
ZERO_VAL = 0
NEGATIVE_VAL = -5
STRING_VAL = "10"


class RectangleTestCase(unittest.TestCase):

    # 1. Положительные значения
    def test_area_positive(self):
        """Проверка площади для корректных положительных сторон."""
        res = rectangle.area(VALID_A, VALID_B)
        self.assertEqual(res, VALID_A * VALID_B)

    def test_perimeter_positive(self):
        """Проверка периметра для корректных положительных сторон."""
        res = rectangle.perimeter(VALID_A, VALID_B)
        self.assertEqual(res, 2 * (VALID_A + VALID_B))

    # 2. Отрицательные значения (стороны не могут быть отрицательными)
    def test_area_negative(self):
        """Длина стороны не может быть отрицательной: ожидается ValueError."""
        with self.assertRaises(ValueError):
            rectangle.area(NEGATIVE_VAL, VALID_B)

    def test_perimeter_negative(self):
        """Длина стороны не может быть отрицательной: ожидается ValueError."""
        with self.assertRaises(ValueError):
            rectangle.perimeter(VALID_A, NEGATIVE_VAL)

    # 3. Передача строки
    def test_area_string(self):
        """Передача строки вместо числа должна вызывать TypeError."""
        with self.assertRaises(TypeError):
            rectangle.area(STRING_VAL, VALID_B)

    def test_perimeter_string(self):
        """Передача строки вместо числа должна вызывать TypeError."""
        with self.assertRaises(TypeError):
            rectangle.perimeter(VALID_A, STRING_VAL)

    # 4. Граничные значения (ноль)
    def test_area_zero(self):
        """Площадь при нулевой стороне равна 0."""
        res = rectangle.area(VALID_A, ZERO_VAL)
        self.assertEqual(res, 0)

    def test_perimeter_zero(self):
        """Периметр при нулевых сторонах равен 0."""
        res = rectangle.perimeter(ZERO_VAL, ZERO_VAL)
        self.assertEqual(res, 0)