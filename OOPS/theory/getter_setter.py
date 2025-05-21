class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private
        self.__balance = balance  # Private
    
    # Getter for account number
    def get_account_number(self):
        return self.__account_number
    
    # Getter for balance
    def get_balance(self):
        return self.__balance
    
    # Setter for balance with validation
    def set_balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative")
            return
        self.__balance = amount
    
    # Method that uses private variables
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")

# Create an account
account = BankAccount("12345", 1000)

# Can't access private variables directly
# print(account.__balance)  # This will cause an error

# Use getters to access private variables
print(f"Account Number: {account.get_account_number()}")
print(f"Current Balance: ${account.get_balance()}")

# Use setter to modify with validation
account.set_balance(1500)
print(f"Updated Balance: ${account.get_balance()}")

# Try setting an invalid balance
account.set_balance(-500)  # Will print error message

# Use a method that works with private variables
account.deposit(300)