__author__ = 'Michael Nowakowski and Joshua Shi'

import unittest
import homework6


class GerrymanderTest(unittest.TestCase):
    def test_empty(self):
        u_list = [(0, 0)]
        self.assertEqual(homework6.gerrymander(u_list), False)


    def test_basic(self):
        u_list = [(12, 30), (24, 48), (30, 10), (42,5)]
        a = [12, 24, 30, 42]
        b = [30, 48, 10, 5]
        self.assertEqual(homework6.gerrymander(u_list), True)

    def test_advanced(self):
        u_list = [(12, 30), (24, 48), (30, 10), (42, 5), (52, 5), (7, 0)]
        self.assertEqual(homework6.gerrymander(u_list), False)