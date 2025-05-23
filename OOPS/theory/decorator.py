# Python Decorators - Complete Examples

print("=== 1. FUNCTION COPY EXAMPLE ===")
def welcome():
    return "Welcome to the Advanced Python course"

# Copy function to variable
well = welcome
print("Original function:", welcome())
print("Copied function:", well())

# Delete original function
del welcome
print("After deleting original, copy still works:", well())

print("\n" + "="*50)

print("=== 2. CLOSURES EXAMPLE ===")

# Basic closure
def main_welcome(message):
    def sub_welcome():
        print("Welcome to the Advanced Python course")
        print("Please learn this concepts properly")
        print(message)  # Can access outer function's variable
    return sub_welcome

# Call the closure
result_func = main_welcome("Welcome everyone")
result_func()

print("\n" + "-"*30)

# Closure with function parameter
def main_welcome_with_func(func, data):
    message = "Welcome"
    
    def sub_welcome():
        print("Welcome to the Advanced Python course")
        print("Please learn this concepts properly")
        # Call the function passed as parameter
        func(data)
    
    return sub_welcome

# Example usage
my_func = main_welcome_with_func(len, [1, 2, 3, 4, 5])
my_func()

print("\n" + "="*50)

print("=== 3. BASIC DECORATOR EXAMPLE ===")

def main_welcome_decorator(func):
    def sub_welcome():
        print("Welcome to the Advanced Python course")
        func()  # Call the original function
        print("Please learn this concepts properly")
    return sub_welcome

# Method 1: Manual decoration
def course_introduction():
    print("This is an advanced Python course")

decorated_func = main_welcome_decorator(course_introduction)
decorated_func()

print("\n" + "-"*30)

# Method 2: Using @ syntax (This is the proper way!)
@main_welcome_decorator
def course_introduction_decorated():
    print("This is an advanced Python course")

print("Using @ decorator syntax:")
course_introduction_decorated()

print("\n" + "="*50)

print("=== 4. DECORATOR WITH WRAPPER ===")

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

print("\n" + "="*50)

print("=== 5. DECORATOR WITH ARGUMENTS ===")

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello_multiple():
    print("Hello!")

print("Calling function decorated with repeat(3):")
say_hello_multiple()

print("\n" + "="*50)

print("=== 6. PRACTICAL DECORATOR EXAMPLES ===")

# Timer decorator
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)  # Simulate slow operation
    return "Task completed"

result = slow_function()
print(f"Result: {result}")

print("\n" + "-"*30)

# Logging decorator
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📞 Calling function: {func.__name__}")
        if args:
            print(f"   Args: {args}")
        if kwargs:
            print(f"   Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ Function {func.__name__} completed")
        return result
    return wrapper

@log_calls
def add_numbers(a, b):
    return a + b

@log_calls
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print("Testing logged functions:")
sum_result = add_numbers(5, 3)
print(f"Sum result: {sum_result}")

greet_result = greet("Alice", greeting="Hi")
print(f"Greet result: {greet_result}")

print("\n" + "-"*30)

# Validation decorator
def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("All arguments must be positive!")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width

try:
    area1 = calculate_area(5, 3)
    print(f"Area 1: {area1}")
    
    area2 = calculate_area(-5, 3)  # This will raise an error
    print(f"Area 2: {area2}")
except ValueError as e:
    print(f"❌ Error: {e}")

print("\n" + "="*50)

print("=== 7. CHAINING MULTIPLE DECORATORS ===")

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*{result}*"
    return wrapper

@bold
@italic
def format_text(text):
    return text

formatted = format_text("Hello World")
print(f"Formatted text: {formatted}")

print("\n" + "="*50)

print("=== 8. CLASS-BASED DECORATOR ===")

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_something():
    return "Something!"

# Call the function multiple times
for i in range(3):
    result = say_something()
    print(f"Result: {result}")

print("\n" + "="*50)
print("🎉 All decorator examples completed!")