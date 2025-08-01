# Global conversion constants
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
FREEZING_POINT_C = 32

# Convert Celsius to Fahrenheit
def to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_C

# Convert Fahrenheit to Celsius
def to_celsius(fahrenheit):
    return (fahrenheit - FREEZING_POINT_C) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Main interaction
try:
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        converted = to_fahrenheit(temp)
        print(f"{temp}°C is {converted:.2f}°F")
    elif unit == "F":
        converted = to_celsius(temp)
        print(f"{temp}°F is {converted:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    print("Invalid temperature input. Please enter a numeric value.")

