'''
Encapsulation allows you to bundle data and methods into a single unit and control access 
to the internal state of an object. By using public, protected, 
and private members, you can ensure that the data is accessed and modified only through well-defined 
interfaces, leading to more secure, maintainable, and understandable code.

Key Concepts of Encapsulation:
    Data Hiding: 
        Encapsulation allows the internal state of an object to be hidden from the outside. 
        This prevents the outside code from directly accessing and modifying the internal state 
        of the object.

    Public, Protected, and Private Members: 
        In Python, encapsulation is achieved through the use of access specifiers:
            Public members: Accessible from outside the class.
            Protected members: Indicated by a single underscore _ prefix. Intended to be used within 
            the class and its subclasses.
            Private members: Indicated by a double underscore __ prefix. Intended to be inaccessible 
            from outside the class.
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make          # Public attribute

        '''
        Protected Attribute: _model is a protected attribute and is intended for use within the class 
        and its subclasses. It can still be accessed from outside the class, but this is not recommended.
        '''
        self._model = model       # Protected attribute

        '''
        Private Attribute: __year is a private attribute and cannot be accessed directly from outside the 
        class. Accessing it directly will result in an AttributeError. It can still be accessed using name 
        mangling (_ClassName__attribute), but this is also not recommended.
        '''
        self.__year = year        # Private attribute

    # Public method
    def display_info(self):
        return f"{self.make} {self._model} {self.__year}"

    # Private method
    '''
    Private Method: __calculate_age is a private method and cannot be accessed directly from outside 
    the class. It can only be accessed through a public method like get_car_age.
    '''
    def __calculate_age(self):
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.__year

    # Public method to access private method
    def get_car_age(self):
        return self.__calculate_age()

# Create an instance of Car
my_car = Car("Toyota", "Corolla", 2015)

# Accessing public attribute and method
print(my_car.make)                # Output: Toyota
print(my_car.display_info())      # Output: Toyota Corolla 2015

# Accessing protected attribute (not recommended)
print(my_car._model)              # Output: Corolla

# Accessing private attribute directly will result in an AttributeError
# print(my_car.__year)            # AttributeError

# Accessing private attribute using name mangling
print(my_car._Car__year)          # Output: 2015

# Accessing private method through a public method
print(my_car.get_car_age())       # Output: Car's age in years

'''
Why Use Encapsulation?

    Control Access to Data: 
        Encapsulation helps to control the access to the data. This ensures that the data cannot be changed 
        without validation or other checks.

    Maintainability and Flexibility: 
        By restricting direct access to the internal state, the implementation details can be changed without 
        affecting the outside code that uses the class.

    Improved Security: 
        Encapsulation protects the internal state of the object from unintended or harmful changes.

    Modularity: 
        Encapsulation leads to a modular approach where different parts of a program are isolated from each 
        other, making the code easier to manage and understand.

'''

'''
Advantages of Encapsulation:

    Improved Data Security: 
        By hiding the internal state and requiring all interaction to occur through methods, encapsulation 
        protects the data from being altered accidentally or maliciously.

    Data Validation: 
        Methods can include checks to validate the data before it is modified, ensuring that only valid data 
        is stored.

    Ease of Maintenance: 
        Encapsulation allows the internal implementation to be changed without affecting the external code 
        that uses the class. This makes the code more maintainable and adaptable to changes.

    Reduced Complexity: 
        By exposing only what is necessary, encapsulation reduces the complexity of the code. Users of the 
        class do not need to understand the internal workings to use it effectively.
'''
