'''
You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

Input: 3
Output: ['***', '* *', '***']
 
Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']
'''

def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    lst = []
    str1 = '*'
    str2 = ' '
    for i in range(1, n+1):
        if n <= 2:
            lst.append(str1*n)
        else:
            if i==1 or i==n:
                lst.append(str1*n)
            else:
                str = str1 + str2*(n-2) + str1
                lst.append(str)
    return lst

print(generate_hollow_square(3))