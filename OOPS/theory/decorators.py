'''
Python Decorators - Simple Explanation
What are Decorators?
Decorators are a way to add extra features to functions without changing the original function code.
Think of it like adding accessories to your phone - you can add a case, screen protector, or pop socket without modifying the phone itself!

Prerequisites: Understanding the Building Blocks
1. Function Copy
In Python, you can copy functions to variables:
pythondef welcome():
    return "Welcome to Advanced Python!"

# Copy the function to a variable
well = welcome

# Both work the same way
print(welcome())  # Output: Welcome to Advanced Python!
print(well())     # Output: Welcome to Advanced Python!

# Even if you delete the original, the copy still works!
del welcome
print(well())     # Still works!
Key Point: Functions are objects in Python - you can copy, pass, and store them!

2. Closures (Function Inside Function)
A closure is when you have a function inside another function:
pythondef main_welcome(message):
    # This variable is available to the inner function
    greeting = "Hello"
    
    def sub_welcome():
        # Inner function can access outer function's variables
        print(f"{greeting}! {message}")
        print("Please learn concepts properly")
    
    return sub_welcome  # Return the inner function

# Usage
my_func = main_welcome("Welcome to Python")
my_func()
# Output: 
# Hello! Welcome to Python
# Please learn concepts properly
Key Points:

Inner functions can access outer function variables
You can return the inner function
The inner function "remembers" the outer variables even after the outer function finishes


Now Let's Understand Decorators!
Basic Decorator Example
pythondef my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()  # Call the original function
        print("Something after the function")
    return wrapper

# Method 1: Manual decoration
def say_hello():
    print("Hello!")

decorated_hello = my_decorator(say_hello)
decorated_hello()

# Method 2: Using @ symbol (This is the decorator syntax!)
@my_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye()  # Automatically uses the decorator
Output for both methods:
Something before the function
Hello! (or Goodbye!)
Something after the function

Real-World Analogy
Think of decorators like gift wrapping:

Original function = Your gift (a book)
Decorator = Gift wrapping process
Decorated function = Wrapped gift

The book is still the same, but now it has extra presentation (wrapping paper, bow, card).

Step-by-Step: How Decorators Work
Step 1: The Decorator Function
pythondef my_decorator(original_function):
    def wrapper_function():
        # Do something BEFORE
        print("🎬 Action starts!")
        
        # Call the original function
        result = original_function()
        
        # Do something AFTER  
        print("🎬 Cut! Scene complete!")
        
        return result
    return wrapper_function
Step 2: Apply the Decorator
python@my_decorator
def perform_scene():
    print("🎭 Actor delivers amazing performance!")

# When you call perform_scene(), you actually get:
perform_scene()
Step 3: What Actually Happens
🎬 Action starts!
🎭 Actor delivers amazing performance!
🎬 Cut! Scene complete!

Decorators with Arguments
Sometimes you want to customize your decorator:
pythondef repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Hello!
# Hello! 
# Hello!
This is like saying: "Wrap this gift, but use 3 layers of wrapping paper!"

Common Use Cases
1. Timing Functions
pythonimport time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Function took {end - start} seconds")
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Done!")
2. Authentication (Web Development)
pythondef login_required(func):
    def wrapper():
        if user_is_logged_in():
            func()
        else:
            print("Please log in first!")
    return wrapper

@login_required
def view_profile():
    print("Here's your profile!")
3. Logging
pythondef log_calls(func):
    def wrapper():
        print(f"Calling function: {func.__name__}")
        result = func()
        print(f"Function {func.__name__} completed")
        return result
    return wrapper

@log_calls
def important_calculation():
    return 2 + 2

Key Benefits

Don't Repeat Yourself (DRY): Write common functionality once, apply everywhere
Clean Code: Keep original functions focused on their main job
Flexible: Easy to add/remove functionality
Reusable: Same decorator can be used on multiple functions


Simple Mental Model
Original Function: 🍎 (apple)
Decorator: 📦 (box)
Result: 📦🍎 (boxed apple)

The apple is still an apple, but now it's presented in a nice box!

Summary
Decorators are like magical wrappers that:

Take a function as input
Add extra behavior before/after the function
Return the enhanced function
Use the @decorator_name syntax for clean code

The magic formula:
python@decorator
def my_function():
    pass

# Is the same as:
# my_function = decorator(my_function)
Think of decorators as function enhancers - they make your functions more powerful without changing their core purpose!
'''

