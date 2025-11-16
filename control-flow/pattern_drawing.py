def draw_square_pattern():
    """
    Prompts the user for a pattern size and prints a square pattern
    of asterisks using nested loops.
    """
    print("--- Pattern Drawing with Nested Loops ---")

    # 1. Prompt User for Pattern Size
    try:
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

    # 2. Draw the Pattern using a while loop for rows
    while row_count < size:
        # Use a for loop for columns to print asterisks in a single row
        # The range starts at 0 and goes up to 'size' (exclusive), running 'size' times.
        for _ in range(size):
            # Print an asterisk, preventing a newline after each one
            print("*", end="")

        # After the inner for loop finishes (one row is complete),
        # print a newline character to move to the next row
        print()

        # Increment the row counter for the while loop
        row_count += 1

# Run the function
if __name__ == "__main__":
    draw_square_pattern()