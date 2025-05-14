
numbers = [1,3,4,2,4,11,34,2,33,4,45,33]
temp = 0
for number in numbers:
    if number > temp:
        temp = number
    
print(temp)