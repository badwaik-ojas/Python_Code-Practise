"""
Tuples:
    Tuples are immutable lists and cannot be changed in any way once it is created.
    They are ordered collection.
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

'''
🧳 Packing and Unpacking in Tuples (Python)
In Python, packing and unpacking refer to the ways you can group and extract values using tuples (and lists too).

📦 Tuple Packing
Packing means putting multiple values into a single tuple.

    packed = 1, 2, 3
    print(packed)  # Output: (1, 2, 3)

Equivalent to:
    packed = (1, 2, 3)

🎁 Tuple Unpacking
Unpacking means extracting values from a tuple and assigning them to variables.
    a, b, c = (1, 2, 3)
    print(a, b, c)  # Output: 1 2 3

🌟 Use with Functions
✅ Returning multiple values (packing)

    def get_user():
        return "Alice", 30

user = get_user()  # ('Alice', 30) — packed

✅ Receiving multiple values (unpacking)

    name, age = get_user()
    print(name)  # Alice
    print(age)   # 30

🪄 Advanced Unpacking: Using * (Starred Expressions)

    a, *b = (1, 2, 3, 4)
    print(a)  # 1
    print(b)  # [2, 3, 4]

    *a, b = (1, 2, 3, 4)
    print(a)  # [1, 2, 3]
    print(b)  # 4

    a, *b, c = (1, 2, 3, 4, 5)
    print(a, b, c)  # 1 [2, 3, 4] 5

⚠️ Errors to Avoid
You must match the number of variables unless using *.
    x, y = (1, 2, 3)  # ❌ Too many values to unpack
'''
x =[[1, 3], 1, 2, 3]
x[1] = [1, 3]

x =([1, 2], 1, 2, 3)
x[0][1] = 3

'''
📌 Positional Arguments vs Keyword Arguments in Python
Understanding the difference helps you write flexible and readable functions.

🧱 1. Positional Arguments
    These are arguments passed by order/position. The values are assigned to parameters based on their position.
        def greet(name, age):
            print(f"Hello, {name}. You are {age} years old.")

        greet("Alice", 30)  # Positional: name="Alice", age=30
        ✅ Pros:
            Concise and fast to write.
        ❌ Cons:
            Can be confusing if there are many arguments, especially optional ones.

🏷️ 2. Keyword Arguments
    These are passed by specifying parameter names explicitly, regardless of their order.
    
        greet(age=30, name="Alice")  # Keyword: same result
            ✅ Pros:
                Clear and readable.
                Order doesn’t matter.
            ❌ Cons:
                Slightly longer to write.

🧪 Mixing Positional and Keyword Arguments
    You can mix them, but positional must come first.

    greet("Alice", age=30)  # ✅ Valid
    # greet(name="Alice", 30) ❌ SyntaxError: positional argument follows keyword

⚙️ Useful With *args and **kwargs

    def show(*args, **kwargs):
        print("Positional:", args)
        print("Keyword:", kwargs)

    show(1, 2, name="Alice", age=30)

    # Output:
        # Positional: (1, 2)
        # Keyword: {'name': 'Alice', 'age': 30}
'''


