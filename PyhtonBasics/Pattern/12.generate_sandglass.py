'''
You are given an integer n. Your task is to return a sandglass pattern of '*', where the first row contains 2n - 1 stars and each subsequent row decreases the number of stars by 2, until the last row contains a single star. After reaching the smallest width, the pattern then continues with the same number of stars increasing back to 2n - 1. The stars in each row should be centered.

Input: 3
Output: ['*****', ' *** ', '  *  ', ' *** ', '*****']
 
Input: 4
Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']
'''

def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """

    pattern = []
    for i in range(n, 1, -1):
        star = '*'*(2*i-1)
        space = ' '*(n-i)
        st = space + star + space
        pattern.append(st)
    for i in range(1, n+1):
        star = '*'*(2*i-1)
        space = ' '*(n-i)
        st = space + star + space
        pattern.append(st)
    return pattern

print(generate_sandglass(3))
