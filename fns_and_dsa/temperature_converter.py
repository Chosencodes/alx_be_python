# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
FAHRENHEIT_FREEZING_POINT = 32

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_FREEZING_POINT

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Display menu
def display_menu():
    print("Temperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")

# Main interaction function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius:.2f}°C is {fahrenheit:.2f}°F\n")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

        elif choice == "2":
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C\n")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.\n")

if __name__ == "__main__":
    main()

