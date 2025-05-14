import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_length = nr_letters + nr_symbols + nr_numbers
lis = [letters, numbers, symbols]
num = 0
l = 0
s = 0
n = 0
password_list = []

'''
while num < password_length:
    select_random = random.randint(0,2)
    print(num)
    if select_random == 0 and l != nr_letters:
        password += random.choice(letters)
        l += 1
        num += 1
    elif select_random == 1 and s != nr_symbols:
        password += random.choice(symbols)
        s += 1
        num += 1
    elif select_random == 2 and n != nr_numbers:
        password += random.choice(numbers)
        n += 1 
        num += 1
'''

for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))
for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)
password = "".join(password_list)
print(password)
     




