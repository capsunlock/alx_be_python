class BankAccount:
    """
    Represents a simple bank account with deposit, withdraw, and display operations.
    """
    
    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional starting balance.
        :param initial_balance: The starting balance of the account (default is 0).
        """
        # Encapsulation: We store the balance privately, accessible only through methods.
        self._account_balance = initial_balance
        print(f"Account initialized with starting balance: ${self._account_balance:.2f}")

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        :param amount: The amount to deposit.
        """
        if amount > 0:
            self._account_balance += amount
            # print(f"Deposit successful. New balance: ${self._account_balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the amount from the balance if sufficient funds are available.
        :param amount: The amount to withdraw.
        :return: True if withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if self._account_balance >= amount:
            self._account_balance -= amount
            # print(f"Withdrawal successful. New balance: ${self._account_balance:.2f}")
            return True
        else:
            # print("Withdrawal failed: Insufficient funds.")
            return False

    def display_balance(self):
        """
        Prints the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")