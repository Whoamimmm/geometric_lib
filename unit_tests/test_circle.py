import unittest
from circle import area, perimeter


class TestCircle(unittest.TestCase):

    def test_area(self):
        # Arrange
        radius = 5
        expected_area = 78.53981633974483

        # Act
        actual_area = area(radius)

        # Assert
        self.assertEqual(actual_area, expected_area)

    def test_perimeter(self):
        # Arrange
        radius = 5
        expected_perimeter = 31.41592653589793

        # Act
        actual_perimeter = perimeter(radius)

        # Assert
        self.assertEqual(actual_perimeter, expected_perimeter)


if __name__ == '__main__':
    unittest.main()
