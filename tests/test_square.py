import unittest
import square


# Константы
VALID_SIDE = 6
ZERO_SIDE = 0
NEGATIVE_SIDE = -4
STRING_SIDE = "six"


class SquareTestCase(unittest.TestCase):

    # 1. Положительные значения
    def test_area_positive(self):
        """Проверка площади для положительной стороны."""
        res = square.area(VALID_SIDE)
        res1 = VALID_SIDE * VALID_SIDE
        self.assertEqual(res, res1)

    def test_area_positive(self):
        """Проверка площади для положительной стороны."""
        res = square.area(8)
        res1 = 8 * 8
        self.assertEqual(res, res1)
    
    def test_perimeter_positive(self):
        """Проверка периметра для положительной стороны."""
        res = square.perimeter(VALID_SIDE)
        res1 = 4 * VALID_SIDE
        self.assertEqual(res, res1)

    # 2. Отрицательные значения (сторона не может быть отрицательной)
    def test_area_negative(self):
        """Длина стороны не может быть отрицательной: ожидается ValueError."""
        with self.assertRaises(ValueError):
            square.area(NEGATIVE_SIDE)

    def test_perimeter_negative(self):
        """Длина стороны не может быть отрицательной: ожидается ValueError."""
        with self.assertRaises(ValueError):
            square.perimeter(NEGATIVE_SIDE)

    # 3. Передача строки
    def test_area_string(self):
        """Передача строки вместо числа должна вызывать TypeError."""
        with self.assertRaises(TypeError):
            square.area(STRING_SIDE)

    def test_perimeter_string(self):
        """Передача строки вместо числа должна вызывать TypeError."""
        with self.assertRaises(TypeError):
            square.perimeter(STRING_SIDE)

    # 4. Граничные значения (ноль)
    def test_area_zero(self):
        """Площадь при нулевой стороне равна 0."""
        res = square.area(ZERO_SIDE)
        self.assertEqual(res, 0)

    def test_perimeter_zero(self):
        """Периметр при нулевой стороне равен 0."""
        res = square.perimeter(ZERO_SIDE)
        self.assertEqual(res, 0)