import array as arr
from array import *

# Array is a container which can hold a fix number of items and these items should be of the same type.
# syntax: arr.array(<>,list())

# behaviour same as list 
special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
print(special_nums)

'''
✅ Core Concepts
1. What is an Array?
An array is a collection of elements stored in contiguous memory locations.

Every element in the array must be of the same data type (homogeneous).

Arrays allow for efficient access and manipulation via indexing.

Memory Representation Example:
If memory starts at address 100 and each integer takes 4 bytes:

Element 1 → Address 100

Element 2 → Address 104

Element 3 → Address 108
…and so on.

2. Why Understand Arrays in Python?
Although Python does not have a built-in array type like C/C++, Python's list is an abstraction built on top of C-style arrays.

Many advanced data structures are developed to overcome the limitations of basic arrays.

Understanding arrays helps in appreciating how lists are implemented and why alternatives are needed in more complex problems.

🆚 Arrays vs. Lists in Python
Feature	            Array	                                        List
Type of Elements	Homogeneous (same type)	                        Heterogeneous (different types allowed)
Size	            Fixed	                                        Dynamic (can grow/shrink)
Flexibility	        Less flexible	                                Highly flexible
Performance	        More memory-efficient and faster for large data	Slightly slower due to additional abstraction
Access and Update	O(1) — Efficient via indexing	                O(1) — Same efficiency
Usage in Python	    Via array or numpy module	                    Built-in list type
Use Case	        Numeric operations, large fixed-type datasets	General-purpose, flexible collections

🧠 Important Python-Specific Points
1. Python Built-in Data Structures
Built-ins like list, dict, set, tuple are natively available.

Arrays are not built-in, and must be imported using:

python
Copy
Edit
from array import array
2. Creating Arrays in Python
python
Copy
Edit
from array import array
arr = array('i', [1, 2, 3, 4, 5])  # 'i' means signed int
Type Code is required (e.g., 'i' for integers).

Modifying:

python
Copy
Edit
arr[0] = 10
3. Common Type Codes
Code	Type	Size (bytes)
'i'	Signed integer	2 or 4
'f'	Float	4
'd'	Double	8
'u'	Unicode character	2

🚫 Limitations of Arrays
Fixed Size: Cannot grow dynamically once declared.

Homogeneous Data: Can only store one type of element.

Not ideal for problems where flexibility or mixed types are needed.

✅ Advantages of Lists
Dynamic sizing — automatically resizes when appending or deleting.

Can store mixed data types (e.g., [1, 2.5, "hello"]).

Extensive built-in methods: .append(), .remove(), .sort(), etc.

🧩 When to Use What?
Scenario	Prefer
Large homogeneous numeric data	Array / NumPy
General-purpose collections	List
Performance-sensitive applications	Array or use NumPy for speed
When memory overhead is not a concern	List

🧠 Expert Insight
Understanding how Python lists are built on arrays bridges the conceptual gap between Python and lower-level languages (like C/C++).

Memory layout and data type constraints matter in algorithm optimization, especially in interviews and real-world applications.

Many advanced data structures (e.g., dynamic arrays, heaps, hash tables) internally use arrays, so understanding them is foundational to DSA mastery.

🔁 Key Takeaways
Arrays are simple, efficient, and used for homogeneous data.

Lists in Python are more flexible but slightly less efficient.

Arrays are not built-in in Python — you must use array module or numpy.

Lists are built on top of C-style arrays, but with dynamic capabilities.

For most use cases in Python, lists are preferred, but arrays and NumPy are used in numerical and scientific computing.
'''

