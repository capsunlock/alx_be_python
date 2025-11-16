def calculator():
    """
    Prompts the user for two numbers and an operation, then performs
    the calculation using a match-case statement.
    """
    print("--- Simple Calculator with Match Case ---")

    # 1. Prompt for User Input
    try:
        # Get the first number (num1)
        # Using float() to allow for decimal numbers
        num1_input = input("Enter the first number: ")
        num1 = float(num1_input)

        # Get the second number (num2)
        num2_input = input("Enter the second number: ")
        num2 = float(num2_input)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Get the operation choice
    operation = input("Choose the operation (+, -, *, /): ")

    # Variable to hold the result
    result = None
    message = ""

    # 2. Perform the Calculation Using Match Case
    match operation:
        case '+':
            # Addition
            result = num1 + num2
            message = f"The result is {result}."
        case '-':
            # Subtraction
            result = num1 - num2
            message = f"The result is {result}."
        case '*':
            # Multiplication
            result = num1 * num2
            message = f"The result is {result}."
        case '/':
            # Division
            if num2 != 0:
                result = num1 / num2
                message = f"The result is {result}."
            else:
                # Handle division by zero case gracefully
                message = "Cannot divide by zero."
        case _:
            # Default case for invalid operation input
            message = f"Error: Invalid operation '{operation}'. Please choose one of +, -, *, /."

    # 3. Output the Result
    print(message)

# Run the calculator function
if __name__ == "__main__":
    calculator()