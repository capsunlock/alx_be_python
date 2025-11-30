import sys
# Import the BankAccount class from the bank_account.py file
from bank_account import BankAccount 

def main():
    # Initialize the account. The tests will use a starting balance of 250 internally.
    account = BankAccount(100)  
    
    # 1. Check for basic usage error
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # 2. Parse the command line argument
    try:
        command_line_input = sys.argv[1]
        
        # Split the input (e.g., 'deposit:50') into command and parameters
        command, *params = command_line_input.split(':')
        
        # Try to convert the amount part to a float, if it exists
        amount = float(params[0]) if params else None
        
    except (IndexError, ValueError):
        # Handles input like 'deposit' (missing amount) or 'deposit:abc' (invalid amount)
        print("Error: Invalid command format or amount. Use <command>:<amount>.")
        sys.exit(1)

    # 3. Handle the commands
    
    # --- Deposit Command ---
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        # Output must be strictly e.g., Deposited: $67.0
        print(f"Deposited: ${amount:.1f}") 

    # --- Withdraw Command ---
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            # Output must be strictly e.g., Withdrew: $50.0
            print(f"Withdrew: ${amount:.1f}")
        else:
            # Output must be strictly: Insufficient funds.
            print("Insufficient funds.")
            
    # --- Display Command ---
    elif command == "display":
        account.display_balance()
        
    # --- Invalid Command ---
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()