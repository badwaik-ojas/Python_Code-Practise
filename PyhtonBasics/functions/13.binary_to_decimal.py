'''
You are given a string binary_str representing a binary number. Your task is to convert this binary string to its corresponding decimal integer. Do not use any built-in functions for conversion.

Input: binary_str = "101"
Output: 5
 
Input: binary_str = "1101"
Output: 13
'''

def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    # Your code here
    sum = 0
    for i, k in enumerate(reversed(binary_str)):
        print(f"i:{i}, k:{k}") 
        if int(k) == 1:
            sum += 2**int(i)
    return sum        

print(binary_to_decimal('1101'))