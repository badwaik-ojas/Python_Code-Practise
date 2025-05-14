"""
In Python, you can achieve similar functionality to Scala's for comprehension using list 
comprehensions. List comprehensions provide a concise way to create lists.
"""

my_list = [1, 2, 3, 4, 5]

# Using list comprehension to loop over the list
result = [x**2 for x in my_list]

# Printing each element
print(result)

# Using list comprehension to loop over the list
result = [x**2 for x in my_list if x%2 ==0]

# Printing each element
print(result)