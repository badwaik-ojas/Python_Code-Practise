"""
Decorators
    Decorators provide a simple syntax for calling higher-order functions.
    By definition, a decorator is a function that takes another function and extends the behavior of the 
    latter function without explicitly modifying it.
    A decorator in Python is a function that takes another function as its argument, and returns yet another function.
    Decorators can be extremely useful as they allow the extension of an existing function, without any 
    modification to the original function source code.
    
    In fact, there are two types of decorators in Python including class decorators and function decorators.
    In application, decorators are majorly used in creating middle layer in the backend, it performs task like token authentication, validation, image compression and many more.
"""

def my_decorator(func):
    def test():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return test

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

"""
my_decorator is a decorator function that takes func as an argument and defines a nested function 
wrapper.

wrapper is the inner function that adds functionality before and after calling func.

@my_decorator is used to decorate the say_hello function.

When say_hello is called, it actually calls wrapper, which in turn calls say_hello within its 
functionality.
"""

"""
Decorators are commonly used for tasks such as logging, authentication, memoization, access control, 
and more. They help keep the code clean and modular by separating concerns and promoting reusable 
components.
"""

