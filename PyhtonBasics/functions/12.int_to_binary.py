'''
You are given an integer n. Your task is to return its binary representation as a string. Do not use any built-in functions for conversion.

Input: n = 5
Output: "101"
 
Input: n = -5
Output: "-101"
'''
def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    
    binary = ''
    num = n
    
    if n == 0:
        return "0"  # Special case for zero
 
    # Store the binary representation
    binary_representation = ""
    
    # Handle negative numbers
    is_negative = n < 0
    if is_negative:
        n = -n  # Work with the absolute value
    
    while n >0:
        binary_representation += str(n%2)
        n = n//2
    if is_negative:
        binary_representation = "-" + binary_representation
    return binary_representation
