# Objective: Illustrate variable scope using global constants for temperature conversion.

# --- 1. Define Global Conversion Factors ---
# Setting the factors using the exact required fractional notation.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# --- 2. Implement Conversion Functions ---

def convert_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius."""
    # The function reads the global FAHRENHEIT_TO_CELSIUS_FACTOR
    # Formula: (F - 32) * 5/9
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit."""
    # The function reads the global CELSIUS_TO_FAHRENHEIT_FACTOR
    # Formula: (C * 9/5) + 32
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# --- 3. User Interaction and Main Logic ---

def main():
    while True:
        try:
            # User interaction: Prompt for temperature input
            temp_input = input("Enter the temperature to convert: ")
            temperature = float(temp_input)
            break
        except ValueError:
            # Implementation of Value Error handling
            raise ValueError("Invalid temperature. Please enter a numeric value.")

    # User interaction: Prompt for unit input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    result_temp = None
    result_unit = ""
    original_unit = ""

    if unit == 'F':
        # Implement conversion F to C
        result_temp = convert_to_celsius(temperature)
        original_unit = "F"
        result_unit = "C"
    elif unit == 'C':
        # Implement conversion C to F
        result_temp = convert_to_fahrenheit(temperature)
        original_unit = "C"
        result_unit = "F"
    else:
        print("Invalid unit input. Please enter 'C' or 'F'.")
        return

    # User interaction: Display the final result
    print(f"{temperature}°{original_unit} is {result_temp}°{result_unit}")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)