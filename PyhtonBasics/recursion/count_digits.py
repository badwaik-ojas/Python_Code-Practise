'''
Number of Digits using Recursion
Problem Description:

You are given a positive integer n. Your task is to find the number of digits in the integer using recursion.

Input: n = 12345
Output: 5
 
Input: n = 7
Output: 1
'''

def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n//10)
    
print(count_digits(12345))  # Output: 5