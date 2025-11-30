import sys
from robust_division_calculator import safe_divide

def main():
    """
    Handles command line arguments and prints the result of the safe division.
    """
    # Check if exactly two arguments (numerator and denominator) are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Arguments are passed as strings from the command line
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the robust division function
    result = safe_divide(numerator, denominator)
    
    # Print the result or the error message returned by safe_divide
    print(result)

if __name__ == "__main__":
    main()