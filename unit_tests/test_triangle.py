import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):

    def test_area(self):
        # Arrange
        side1 = 5
        side2 = 6
        side3 = 4
        expected_area = 7.5

        # Act
        actual_area = area(side1, side2, side3)

        # Assert
        self.assertEqual(actual_area, expected_area)

    def test_perimeter(self):
        # Arrange
        side1 = 5
        side2 = 6
        side3 = 4
        expected_perimeter = 15

        # Act
        actual_perimeter = perimeter(side1, side2, side3)

        # Assert
        self.assertEqual(actual_perimeter, expected_perimeter)


if __name__ == '__main__':
    unittest.main()
