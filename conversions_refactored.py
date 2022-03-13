class InvalidUnitError(Exception):
    def __init__(self, msg):
        self.msg = "Units entered are not compatible for conversion!"


class InvalidInputError(Exception):
    def __init__(self, msg):
        self.msg = "Input values are not recognized and cannot be converted. Please enter a valid unit."


    # *********conversion functions*********
def convert(from_unit, to_unit, value):
    # celsius to fahrenheit or kelvin
    cel_to_fahr = round((value * 9 / 5) + 32, 3)
    cel_to_kel = round(value + 273.15, 3)

    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        print(f"{value} degrees Celsius is {cel_to_fahr} degrees Fahrenheit")
        return cel_to_fahr

    elif from_unit == 'celsius' and to_unit == 'kelvin':
        print(f"{value} degrees Celsius is {cel_to_kel} degrees Kelvin")
        return cel_to_kel
    elif from_unit == 'celsius' and to_unit == 'celsius':
        print(f"{value} degrees Celsius is also {value} !")
        return value
    else:
        pass

    # fahrenheit to kelvin or celsius
    fahr_to_kel = round((value + 459.67) * 5 / 9, 3)
    fahr_to_cel = round((value - 32) * 5 / 9, 3)

    if from_unit == 'fahrenheit' and to_unit == 'kelvin':
        print(f"{value} degrees Fahrenheit is {fahr_to_kel} degrees Kelvin")
        return fahr_to_kel
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        print(f"{value} degrees Fahrenheit is {fahr_to_cel} degrees Celsius")
        return fahr_to_cel
    elif from_unit == 'fahrenheit' and to_unit == 'fahrenheit':
        print(f"{value} degrees Fahrenheit is also {value} !")
        return value
    else:
        pass

    # kelvin to celsius or fahrenheit
    kel_to_cel = round((value - 273.15), 3)
    kel_to_fahr = round((value * 9 / 5) - 459.67, 3)

    if from_unit == 'kelvin' and to_unit == 'celsius':
        print(f"{value} degrees Kelvin is {kel_to_cel} degrees Celsius")
        return kel_to_cel
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        print(f"{value} degrees Kelvin is {kel_to_fahr} degrees Fahrenheit")
        return kel_to_fahr
    elif from_unit == 'kelvin' and to_unit == 'kelvin':
        print(f"{value} degrees Kelvin is also {value} !")
        return value
    else:
        pass

    # yards to meters or miles
    yards_to_meters = round(value / 1.094, 3)
    yards_to_miles = round(value / 1760, 3)

    if from_unit == 'yards' and to_unit == 'meters':
        print(f"{value} Yards is {yards_to_meters} Meters")
        return yards_to_meters
    elif from_unit == 'yards' and to_unit == 'miles':
        print(f"{value} Yards is {yards_to_miles} Miles")
        return yards_to_miles
    elif from_unit == 'yards' and to_unit == 'yards':
        print(f"{value} Yards is also {value} Yards!")
    else:
        pass

    # miles to meters or yards
    miles_to_meters = round(value * 1609, 3)
    miles_to_yards = round(value * 1760, 3)

    if from_unit == 'miles' and to_unit == 'meters':
        print(f"{value} Miles is {miles_to_meters} Meters")
        return miles_to_meters
    elif from_unit == 'miles' and to_unit == 'yards':
        print(f"{value} Miles is {miles_to_yards} Yards")
        return miles_to_yards
    elif from_unit == 'miles' and to_unit == 'miles':
        print(f"{value} Miles is also {value} Miles!")
    else:
        pass

    # meters to miles or yards
    meters_to_miles = round(value / 1609, 3)
    meters_to_yards = round(value * 1.094, 3)

    if from_unit == 'meters' and to_unit == 'miles':
        print(f"{value} Meters is {meters_to_miles} Miles")
        return meters_to_miles
    elif from_unit == 'meters' and to_unit == 'yards':
        print(f"{value} Meters is {meters_to_yards} Yards")
        return meters_to_yards
    elif from_unit == 'meters' and to_unit == 'meters':
        print(f"{value} Meters is also {value} Meters!")
    else:
        pass


    # exceptions

    if from_unit == 'meters' or from_unit == 'miles' or from_unit == 'yards' and to_unit == 'celsius' or to_unit == 'kelvin' or to_unit == 'fahrenheit':
        raise InvalidUnitError('Units entered are not compatible for conversion!')

    elif from_unit == 'celsius' or from_unit == 'kelvin' or from_unit == 'fahrenheit' and to_unit == 'yards' or to_unit == 'miles' or to_unit == 'meters':
        raise InvalidUnitError('Units entered are not compatible for conversion!')

    elif from_unit != 'celsius' or from_unit != 'fahrenheit' or from_unit != 'kelvin' or from_unit != 'yards' or from_unit != 'miles' or from_unit != 'meters':
        raise InvalidInputError('Invalid input(s). Choose from the following units to convert: Celsius, Kelvin, '
                                'Fahrenheit, Yards, Meters, Miles')

    elif to_unit != 'celsius' or to_unit != 'fahrenheit' or to_unit != 'kelvin' or to_unit != 'yards' or to_unit != 'miles' or to_unit != 'meters':
        raise InvalidInputError('Invalid input(s). Choose from the following units to convert: Celsius, Kelvin, '
                                'Fahrenheit, Yards, Meters, Miles')
    else:
        pass






