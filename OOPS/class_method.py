'''
In Python, class methods are methods that are bound to the class and not the instance of the class. They 
can modify class state that applies across all instances of the class. Class methods take a reference to 
the class itself as the first parameter, conventionally named cls.

To define a class method, you use the @classmethod decorator. The first parameter of a class method is 
always a reference to the class itself, which is passed automatically and can be used to access class 
attributes or other class methods.

Class Variable: class_variable is a class-level attribute that is shared among all instances of the class.

Instance Variable: instance_variable is an instance-level attribute that is unique to each instance of the class.

Uses:
    - Providing alternative constructors (factory methods).
    - Modifying or accessing class-level state.
    - Defining utility methods that pertain to the class rather than instances.

'''

class MyClass:
    class_variable = 0  # Class variable

    def __init__(self, value):
        self.instance_variable = value
        MyClass.class_variable += value

    @classmethod
    def set_class_variable(cls, value):
        cls.class_variable = value

    @classmethod
    def get_class_variable(cls):
        return cls.class_variable

# Create an instance of MyClass
obj1 = MyClass(10)

# Access and modify the class variable using class methods
print(MyClass.get_class_variable())  # Output: 10

MyClass.set_class_variable(20)
print(MyClass.get_class_variable())  # Output: 20

# Create another instance to show that the class variable is shared
obj2 = MyClass(5)
print(MyClass.get_class_variable())  # Output: 25

