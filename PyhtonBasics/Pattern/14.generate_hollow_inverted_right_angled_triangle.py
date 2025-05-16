'''
You are given an integer n. Your task is to return a hollow inverted right-angled triangle pattern of '*', where the first row contains n stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be left-aligned.

Input: 4
Output: ['****', '* *', '**', '*']
 
Input: 5
Output: ['*****', '*  *', '* *', '**', '*']
'''

def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    pattern = []
    star = '*'
    space = ' '
    for i in range(n, 0, -1):
        if i in (1, 2, n):
            pattern.append(star*i)
        else:
            st = star + (i-2)*space + star
            pattern.append(st)
    return pattern