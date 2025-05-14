# Node class as defined earlier
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList class with insertion methods
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:  # If the list was empty
            self.tail = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, prev_node_value, value):
        current = self.head
        while current and current.value != prev_node_value:
            current = current.next
        if current is None:
            print("Node with value", prev_node_value, "not found.")
            return
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:  # If we added at the end
            self.tail = new_node


linked_list = LinkedList(10)
print("head: ",linked_list.head.value)
print("tail: ",linked_list.tail.value)
print("lenght: ",linked_list.length)
