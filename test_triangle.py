import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 4)
        self.assertEqual(res, 20)

    def test_perimeter(self):
        res = perimeter(3, 3, 3)
        self.assertEqual(res, 9)