import unittest
from HW01ChrisBoffa import classify_triangle


class TriangleClassification(unittest.TestCase):

    def test_classify_equilateral_triangles(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral')
        self.assertEqual(classify_triangle(10, 10, 10), 'equilateral')
        self.assertEqual(classify_triangle(-10, -10, -10), 'equilateral')

    def test_classify_scalene_triangles(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'scalene')
        self.assertEqual(classify_triangle(7, 6, 3), 'scalene')

    def test_classify_isosceles_triangles(self):
        self.assertEqual(classify_triangle(2, 2, 3), 'isosceles')
        self.assertEqual(classify_triangle(2, 3, 3), 'isosceles')
        self.assertEqual(classify_triangle(3, 2, 3), 'isosceles')

    def test_classify_right_triangles(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'right')
        self.assertEqual(classify_triangle(-3, -4, -5), 'right')


if __name__ == '__main__':
    unittest.main()
