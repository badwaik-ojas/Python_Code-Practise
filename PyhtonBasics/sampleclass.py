class PyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello World! My name is {self.name} and I am {self.age} years old")

def main():
    x = PyClass("Ojas", 34)

    print(x.greeting())

    a = input("Input Name")
    b = input("input age")

    c = PyClass(a,b)
    print(c.greeting())

if __name__ == "__main__":
    main()