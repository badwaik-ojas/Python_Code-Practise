
def contains_duplicate(nums):
    len1 = len(nums)
    len2 = len(set(nums))
    if len1 > len2:
        return True
    return False

print(contains_duplicate([1,2,3]))