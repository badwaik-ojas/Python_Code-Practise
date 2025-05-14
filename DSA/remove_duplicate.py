def remove_duplicates(arr):
    seen = []
    for num in arr:
        if num not in seen:
            seen.append(num)
        
    return seen

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
