# Methond 1

def max_product(arr):
    max_prod = 0
    for i, num1 in enumerate(arr):
        for j, num2 in enumerate(arr):
            if i != j:
                if num1 * num2 > max_prod:
                    max_prod = num1 * num2
    return max_prod

arr = [1, 7, 3, 4, 9, 5] 
print(max_product(arr))

# Method 2 

def max_product1(arr):
    max1, max2 = 0, 0
    for i, num in enumerate(arr):
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        
    return max1 * max2

arr = [1, 7, 3, 4, 9, 5] 
print(max_product(arr))