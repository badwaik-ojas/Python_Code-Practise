"""
Dictionaries in Python
    Dictionaries are used to store data values in key:value pairs.
    A dictionary is a collection which is ordered, changeable or mutable and do not allow duplicates.
    Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
    Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has
    been created.

    Unique: Each key must be unique within the dictionary.
    Immutable: Keys must be of immutable types such as strings, numbers, or tuples.
    Hashable: Keys must be hashable, which allows Python to use a hash table to quickly retrieve values.
    Ordered (Python 3.7+): The insertion order of keys is maintained.

    A key must be hashable, which means it has a hash value that does not change during its lifetime. 
    This is why immutable types are used as keys since they have a fixed hash value
"""

dict1 = {'key1':1, 'key2':2, 'key3':3}
print(dict1['key1'])

test = {(1,3):5, 4:5}
print(test)

# keys(): print all keys
print(dict1.keys())

# values(): print all values
print(dict1.values())

# del: delete keys
del(dict1['key3'])
print(dict1)

# shallow copy and deep copy concept similar to one declared in set

# pop(): This function is used to remove a specific item from the dictionary
print(dict1.pop('key2'))

# get(): This method returns the value for the specified key if it is available in the dictionary. If the key is not available, it returns None.
print(dict1.get('key1'))

# It returns a new dictionary with the certain sequence of the items as the keys of the dictionary and the values are assigned with None.
dict2 = {'key1':1, 'key2':2, 'key3':3, 'key4':4, 'key5':5, 'key6':6}
dict3 = dict.fromkeys({'a','b'})
print(dict3)

# update
dict2 = {'key1':1, 'key2':2, 'key3':3, 'key4':4, 'key5':5, 'key6':6}
dict3 = {'key1':7, 'key2':8, 'key6':1000}
dict2.update(dict3)
print("dict2", dict2)

# Items(): It returns a list of key:value pairs in a dictionary. The elements in the lists are tuples
dict2 = {'key1':1, 'key2':2, 'key3':3, 'key4':4, 'key5':5, 'key6':6}
print(dict2.items())

# loops
# for x in product: returns keys
# for y in product.values(): returns values
# for x, y in product.items(): returns tuple(key, value)