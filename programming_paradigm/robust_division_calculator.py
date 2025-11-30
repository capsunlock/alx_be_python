def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling for ValueError (non-numeric)
    and ZeroDivisionError.

    Args:
        numerator (str): The string input for the numerator.
        denominator (str): The string input for the denominator.

    Returns:
        str: The division result or an appropriate error message.
    """
    
    # --- Try to convert inputs to float and perform division ---
    try:
        # Attempt to convert both arguments to floating-point numbers
        num = float(numerator)
        den = float(denominator)

        # Attempt the division
        result = num / den
        
        # If successful, return the formatted result
        return f"The result of the division is {result}"

    # --- Catch Specific Errors ---
    
    except ValueError:
        # This catches errors when float(numerator) or float(denominator) fails
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # This catches errors when the division (num / den) results in division by zero
        return "Error: Cannot divide by zero."

    except Exception as e:
        # Catch any unexpected errors
        return f"An unexpected error occurred: {e}"