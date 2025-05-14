# Node class as defined earlier
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList class with optional initial node
class LinkedList:
    def __init__(self, value=None):
        if value is not None:  # Initialize with one node
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:  # Initialize empty linked list
            self.head = None
            self.tail = None
            self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1



# Example usage
# Creating a Linked List with one node
linked_list = LinkedList(10)
print("Head Value:", linked_list.head.value)  # Output: 10
print("Tail Value:", linked_list.tail.value)  # Output: 10
print("Length:", linked_list.length)  # Output: 1

# Creating an empty Linked List
empty_list = LinkedList()
print("Head:", empty_list.head)  # Output: None
print("Tail:", empty_list.tail)  # Output: None
print("Length:", empty_list.length)  # Output: 0
