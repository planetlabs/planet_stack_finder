# Author: matt0 (matt@planet.com)
# Description: Tests the functionality of stack_finder.py

import unittest
from stackfinder import geodetics


class StackFinderTest(unittest.TestCase):
    def test_arc_length_to_latitude(self):
        km = 200
        expected = 1.7966305682390429

        # Test positive km
        output = geodetics.arc_length_to_latitude(km)
        self.assertAlmostEqual(output, expected)

        # Test negative km
        output = geodetics.arc_length_to_latitude(-km)
        self.assertAlmostEqual(output, -expected)

    def test_arc_length_to_latitude_zero_km(self):
        self.assertEqual(geodetics.arc_length_to_latitude(0), 0)

    def test_change_in_longitude(self):
        latitude = 70
        km = 200
        expected = 5.254622441495266

        # Test positive latitude, positive km
        output = geodetics.change_in_longitude(latitude, km)
        self.assertAlmostEqual(output, expected)

        # Test negative latitude, positive km
        output = geodetics.change_in_longitude(-latitude, km)
        self.assertAlmostEqual(output, expected)

        # Test positive latitude, negative km
        output = geodetics.change_in_longitude(latitude, -km)
        self.assertAlmostEqual(output, -expected)

        # Test negative latitude, negative km
        output = geodetics.change_in_longitude(-latitude, -km)
        self.assertAlmostEqual(output, -expected)

    def test_change_in_longitude_zero_km(self):
        self.assertEqual(geodetics.change_in_longitude(70, 0), 0)

if __name__ == '__main__':
    unittest.main()
