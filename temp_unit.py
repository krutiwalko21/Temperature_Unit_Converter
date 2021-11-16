

def conversion(value, from_unit, to_unit):
    """ Convert and return the temperature value from from_unit to to_unit. """

    #Conversion Formula from different units to Kelvin
    toK = {'K': lambda val: val,                     #Kelvin
           'C': lambda val: val + 273.15,            #Celsius
           'F': lambda val: (val - 32)*5/9 + 273.15, #fahrenheit
          }
    #Conversion Formula from Kelvin to different units
    fromK = {'K': lambda val: val,
             'C': lambda val: val - 273.15,
             'F': lambda val: (val - 273.15) * 9/5 + 32 ,
            }

    #Convert the temperature from from_unit to K
    try:
        T = toK[from_unit](value)
    except KeyError:
        raise ValueError('Unrecognised temperature unit: {}'.format(from_unit))

    if T < 0:
        raise ValueError('Invalid temperature: {} {} is less than 0 K'
                                .format(value, from_unit))

    if from_unit == to_unit:
        return value

    #Convert it from K to to_unit and return its value
    try:
        return fromK[to_unit](T)
    except KeyError:
        raise ValueError('Unrecognised temperature unit: {}'.format(to_unit))

