import unittest
from GeometryLibPy import Triangle
from GeometryLibPy import Circumference


class TriangleTestCase(unittest.TestCase):
    def setUp(self):
        self.triangle_1 = Triangle([15, 9, 7])
        self.triangle_2 = Triangle([5, 6, 7])
        self.right_angled_triangle = Triangle([3, 4, 5])
        self.max_delta = 0.01

    def test_area_triangle(self):
        self.assertAlmostEqual(20.69, self.triangle_1.get_area(),places=None,
                               msg='incorrect area', delta=self.max_delta)

        self.assertAlmostEqual(14.69, self.triangle_2.get_area(), places=None,
                               msg='incorrect area', delta=self.max_delta)

    def test_right_rule(self):
        self.assertTrue(self.right_angled_triangle.is_right_triangle(),
                        "incorrect right rule")

        self.assertTrue(not self.triangle_1.is_right_triangle(),
                        "incorrect right rule")

    def test_resize_triangle(self):
        self.triangle_1.update_sides([5, 6, 7])
        self.assertAlmostEqual(14.69, self.triangle_1.get_area(), places=None,
                               msg='incorrect resizing method', delta=self.max_delta)


class CircumferenceTestCase(unittest.TestCase):
    def setUp(self):
        self.circle = Circumference(5)
        self.max_delta = 0.01

    def test_area_circumference(self):
        self.assertAlmostEqual(78.53, self.circle.get_area(),
                               places=None,
                               msg='incorrect area',
                               delta=self.max_delta)

    def test_resize_circumference(self):
        self.circle.update_radius(4)
        self.assertAlmostEqual(50.27, self.circle.get_area(),
                               places=None,
                               msg='incorrect resizing method',
                               delta=self.max_delta)