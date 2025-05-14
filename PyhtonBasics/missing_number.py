def find_missing_number(nums):
    n = len(nums) + 1  # Length of the list including the missing number
    total_sum = n * (n + 1) / 2  # Sum of first n natural numbers

    actual_sum = sum(nums)  # Sum of numbers in the list
    missing_number = total_sum - actual_sum  # Find the missing number
    return missing_number

# Example usage:
nums = [1, 2, 3, 4, 7, 6, 8]
missing_number = find_missing_number(nums)
print("The missing number is:", missing_number)
