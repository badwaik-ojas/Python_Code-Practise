'''
Merge Three Dictionaries

Design a Python function named merge_three_dictionaries to merge exactly three dictionaries into one.

Input: ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

Input: ({'x': 10, 'y': 20}, {'z': 30}, {'a': 40, 'b': 50})
Output: {'x': 10, 'y': 20, 'z': 30, 'a': 40, 'b': 50}
'''
def merge_three_dictionaries(dict1, dict2, dict3):
    # Your code goes here
    dict = {}
    return dict1 | dict2 | dict3



