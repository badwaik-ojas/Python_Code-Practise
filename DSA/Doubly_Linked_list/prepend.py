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

    def prepend(self, value):
        # Step 1: Create a new node
        new_node = Node(value)

        # Step 2: Check if the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Step 3: Update references for non-empty list
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node  # Update head to the new node

        # Step 4: Increment the length of the list
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
dll.prepend(50)
dll.prepend(60)
print(dll)

# This would create a list where the head node is 60, followed by 50.
