import unittest
from temp_conversion_tool import convert_to_celsius, convert_to_fahrenheit

class TestTemperatureConversion(unittest.TestCase):

    def test_convert_to_celsius(self):
        self.assertAlmostEqual(convert_to_celsius(32), 0.0)
        self.assertAlmostEqual(convert_to_celsius(212), 100.0)
        self.assertAlmostEqual(convert_to_celsius(98.6), 37.0, places=1)

    def test_convert_to_fahrenheit(self):
        self.assertAlmostEqual(convert_to_fahrenheit(0), 32.0)
        self.assertAlmostEqual(convert_to_fahrenheit(100), 212.0)
        self.assertAlmostEqual(convert_to_fahrenheit(37), 98.6, places=1)

if __name__ == '__main__':
    unittest.main()

