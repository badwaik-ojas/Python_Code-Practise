# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

# Queue class
class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        return " -> ".join([str(value) for value in self.linked_list])

    def enqueue(self, value):
        new_node = Node(value)
        if self.linked_list.head is None:  # If queue is empty
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:  # Add to the end
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

    def is_empty(self):
        return self.linked_list.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.linked_list.head is None:  # If queue is empty
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:  # Add to the end
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty. No nodes to dequeue."
        temp_node = self.linked_list.head
        if self.linked_list.head == self.linked_list.tail:  # Only one node
            self.linked_list.head = None
            self.linked_list.tail = None
        else:  # More than one node
            self.linked_list.head = self.linked_list.head.next
        return temp_node.value

    def peek(self):
        if self.is_empty():
            return "Queue is empty. No nodes to peek."
        return self.linked_list.head.value

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None

# Test the implementation
custom_queue = Queue()
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
print(custom_queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
print(q.is_empty()) # Output: False
q.delete()
print(q.is_empty()) # Output: True

