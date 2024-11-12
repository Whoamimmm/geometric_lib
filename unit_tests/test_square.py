import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test_area(self):
        # Arrange
        side = 5
        expected_area = 25

        # Act
        actual_area = area(side)

        # Assert
        self.assertEqual(actual_area, expected_area)

    def test_perimeter(self):
        # Arrange
        side = 5
        expected_perimeter = 20

        # Act
        actual_perimeter = perimeter(side)

        # Assert
        self.assertEqual(actual_perimeter, expected_perimeter)


if __name__ == '__main__':
    unittest.main()
