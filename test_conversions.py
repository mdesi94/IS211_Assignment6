import unittest
import conversions


class TestConversions(unittest.TestCase):
    # Testing conversion of different values from celsius to Kelvin
    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(10.0), 283.15)
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(-5.0), 268.15)
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(592.8), 865.95)
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(5000), 5273.15)
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(0), 273.15)

    # Testing conversion of different values from celsius to Fahrenheit
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(56.9), 134.42)
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(.023), 32.0414)
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(-18.9), -2.02)
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(2000), 3632)
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(0), 32)

    # Testing conversion of Fahrenheit to Kelvin
    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(6.95), 259.2333, places=3)
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(0.895), 255.86944, places=3)
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(-10.6), 249.4833, places=3)
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(2000), 1366.483, places=3)
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(0), 255.372, places=3)

    # Testing conversion of Fahrenheit to Celsius
    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(6.95), -13.916667, places=3)
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(0.895), -17.280556, places=3)
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(-10.6), -23.66667, places=3)
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(2000), 1093.333, places=3)
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(0), -17.7778, places=3)

    # Testing conversion of Kelvin to Fahrenheit
    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(6.95), -447.16, places=3)
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(0.895), -458.059, places=3)
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(-10.6), -478.75, places=3)
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(2000), 3140.33, places=3)
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(0), -459.67, places=3)

    # Testing conversion of Kelvin to Celsius
    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(6.95), -266.2, places=3)
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(0.895), -272.255, places=3)
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(-10.6), -283.75, places=3)
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(2000), 1726.85, places=3)
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(0), -273.15, places=3)


if __name__ == '__main__':
    unittest.main()
