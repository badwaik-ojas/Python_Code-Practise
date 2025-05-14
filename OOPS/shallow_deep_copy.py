'''

Shallow Copy
A shallow copy of an object creates a new object, but inserts references into it to the objects 
found in the original. This means that if the original object contains references to other objects, 
the shallow copy will reference the same objects. Consequently, changes to the nested objects will be 
reflected in both the original and the copied object.

'''

import copy

original = [1, 2, [3, 4]]
shallow_copy = copy.copy(original)

# Modify the nested list
shallow_copy[2][0] = 99

print(original)  # Output: [1, 2, [99, 4]]
print(shallow_copy)  # Output: [1, 2, [99, 4]]

'''
Deep Copy
A deep copy of an object creates a new object, and recursively copies all objects found in the original. 
This means that the copied object and the original object do not share references to nested objects; 
each nested object is itself a new object.
'''

import copy

original = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original)

# Modify the nested list
deep_copy[2][0] = 99

print(original)  # Output: [1, 2, [3, 4]]
print(deep_copy)  # Output: [1, 2, [99, 4]]

original = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original)

# Modify the nested list
deep_copy[2][0] = 99

print(original)  # Output: [1, 2, [3, 4]]
print(deep_copy)  # Output: [1, 2, [99, 4]]



