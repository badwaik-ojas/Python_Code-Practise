print("Welcome to the tip calculator!\n")

# Input total bill amount
bill_amount = float(input("What is your total bill amount? \n"))

# Enter the percent tip you want to provide
tip = int(input("How much tip you want to provide? 10, 12 or 15 \n"))

# Enter the number of people were there?
no_of_person = int(input("How many people to split the bill into?\n"))

total_amount = (bill_amount) * ( 1 + tip/100)

amt_per_person = total_amount / no_of_person

print(f"Each person should pay: ${round(amt_per_person,2)}")

x