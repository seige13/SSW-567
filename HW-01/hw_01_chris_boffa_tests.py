"""
Unit tests for HW 01
"""
import unittest
from hw_01_chris_boffa import classify_triangle


class TriangleClassification(unittest.TestCase):
    """
    Unit test class
    """

    def test_classify_equilateral_triangles(self):
        """
        Test equilateral triangle
        """
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral')
        self.assertEqual(classify_triangle(10, 10, 10), 'equilateral')

    def test_classify_scalene_triangles(self):
        """
        Test scalene triangle
        """
        self.assertEqual(classify_triangle(1, 2, 3), 'scalene')
        self.assertEqual(classify_triangle(7, 6, 3), 'scalene')

    def test_classify_isosceles_triangles(self):
        """
        Test classify isosceles triangle
        """
        self.assertEqual(classify_triangle(2, 2, 3), 'isosceles')
        self.assertEqual(classify_triangle(2, 3, 3), 'isosceles')
        self.assertEqual(classify_triangle(3, 2, 3), 'isosceles')

    def test_classify_right_triangles(self):
        """
        Test classify right triangle
        """
        self.assertEqual(classify_triangle(3, 4, 5), 'right')

    def test_classify_invalid_triangle(self):
        """
        Test classify
        """
        self.assertEqual(classify_triangle(-10, -10, -10), 'Invalid Triangle')


if __name__ == '__main__':
    unittest.main()
