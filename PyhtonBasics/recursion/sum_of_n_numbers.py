'''

Sum of N numbers using Recursion
Problem Description:

You are given a non-negative integer n. Your task is to find the sum of the first n natural numbers using recursion. The sum of the first n natural numbers is given by the formula S=1+2+3+...+nS = 1 + 2 + 3 + ... + nS=1+2+3+...+n.

Input: n = 5
Output: 15  # (1 + 2 + 3 + 4 + 5)
 
Input: n = 0
Output: 0   # Sum of zero natural numbers

'''

def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n-1)