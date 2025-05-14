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
        # Append method logic here
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

    def __str__(self):
        # Step 1: Start from the head of the list
        temp_node = self.head
        result = ""
        
        # Step 2: Loop through each node in the list
        while temp_node:
            # Append the current node's value to the result
            result += str(temp_node.value)
            
            # Check if there's a next node; if so, add the arrow
            if temp_node.next:
                result += " <-> "
            
            # Move to the next node
            temp_node = temp_node.next

        # Return the final string representation
        return result

# Example usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print(dll)  # Output: "10 <-> 20 <-> 30"
