'''
Question 0: Class for Bank Account

Design a Python class named BankAccount to represent bank accounts.

Theory:
A bank account typically includes attributes such as account number, balance, and account holder name. The class should handle operations such as deposit, withdrawal, and transfer of funds between accounts.

Operations:

Deposit – Add funds to the account
Withdrawal – Subtract funds from the account
Transfer – Transfer funds from one account to another

Test Cases:

Test Case 1:

acc1 = BankAccount("John Doe", 1000)  
acc2 = BankAccount("Jane Smith", 2000)

assert acc1.balance == 1000  
assert acc2.balance == 2000

acc1.deposit(500)  
acc2.withdraw(100)  
acc1.transfer(acc2, 200)

assert acc1.balance == 1300  
assert acc2.balance == 2300
Test Case 2:

acc3 = BankAccount("Alice Johnson", 500)  
acc4 = BankAccount("Bob Brown", 1500)

assert acc3.balance == 500  
assert acc4.balance == 1500

acc3.deposit(100)  
acc4.withdraw(200)  
acc3.transfer(acc4, 300)

assert acc3.balance == 400  
assert acc4.balance == 1800
'''

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance")
        self.withdraw(amount)            # Withdraw from current account
        target_account.deposit(amount)   # Deposit into target account