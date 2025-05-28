def check_sorted(arr):
    if len(arr) <= 1:
        return True
    if arr[0] < arr[1]:
        return check_sorted(arr[1:])
    return False

print(check_sorted([1, 2, 3, 4, 5]))  # Output: True
print(check_sorted([1, 6, 3, 4, 5]))  # Output: False