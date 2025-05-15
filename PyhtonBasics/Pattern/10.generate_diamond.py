'''
You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.

Input: 3
Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
'''
def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    pattern = []
    for i in range(n):
        star = '*'*(2*i+1)
        space = ' '*(n-i-1)
        st = space + star + space
        pattern.append(st)
    for i in range(n-1,0,-1):
        star = '*'*(2*i-1)
        space = ' '*(n-i)
        st = space + star + space
        pattern.append(st)
    return pattern
print(generate_diamond(5))