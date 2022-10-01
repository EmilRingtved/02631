import numpy as np
def convertTemperature(T,unitFrom,unitTo):
    if unitTo == "Celsius":
        if unitFrom == "Fahrenheit":
            T = (T-32)/1.8
            return T
        elif unitFrom == "Kelvin":
            T = T - 273.15
            return T
    elif unitTo == "Fahrenheit":
        if unitFrom == "Celsius":
            T = 1.8*T+32
            return T
        elif unitFrom == "Kelvin":
            T = 1.8*T-459.67
            return T
    elif unitTo == "Kelvin":
        if unitFrom == "Celsius":
            T = T+273.15
            return T
        elif unitFrom == "Fahrenheit":
            T = (T+459.67)/1.8
            return T
    else:
        return "invalid"
print(convertTemperature(50.0,"Fahrenheit","Celsius"))