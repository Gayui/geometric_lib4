import unittest
import math
from circle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(4)
        self.assertEqual(res, math.pi * 16)

    def test_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, math.pi * 4)