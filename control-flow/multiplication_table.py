def multiplication_table_generator():
    """
    Prompts the user for a number and prints its multiplication table
    from 1 to 10 using a for loop.
    """
    print("--- Multiplication Table Generator ---")

    # 1. Prompt User for a Number
    try:
        # Ask for the number and convert it to an integer
        number_input = input("Enter a number to see its multiplication table: ")
        # Ensure 'number' is an integer for clean table display
        number = int(number_input)
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    # 2. Generate and Print the Multiplication Table
    # The loop iterates from 1 up to (but not including) 11, which covers 1 through 10.
    for i in range(1, 11):
        # Calculate the product
        product = number * i

        # Print each line in the required format: "X * Y = Z"
        print(f"{number} * {i} = {product}")

# Run the function
if __name__ == "__main__":
    multiplication_table_generator()