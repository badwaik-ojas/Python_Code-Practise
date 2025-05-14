"""
Tuples:
    Tuples are immutable lists and cannot be changed in any way once it is created.
    Tuples are defined in the same way as lists.
    They are enclosed within parenthesis and not within square braces.
    Tuples are ordered, indexed collections of data.
    Similar to string indices, the first value in the tuple will have the index [0], the second value [1]
    Negative indices are counted from the end of the tuple, just like lists.
    Tuple also has the same structure where commas separate the values.
    Tuples can store duplicate values.
    Tuples allow you to store several data items including string, integer, float in one variable.
"""

"""
One element tuple:
    if a tuple includes only one element, you should put a comma after the element. Otherwise, it is not considered as a tuple.
"""

t = (1,2,3,4,5)
print(t)

# length
print(len(t))

# access
print(t[3])

# Same function as list
# concat using "+"

"""
functions like 
    min
    max
    len
    slicing
    delete 
same as List
"""

# tuple(seq): It converts a specific sequence to a tuple
str = "hello world"
str_tup = tuple(str)
print(str_tup)

# sorted tuple
t1= (1,4,5,3,2,3,4,2,9)
print(sorted(t1))

# nested tuple
t2 = ((1,2,3), (4,5,6), (7,8), (9))
print(t2)
print(t2[0][1])

# get the index of the value
print(t.index(2))

# number of times the item occured in a tuple
print(t1.count(2))


print(t.index(2))



