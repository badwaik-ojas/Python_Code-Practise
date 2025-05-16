'''
You are given two integers n and m. Your task is to find the GCD of these two numbers. The GCD is the largest positive integer that divides both numbers without leaving a remainder. Do not use any built-in functions and do not use recursion.
Input: n = 48, m = 18
Output: 6
 
Input: n = 56, m = 98
Output: 14
'''


def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD of n and m.
    """
    # Ensure n and m are positive
    n = abs(n)
    m = abs(m)
 
    # Use the Euclidean algorithm iteratively
    while m != 0:
        n, m = m, n % m  # Assign m to n and remainder of n divided by m to m
 
    return n  # When m becomes 0, n is the GCD