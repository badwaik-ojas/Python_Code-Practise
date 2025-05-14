def max_subarray_sum(nums):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0  # Initialize current_sum to 0

    for num in nums:
        current_sum = max(num, current_sum + num)  # Update current_sum
        max_sum = max(max_sum, current_sum)  # Update max_sum

    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, -1, -5, 4]  # Example array
result = max_subarray_sum(nums)
print("Maximum subarray sum:", result)

def min_subarray_sum(nums):
    min_sum = float('inf')  # Initialize max_sum to negative infinity
    current_sum = 0  # Initialize current_sum to 0

    for num in nums:
        current_sum = min(num, current_sum + num)  # Update current_sum
        min_sum = min(min_sum, current_sum)  # Update max_sum

    return min_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Example array
result = min_subarray_sum(nums)
print("Min subarray sum:", result)