import unittest

import day04


class TestHaveOverlap(unittest.TestCase):

    def test_no_overlap(self):
        self.assertFalse(day04.have_overlap(1, 3, 4, 6))
        self.assertFalse(day04.have_overlap(1, 3, 6, 6))
        self.assertFalse(day04.have_overlap(1, 1, 2, 2))
        self.assertFalse(day04.have_overlap(1, 5, 9, 10))
        self.assertFalse(day04.have_overlap(85, 85, 77, 84))
        self.assertFalse(day04.have_overlap(20, 91, 16, 19))

    def test_have_overlap(self):
        self.assertTrue(day04.have_overlap(1, 3, 3, 6))
        self.assertTrue(day04.have_overlap(1, 1, 1, 5))
        self.assertTrue(day04.have_overlap(1, 4, 2, 5))
        self.assertTrue(day04.have_overlap(1, 4, 2, 3))
        self.assertTrue(day04.have_overlap(60, 89, 83, 90))
        self.assertTrue(day04.have_overlap(6, 21, 2, 75))
