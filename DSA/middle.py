def middle(lst):
    len1 = len(lst)
    mid = int(len1/2)
    rem = len1%2
    if rem == 0:
        return [lst[mid-1], lst[mid]]
    else:
        return [(lst[mid-2], lst[mid-1]), (lst[mid+2], lst[mid+1])]
    
myList = [1, 2, 3, 4]
print(middle(myList))  # [2,3]

