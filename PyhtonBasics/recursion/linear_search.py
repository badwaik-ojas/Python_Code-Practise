def linear_search(arr, x):
    if len(arr) <=0:
        return False
    if arr[0] == x:
        return True
    return linear_search(arr[1:], x)

print(linear_search([1,2,3,4], 5))
    
