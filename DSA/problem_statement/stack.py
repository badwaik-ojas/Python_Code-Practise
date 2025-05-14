class Node:
    def __init__(self, value, min_value):
        self.value = value
        self.min_value = min_value
        self.next = None

class MinStack:
    def __init__(self):
        self.top = None  # Points to the top of the stack
    
    def push(self, item):
        if self.top is None:
            # Stack is empty; the pushed item is also the minimum
            new_node = Node(item, item)
        else:
            # Compare the item with the current minimum
            current_min = self.top.min_value
            new_min = min(item, current_min)
            new_node = Node(item, new_min)
            new_node.next = self.top  # Link the new node to the current top
        self.top = new_node  # Update the top pointer
    
    def pop(self):
        if self.top is None:
            return None  # Stack is empty
        popped_value = self.top.value
        self.top = self.top.next  # Move the top pointer to the next node
        return popped_value
    
    def minimum(self):
        if self.top is None:
            return None  # Stack is empty
        return self.top.min_value  # Return the minimum value from the top node

stack = MinStack()
stack.push(10)
stack.push(15)
stack.push(5)
stack.push(25)
stack.push(0)
stack.push(8)

print(stack.minimum())

stack.pop()
stack.pop()
print(stack.minimum())

