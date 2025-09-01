def convert_temperature(value, unit):
    unit = unit.lower()
    
    if unit == "celsius" or unit == "c":
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        print(f"{value} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K")
    
    elif unit == "fahrenheit" or unit == "f":
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{value} °F = {celsius:.2f} °C = {kelvin:.2f} K")
    
    elif unit == "kelvin" or unit == "k":
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{value} K = {celsius:.2f} °C = {fahrenheit:.2f} °F")
    
    else:
        print("Invalid unit! Please enter Celsius, Fahrenheit, or Kelvin.")


# ---- Main Program ----
value = float(input("Enter the temperature value: "))
unit = input("Enter the unit (Celsius/Fahrenheit/Kelvin): ")

convert_temperature(value, unit)
