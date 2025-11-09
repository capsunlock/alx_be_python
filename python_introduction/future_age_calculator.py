# Assuming the current year is 2023
YEARS_TO_FUTURE = 27

# Prompt the user for their current age.
# The input() function returns a string, so we wrap it in int() to ensure
# we can perform arithmetic calculations.
try:
    current_age = int(input("How old are you? "))
except ValueError:
    # Error handling just incase the user enters non-integer text
    print("Invalid input. Please enter your age as a whole number.")
    exit()

# Calculate the user's age in the year 2050 by adding the difference in years.
future_age = current_age + YEARS_TO_FUTURE

# Print the result in specified format.
print(f"In 2050, you will be {future_age} years old.")