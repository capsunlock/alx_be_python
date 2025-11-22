# Objective: Familiarize yourself with Python’s datetime module.

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    # Part 1: Get the current date and time
    current_date = datetime.now()
    
    # Format and print the result
    # %Y = Year (4 digits), %m = Month (2 digits), %d = Day (2 digits)
    # %H = Hour (24h format), %M = Minute (2 digits), %S = Second (2 digits)
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_datetime}")
    # We return the datetime object for potential further use, though not strictly required by the prompt
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days and calculates the future date.

    Args:
        current_date (datetime): The starting datetime object.
    """
    while True:
        try:
            # Prompt the user for the number of days
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Part 2: Calculate the future date
    # timedelta is used to represent a duration (in this case, a number of days)
    time_difference = timedelta(days=days_to_add)
    future_date = current_date + time_difference
    
    # Format and print the future date
    # We only use %Y, %m, and %d to show only the date part
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {formatted_future_date}")
    # We return the future date object
    return future_date

def main():
    # Execute Part 1: Display current date and get the current date object
    current = display_current_datetime()
    
    # Execute Part 2: Calculate the future date
    calculate_future_date(current)

if __name__ == "__main__":
    main()