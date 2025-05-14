class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        # Step 1: Create a new node with the given value
        new_node = Node(value)
        
        # Step 2: Check if the list is empty
        if not self.head:
            # If the list is empty, new_node is both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Step 3: Link the new node
            self.tail.next = new_node          # Update current tail's next to new node
            new_node.previous = self.tail      # Set new node's previous to current tail
            self.tail = new_node               # Update tail to the new node
        
        # Step 4: Increment length of the list
        self.length += 1

# Example usage
dll = DoublyLinkedList()
dll.append(10)   # Appending first element
dll.append(20)   # Appending second element

print(dll.head.value)        # Output: 10
print(dll.head.next.value)   # Output: 20
print(dll.tail.value)        # Output: 20
