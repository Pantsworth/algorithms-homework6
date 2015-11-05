__author__ = 'Michael Nowakowski and Joshua Shi'

import unittest
import homework6


# class ReadingTest(unittest.TestCase):
#     def test_base_case(self):
#         days = []
#         sections = []
#         homework6.reading_weeping(days, sections)
#
#
#     def test_basic(self):
#         days = [1,2,3]
#         sections = [1,2,3]
#         homework6.reading_weeping(days, sections)

class FirstEncounters(unittest.TestCase):
    def test_empty(self):
        homework6.first_encounters("", "", "")

    def test_basic(self):
        a = "a"
        b = "c"
        c = "ac"
        self.assertEqual(homework6.first_encounters(a, b, c), True)

    def test_harder(self):
        a = "abb"
        b = "bc"
        c = "abbbc"
        self.assertEqual(homework6.first_encounters(a, b, c), True)
