'''

Creating a Stack in Python
    Using a Python list without size limit
    Using a Python list with size limit
    Using a linked list
'''

# Using a Python list without size limit

class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.stack = []
    
    def __str__(self):
        # Customize the string output to display the stack vertically
        stack_representation = "\n".join(map(str, reversed(self.stack)))
        return stack_representation if stack_representation else "Stack is empty"
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            return "No elements to pop"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def delete(self):
        self.stack = []

# Example Usage
stack = Stack()
print("When Empty: ",stack)  # Output: "Stack is empty"
print("isEmpty: ", stack.isEmpty())
stack.stack = [10, 20, 30]  # Pretend we've pushed these values
print("When it has value:\n",stack)
print("isEmpty: ", stack.isEmpty())
stack.push(40)
print("after append: ",stack)
stack.pop()
print("after pop: ",stack)
print("peek: ",stack.peek())
print("delete: ", stack.delete())