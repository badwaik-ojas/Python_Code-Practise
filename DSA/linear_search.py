import numpy as np

def find_number(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return (i, num)
    return set()
        
arr = np.array([1, 2, 3, 4, 5, 6, 7, 10, 12, 14])
target = 22

result = find_number(arr=arr, target=target)

if len(result) > 1:
    print(f"The number {target} exist at index {result[0]}")
else:
    print(f"the number {target} does not exist")
