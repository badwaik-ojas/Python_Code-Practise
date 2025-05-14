"""
Lists:
    Lists are ordered.
    Lists can contain any arbitrary objects.
    List elements can be accessed by index.
    Lists can be nested to arbitrary depth.
    Lists are mutable.
    Lists are dynamic.
    Lists are ordered, mutable collections of items.
    They can contain items of different data types.
"""

l = [{1:1},1,2,{1,2,3}, set()]
print(l)

m = set()
print(m)

l = [0,1,2,3,4,5,6,7,8,9,10]
print(l[0:3])

# extend: we use the extend() function to add a new element to the list.
l.extend([11,12,13])
print(l)

# append: As different from the extend() method, with the append() method, we add only one element to the list
l.append(12)
print(l)

# length
print(len(l))

# insert: This is used to insert an element in a list at an index
l.insert(13,99)
print(l)

# min, max, sum
print("min: ",min(l)," max: ", max(l)," sum: ",sum(l))

# update an element
l[13] = 13
print("update: ",l)

# delete an element
del(l[2])
print(l)

# delete complete list
# del l

l = [0,1,2,3,4,5,6,7,8,9,10]

# covert a string into list, default sep = " "(space)
mes = "hello world how are you"
mes_list = mes.split()
print(mes_list)

# input function
# text = input("exter list")
# print(text)

# in and not in
print(13 in l)
print(2 in l)
print(l)
# All List element
l.append(1)
print(l) # Add element
x = l.count(1)
print(x) # Count the number of occurance.
l.extend([1,2,3,4])
print(l) # Adds list to the existing list
print(l.index(3)) # Return the index value of the element.
print(l.pop(1)) # Remove the element by index value
l.remove(1)
print(l) # Remove the first element with value specified.
l.sort()
print(l) # Sorts the element.
l.reverse() # reverses the list
l.clear() #clears the list

'''
##### List Comprehension

Basics Syantax            [expression for item in iterable]
with conditional logic    [expression for item in iterable if condition]
Nested List Comprehension [expression for item1 in iterable1 for item2 in iterable2]
List Comprehension with else [<value_if_true> if <condition> else <value_if_false> for <item> in <iterable>]

'''
sqaure=[num**2 for num in range(10)]
even_numbers=[num for num in range(10) if num%2==0]
words = ["hello", "world", "python", "list", "comprehension"]
numbers = [1, 2, 3, 4, 5]
result = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(result)
enumerate(l)





