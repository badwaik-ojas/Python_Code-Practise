"""
Sets:
    Set is one of 4 built-in data types in Python used to store collections of data including List, Tuple, and Dictionary
    Sets are unordered, but you can remove items and add new items.
    Set elements are unique. Duplicate elements are not allowed.
    A set itself may be modified, but the elements contained in the set must be of an immutable type.
    Sets are used to store multiple items in a single variable.
    You can denote a set with a pair of curly brackets {}.
    A set can not have mutable elements such as list or dictionary in it.
    Sets are useful for membership tests, eliminating duplicate entries, and performing mathematical set operations like union, intersection, difference, and symmetric difference.
"""

x = set() # empty set
y = ([1,2],3)
y[0][0] = 3
print(y)
# convert list to set
l = [1,2,3,4,2,3,4,2,3]
s = set(l)
print(s)

# add element
s.add(5)
print(s)

# update() fuction
s.update({6,7})
print(s)

# remove element if available
# it throws error if the element is not available
s.remove(7)
print(s)

# discard(): It leaves the set unchanged if the element to be deleted is not available in the set
s.discard(9)
print(s)

"""
Functions like:
    in
    not in
    min
    max
    sum
    index
Same as list and Tuples
"""

#in
print(1 in l)

set1 = {1,2,3}
set2 = {3,4,5,6}

# intersection: intersect of two sets using &
# common element between set
print("common element using intersect: ",set1 & set2)
print(set1.intersection(set2))

# difference: like let join minus common element
print("difference in element using set: ",set1 - set2)
print(set1.difference(set2))

# union: combine 2 sets
print(set1.union(set2))

# copy(): it returns a shallow copy of the original set.
# 
set3 = set1 # this is the shallow copy, both set1 and set3 point to same address updateing any 1 affects both
set1.add(4) 
print(set3)
set4 = set2.copy() # new copy created
set2.add(7)
print(set2)
print(set4) 

#symetric difference: unique element from 2 sets, common element element removed
set1.symmetric_difference(set2)

#intersection update: updates set1 with the output of below code
set1.intersection_update(set2)




















