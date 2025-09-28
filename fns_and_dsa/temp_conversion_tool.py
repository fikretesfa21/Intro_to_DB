FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def fahrenheit_to_celsius(temp):
    return (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def celsius_to_fahrenheit(temp):
    return (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == 'F':
        converted = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    elif unit == 'C':
        converted = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
