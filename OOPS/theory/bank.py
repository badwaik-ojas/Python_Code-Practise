class Bank:

    def __init__(self, owner, balance=0):
        self.balance = balance
        self.owner = owner

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("please enter amount greater than 0")
            return False
        self.balance += amount
        print("amount deposited successfully!")
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print("please enter amount greater than 0")
            return
        elif amount > self.balance:
            print("insufficient funds")
            return
        self.balance -= amount
        print("amount withdrawn successfully")
        return self.balance
    
    def __str__(self):
        return f"bank account created for {self.owner} with balance: {self.balance}"
    
ojas = Bank('Ojas', 10000)
print(ojas)
print(f"add amount 1000, current balance: {ojas.deposit(1000)}")
print(f"withdraw amount 4000, current balance: {ojas.withdraw(4000)}")
print(f"current balance: {ojas.get_balance()}")


        
