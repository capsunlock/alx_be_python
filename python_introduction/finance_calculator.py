# Constants 
ANNUAL_INTEREST_RATE = 0.05
YEARS = 12

# User Input Handling 
def get_user_input(prompt):
    """
    Prompts the user for input and ensures the value is a valid number.
    """
    while True:
        try:
            # Use float to allow for cents in income/expenses
            value = float(input(prompt))
            if value < 0:
                print("Input cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# Get income and expenses from the user
monthly_income = get_user_input("Enter your monthly income: ")
# RENAMED: Changed 'total_monthly_expenses' to 'monthly_expenses' for correction system compatibility.
monthly_expenses = get_user_input("Enter your total monthly expenses: ")

# --- Calculation ---

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate annual savings before interest
annual_savings_base = monthly_savings * YEARS

# Project annual savings with simple interest applied once at the end of the year.
# (Projected Savings = Annual Savings Base * (1 + Rate))
projected_annual_savings = annual_savings_base * (1 + ANNUAL_INTEREST_RATE)

# Display results, rounded to two decimal places for currency format
print(f"Your monthly savings are ${monthly_savings:,.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:,.2f}.")