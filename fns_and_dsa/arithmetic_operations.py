# Objective: Define a function to perform basic arithmetic operations using if/elif/else.

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
    # Normalize the operation string to handle case variations
    op = operation.lower()

    if op == 'add':
        return num1 + num2
    
    elif op == 'subtract':
        return num1 - num2
    
    elif op == 'multiply':
        return num1 * num2
    
    elif op == 'divide':
        # Critical: Handle division by zero scenario
        if num2 == 0:
            return DIVISION_BY_ZERO_ERROR
        else:
            return num1 / num2
    
    else:
        # Default case for any unrecognized operation
        return f"Error: Invalid operation '{operation}'. Must be one of: add, subtract, multiply, divide."