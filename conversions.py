# Converts celsius temps to either kelvin or fahrenheit
def convertCelsiusToKelvin(celsius_temp):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = round(celsius_temp + 273.15, 4)
    return kelvins


def convertCelsiusToFahrenheit(celsius_temp):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = round((celsius_temp * 9/5) + 32, 4)
    return fahrenheit


# Converts fahrenheit temps to either kelvin or celsius
def convertFahrenheitToKelvin(fahrenheit_temp):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins"""
    kelvins = round((fahrenheit_temp + 459.67) * 5 / 9, 4)
    return kelvins


def convertFahrenheitToCelsius(fahrenheit_temp):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    celsius = round((fahrenheit_temp - 32) * 5 / 9, 4)
    return celsius


# Converts kelvin temps to either celsius or fahrenheit
def convertKelvinToFahrenheit(kelvin_temp):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = round(kelvin_temp * 9 / 5 - 459.67, 4)
    return fahrenheit


def convertKelvinToCelsius(kelvin_temp):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius"""
    fahrenheit = round(kelvin_temp - 273.15, 4)
    return fahrenheit
