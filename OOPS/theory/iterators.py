'''
Topic: Python Iterators
What Are Iterators?
Iterators are an advanced Python concept used for:

Efficient looping

Better memory management

They provide a way to access elements sequentially without exposing the underlying data structure.

Basic Example with a List
python
Copy
Edit
my_list = [1, 2, 3, 4, 5, 6]
for i in my_list:
    print(i)
This prints: 1 2 3 4 5 6

type(my_list) returns: <class 'list'>

Creating an Iterator
python
Copy
Edit
iterator = iter(my_list)
print(type(iterator))
Output: <class 'list_iterator'>

An iterator object is created using iter().

Why Use Iterators?
Using iter() does not display the elements immediately.

It shows something like: <list_iterator object at memory_location>

This is because iterators use lazy loading:

Elements are only accessed when explicitly requested (via next()).

Accessing Elements One-by-One
python
Copy
Edit
print(next(iterator))  # 1
print(next(iterator))  # 2
...
Each call to next(iterator) fetches the next element.

Once all elements are exhausted, calling next() again raises a StopIteration exception.

Handling StopIteration Exception
python
Copy
Edit
try:
    print(next(iterator))
except StopIteration:
    print("There are no elements in the iterator.")
This is a clean way to safely iterate and handle the end of iteration.

Using Iterators with Strings
python
Copy
Edit
string_iterator = iter("Hello")
print(next(string_iterator))  # H
print(next(string_iterator))  # e
iter() works not just with lists, but also with strings and other iterable objects.

Key Takeaways
Iterators use lazy evaluation, reducing memory usage.

Use iter() to convert an iterable into an iterator.

Use next() to get elements one-by-one.

Handle StopIteration to avoid crashes at the end of iteration.

'''

my_list = [1, 2, 3, 4, 5, 6]

iterator = iter(my_list)
print(type(iterator))

print(next(iterator))  # 1
print(next(iterator))  # 2

try:
    print(next(iterator))
except StopIteration:
    print("There are no elements in the iterator.")


