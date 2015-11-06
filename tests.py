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

# class FirstEncounters(unittest.TestCase):
#     def test_empty(self):
#         homework6.first_encounters("", "", "")

    # def test_basic(self):
    #     a = "a"
    #     b = "c"
    #     c = "ac"
    #     self.assertEqual(homework6.first_encounters(a, b, c), True)
    #
    # def test_harder(self):
    #     a = "abb"
    #     b = "bc"
    #     c = "abbbc"
    #     self.assertEqual(homework6.first_encounters(a, b, c), True)
    #
    # def test_k_is_big(self):
    #     a = "abb"
    #     b = "bc"
    #     c = "abbabbabbbc"
    #     self.assertEqual(homework6.first_encounters(a, b, c), True)


class GerrymanderTest(unittest.TestCase):
    def test_empty(self):
        pass

    def test_basic(self):
        a = [12, 24, 30, 42]
        b = [30, 48, 10, 5]
        homework6.gerrymander(a, b)