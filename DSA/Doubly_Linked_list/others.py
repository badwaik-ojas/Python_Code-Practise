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
    
    def traverse(self):
        # Step 1: Initialize pointer to the first node (head)
        current_node = self.head

        # Step 2: Traverse and print each node's value
        while current_node:
            print(current_node.value)
            current_node = current_node.next  # Move to the next node

    def reverse_traverse(self):
        # Step 1: Initialize pointer to the last node (tail)
        current_node = self.tail

        # Step 2: Traverse and print each node's value in reverse
        while current_node:
            print(current_node.value)
            current_node = current_node.previous

    def search(self, target):
        current_node = self.head
        index = 0  # Optional index tracking

        while current_node:
            if current_node.value == target:
                return index  # or return True for boolean version
            current_node = current_node.next
            index += 1  # Increment index if tracking position

        return -1  # or return False for boolean version

    def get(self, index):
        # Check for out-of-bounds indices
        if index < 0 or index >= self.length:
            return None
        
        # Determine whether to start from head or tail
        if index < self.length // 2:
            # Start from head for first half
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            # Start from tail for second half
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.previous

        return current_node
    
    def set_value(self, index, value):
        # Retrieve the node at the specified index
        node = self.get(index)
        
        # Check if node is valid (not None)
        if node:
            node.value = value  # Update the node's value
            return True  # Return True to indicate success
        else:
            return False  # Return False if index is invalid
        
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
        
    def insert(self, index, value):
        # Step 1: Handle out-of-bounds indices
        if index < 0 or index > self.length:
            print("Index out of bounds")
            return

        # Step 2: Special cases - inserting at the beginning or end
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return

        # Step 3: Standard insertion in the middle
        new_node = Node(value)
        temp = self.get(index - 1)  # Node before the insertion index
        
        new_node.next = temp.next  # Link new node to the node after `temp`
        new_node.previous = temp       # Set new node's previous to `temp`

        if temp.next:              # Update the `prev` of the following node
            temp.next.previous = new_node

        temp.next = new_node       # Set `temp.next` to the new node
        self.length += 1           # Increment the list length

    def pop_first(self):
        # Step 1: Check if list is empty
        if not self.head:
            return None  # Empty list case

        # Step 2: Create a temporary pointer to the first node
        pop_node = self.head

        # Step 3: Handle the case with only one element
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # Move head to the second node
            self.head = self.head.next
            # Remove backward reference from the new head
            if self.head:
                self.head.prev = None
            # Remove forward reference from the old head (pop_node)
            pop_node.next = None

        # Step 4: Decrease the list length
        self.length -= 1

        # Return the removed node
        return pop_node

    def pop(self):
        # Step 1: Check if list is empty
        if not self.head:
            return None  # Empty list case
        print("1 ",self.head.value)
        print("1 ",self.tail.value)
        # Step 2: Create a temporary pointer to the last node
        pop_node = self.tail

        # Step 3: Handle the case with only one element
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # Move tail to the second last node
            self.tail = self.tail.previous
            print("3 ",self.tail.value)
            # Remove forward reference from the new tail to the removed node
            self.tail.next = None
            # Remove backward reference from the removed node
            pop_node.previous = None

        # Step 4: Decrease the list length
        self.length -= 1
        print("2 ",self.head.value)
        print("2 ",self.tail.value)
        # Return the removed node
        return pop_node

    def remove(self, index):
        # Step 1: Out-of-Bounds Check
        if index < 0 or index >= self.length:
            return None

        # Step 2: Special Cases
        if index == 0:
            return self.pop_first()  # Use existing method to remove first node
        if index == self.length - 1:
            return self.pop()  # Use existing method to remove last node

        # Step 3: Get the Node to Remove
        remove_node = self.get(index)  # Assuming a get method exists
        print(remove_node.value)
        # Step 4: Adjust References
        remove_node.previous.next = remove_node.next
        remove_node.next.previous = remove_node.previous

        # Step 5: Clear Node's References
        remove_node.next = None
        remove_node.previous = None

        # Step 6: Decrease Length
        self.length -= 1

        # Return the removed node
        return remove_node
    



# Example usage
dll = DoublyLinkedList()
dll.prepend(50)
dll.prepend(60)
dll.prepend(70)
dll.prepend(80)
print(dll)
dll.traverse()
dll.reverse_traverse()
print(dll.search(60))
print(dll.get(3))
dll.set_value(1, 100)
print(dll)
dll.insert(2, 150)
print(dll)
dll.pop_first()
print(dll)
dll.pop()
print(dll)
dll.remove(2)
print(dll)

# This would create a list where the head node is 60, followed by 50.
