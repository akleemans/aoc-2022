import unittest

import day25


class TestSnafu(unittest.TestCase):
    # Dec, Snafu
    test_cases = [
        ('1', '1'),
        ('2', '2'),
        ('3', '1='),
        ('4', '1-'),
        ('5', '10'),
        ('6', '11'),
        ('7', '12'),
        ('8', '2='),
        ('9', '2-'),
        ('10', '20'),
        ('15', '1=0'),
        ('20', '1-0'),
        ('2022', '1=11-2'),
        ('12345', '1-0---0'),
        ('314159265', '1121-1110-1=0'),
        ('1747', '1=-0-2'),
        ('906', '12111'),
        ('198', '2=0='),
        ('11', '21'),
        ('201', '2=01'),
        ('31', '111'),
        ('1257', '20012'),
        ('32', '112'),
        ('353', '1=-1='),
        ('107', '1-12'),
        ('37', '122'),
        ('4890', '2=-1=0'),
    ]

    def test_dec_to_snafu(self):
        for (dec, snafu) in self.test_cases:
            self.assertEqual(snafu, day25.dec_to_snafu(dec))

    def test_snafu_to_dec(self):
        for (dec, snafu) in self.test_cases:
            self.assertEqual(dec, day25.snafu_to_dec(snafu))
