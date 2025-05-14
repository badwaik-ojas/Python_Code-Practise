class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def isEmpty(self):
        return self.linked_list.head is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.linked_list.head
        self.linked_list.head = new_node

    def pop(self):
        if self.isEmpty():
            return "No elements to pop"
        popped_value = self.linked_list.head.value
        self.linked_list.head = self.linked_list.head.next
        return popped_value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.linked_list.head.value

    def delete(self):
        self.linked_list.head = None

    def __str__(self):
        current = self.linked_list.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print("print stack: ",stack)
print("pop element: ",stack.pop())
print("print stack after pop: ",stack)
print("peek stack: ",stack)
print("isEmpty: ",stack.isEmpty())
print("delete stack")
stack.delete()





