import unittest
import conversions_refactored


class TestConversionsRefactored(unittest.TestCase):
    def test_conversions(self):
        # tests for celsius to fahrenheit
        self.assertAlmostEqual(conversions_refactored.convert('celsius', 'fahrenheit', 3.59), 38.462, places=3)
        self.assertAlmostEqual(conversions_refactored.convert('celsius', 'fahrenheit', -1.98), 28.436, places=3)
        # tests for celsius to kelvin
        self.assertAlmostEqual(conversions_refactored.convert('celsius', 'kelvin', 15), 288.15, places=3)
        self.assertAlmostEqual(conversions_refactored.convert('celsius', 'kelvin', -12), 261.15, places=3)
        # tests for kelvin to fahrenheit
        self.assertAlmostEqual(conversions_refactored.convert('kelvin', 'fahrenheit', 15), -432.67, places=3)
        self.assertAlmostEqual(conversions_refactored.convert('kelvin', 'fahrenheit', -12), -481.27, places=3)
        # tests for kelvin to celsius
        self.assertAlmostEqual(conversions_refactored.convert('kelvin', 'celsius', 3.59), -269.56, places=3)
        self.assertAlmostEqual(conversions_refactored.convert('kelvin', 'celsius', -1.98), -275.13, places=3)
        # tests for fahrenheit to kelvin
        self.assertAlmostEqual(conversions_refactored.convert('fahrenheit', 'kelvin', 15), 263.706, places=3)
        self.assertAlmostEqual(conversions_refactored.convert('fahrenheit', 'kelvin', -12), 248.706, places=3)
        # tests for fahrenheit to celsius
        self.assertAlmostEqual(conversions_refactored.convert('fahrenheit', 'celsius', 3.59), -15.78333, places=3)
        self.assertAlmostEqual(conversions_refactored.convert('fahrenheit', 'celsius', -1.98), -18.87778, places=3)

        # test for yards to miles
        self.assertAlmostEqual(conversions_refactored.convert('yards', 'miles', 25), 0.0142045, places=3)
        # test miles to meters
        self.assertAlmostEqual(conversions_refactored.convert('miles', 'meters', -2), -3218, places=3)

        # exception tests (misspelling, incompatible units, invalid inputs
        self.assertAlmostEqual(conversions_refactored.convert('yards', 'celsius', -12), -24.4444, places=3)
        self.assertAlmostEqual(conversions_refactored.convert('fahrenheit', 'cesius', 3.59), -15.78333, places=3)
        self.assertAlmostEqual(conversions_refactored.convert('hello', 'celsius', -1.98), -18.87778, places=3)
        # tests for same units
        self.assertAlmostEqual(conversions_refactored.convert('fahrenheit', 'fahrenheit', -1.98), -18.87778, places=3)
        self.assertAlmostEqual(conversions_refactored.convert('yards', 'yards', 5), 5, places=3)


if __name__ == '__main__':
    unittest.main()
