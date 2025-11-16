def draw_square_pattern():
    """
    Prompts the user for a pattern size and prints a square pattern
    of asterisks using nested loops.
    """
    print("--- Pattern Drawing with Nested Loops ---")

    # 1. Prompt User for Pattern Size
    try:
        # Ask for the pattern size and convert it to an integer
        size_input = input("Enter the size of the pattern: ")
        size = int(size_input)

        # Basic validation to ensure it's a positive integer
        if size <= 0:
            print("Please enter a positive integer greater than zero.")
            return

    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    # Initialize a counter for the rows (for the while loop)
    row_count = 0

    # 2. Draw the Pattern
    # Outer loop (while loop) controls the number of rows
    while row_count < size:
        # Inner loop (for loop) controls the number of columns (asterisks) in a single row
        for _ in range(size):
            # Print an asterisk, preventing a newline after each one
            print("*", end="")

        # After the inner for loop finishes, print a newline character to move to the next row
        print()

        # Increment the row counter for the while loop
        row_count += 1

# Run the function
if __name__ == "__main__":
    draw_square_pattern()