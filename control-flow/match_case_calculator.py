# --- User Input Handling ---

def get_number(prompt):
    """
    Prompts the user for numerical input and validates it.
    """
    while True:
        try:
            # Use float() to allow for decimal numbers in the calculation
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Get the two numbers from the user
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

# Get the operation choice from the user
operation = input("Choose the operation (+, -, *, /): ")

# --- Match Case Logic ---
result = None
error_message = None

# The match statement checks the value of the 'operation' variable
match operation:
    case '+':
        result = num1 + num2
    
    case '-':
        result = num1 - num2
    
    case '*':
        result = num1 * num2
    
    case '/':
        # Case for division: Must handle division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            error_message = "Cannot divide by zero."
            
    case _:
        # The underscore (_) acts as a default/catch-all case for invalid operations
        error_message = f"Error: '{operation}' is not a recognized operation."

# --- Output Result ---

if error_message:
    print(error_message)
elif result is not None:
    # Display the result, rounded to two decimal places for readability
    print(f"The result is {result:.2f}.")