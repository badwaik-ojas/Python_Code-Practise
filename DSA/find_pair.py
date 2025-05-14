# Function to find all distinct pairs whose sum equals the target
def find_pairs(nums, target):
    # To store pairs
    pairs = []
    # To store seen numbers to avoid duplicates
    seen = set()
    
    # Iterate over the array
    for i, num in enumerate(nums):
        # Calculate the complement that would add to the current number to make the target
        complement = target - num
        
        # Check if complement exists in the set and pair hasn't been used already
        if complement in seen and (complement, num) not in pairs and (num, complement) not in pairs:
            # Add the distinct pair (smaller, larger) to the list of pairs
            pairs.append((min(num, complement), max(num, complement)))
        
        # Add the current number to the set of seen numbers
        seen.add(num)
    
    return pairs

# Example usage:
nums = [1, 2, 3, 4, 3, 5, 6]
target = 6
result = find_pairs(nums, target)

# Output the result
print(f"Pairs that sum to {target}: {result}")

# Function to find the indices for which the sum of 2 numbers is equal to Target.
def two_sum(nums, target):
    seen = {}
    pairs = []
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen and (complement, num) not in pairs and (num, complement) not in pairs:
            # Add the distinct pair (smaller, larger) to the list of pairs
            pairs.append((seen[complement], i))
                
        seen[num] = i
    
    return pairs
 

indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")

