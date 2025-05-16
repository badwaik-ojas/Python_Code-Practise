'''
Rotate a List (Without Slicing)

You are given a list of integers and an integer k. Write a Python function to rotate the list to the right by k positions without using slicing. A rotation shifts elements from the end of the list to the front.

Input: lst = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]

Input: lst = [10, 20, 30, 40, 50], k = 3
Output: [30, 40, 50, 10, 20]
'''

def rotate_list(lst, k):
    # Handling the case where the list is empty
    if not lst:
        return []
    
    # Modulo to handle the case where k is greater than the length of the list
    k = k % len(lst)
    
    # Brute force approach using loops
    for _ in range(k):
        last_element = lst.pop()  # Remove the last element
        lst.insert(0, last_element)  # Insert it at the front
    
    return lst
    

        
