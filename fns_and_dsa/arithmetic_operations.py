# Objective: Define a function to perform basic arithmetic operations.

# Define a constant for the division by zero error message.
DIVISION_BY_ZERO_ERROR = "Division by zero is not allowed."

def perform_operation(num1, num2, operation):
    """
    Performs one of four basic arithmetic operations based on the input string.

    Args:
        num1: The first number (float).
        num2: The second number (float).
        operation (str): The desired operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error string if
                      division by zero occurs or the operation is invalid.
    """
    # Use the match case statement for clean handling of the four operations
    match operation.lower():
        case 'add':
            return num1 + num2
        
        case 'subtract':
            return num1 - num2
        
        case 'multiply':
            return num1 * num2
        
        case 'divide':
            # Critical: Check for division by zero before performing the operation
            if num2 == 0:
                return DIVISION_BY_ZERO_ERROR
            else:
                return num1 / num2
        
        case _:
            # Handle any input that doesn't match the four required operations
            return f"Error: Invalid operation '{operation}'. Must be one of: add, subtract, multiply, divide."