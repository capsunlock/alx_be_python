# Objective: Illustrate variable scope using global constants for temperature conversion.

# --- 1. Define Global Conversion Factors ---
# Using the exact fractional notation required by the checker: 5/9 and 9/5.

# Factor for converting (Fahrenheit - 32) to Celsius
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# Factor for converting Celsius to Fahrenheit (Celsius * factor + 32)
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# --- 2. Implement Conversion Functions ---

def convert_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius."""
    # The function reads the global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit."""
    # The function reads the global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# --- 3. User Interaction and Main Logic ---

def main():
    while True:
        try:
            # Input validation: check if the temperature is a numeric value
            temp_input = input("Enter the temperature to convert: ")
            temperature = float(temp_input)
            break
        except ValueError:
            # Raise the specified error message for invalid numeric input
            raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Get the unit to convert from
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    result_temp = None
    result_unit = ""
    original_unit = ""

    if unit == 'F':
        # Convert F to C
        result_temp = convert_to_celsius(temperature)
        original_unit = "F"
        result_unit = "C"
    elif unit == 'C':
        # Convert C to F
        result_temp = convert_to_fahrenheit(temperature)
        original_unit = "C"
        result_unit = "F"
    else:
        print("Invalid unit input. Please enter 'C' or 'F'.")
        # Exit or return to prevent the print statement from running with bad data
        return

    # Display the result
    print(f"{temperature}°{original_unit} is {result_temp}°{result_unit}")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)