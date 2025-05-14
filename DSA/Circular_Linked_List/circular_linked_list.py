# Class definition for the circular singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # Method to append a new element
    def append(self, value):
        new_node = Node(value)
        
        # Case when the list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # Point the new node to itself
        else:
            # Regular case: List has one or more nodes
            self.tail.next = new_node  # Last node’s next points to new node
            new_node.next = self.head  # New node points to head
            self.tail = new_node       # Update tail to the new node
            
        self.length += 1  # Increment the list length

    def __str__(self):
        # Initialize a temporary node pointing to the head
        temp_node = self.head.next
        # Result string to accumulate node values
        result = str(self.head.value) + " -> "
        
        # Traverse the linked list
        while temp_node is not self.head:
            # Append the current node's value to result
            result += str(temp_node.value)
            # Add an arrow if there is another node after this one
            if temp_node.next is not self.head:
                result += " -> "
            # Move to the next node
            temp_node = temp_node.next
            
        return result
    
    def prepend(self, value):
        # Create a new node with the given value
        new_node = Node(value)
        
        # Case 1: Empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # Points to itself for circular reference
        else:
            # Case 2: Non-empty list
            new_node.next = self.head  # New node points to current first node
            self.head = new_node       # Update head to point to the new node
            self.tail.next = new_node  # Tail should point to new head
        
        # Increase the length of the list
        self.length += 1

    def insert(self, index, value):
        # Edge case: invalid index (negative or greater than length)
        if index < 0 or index > self.length:
            return False
        
        # Create the new node
        new_node = Node(value)
        
        # Edge case: inserting into an empty list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        # Edge case: inserting at the beginning of the list
        elif index == 0:
            self.prepend(value)
        
        # Edge case: inserting at the end of the list
        elif index == self.length:
            self.append(value)
        
        # General case: inserting at a specific index
        else:
            temp_node = self.head
            # Loop until we reach the node just before the specified index
            for _ in range(index - 1):
                temp_node = temp_node.next
            # Link new node to the next node
            new_node.next = temp_node.next
            # Link the current node to the new node
            temp_node.next = new_node

        # Increment length of list
        self.length += 1
        return True
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next 
            if current == self.head:
                break

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:  # Target found
                return True
            
            current = current.next  # Move to the next node
            
            if current == self.head:  # Prevent infinite loop
                break
        
        return False  # Target not found
    
    def get(self, index):
        # Handle out-of-range indices
        if index < -1 or index >= self.length:
            return None
        elif index == -1:  # Return the last node if index is -1
            return self.tail
        
        # Start from the head
        current = self.head
        # Move to the node at the specified index
        for _ in range(index):
            current = current.next
            
        return current
    
    def set_value(self, index, value):
        # Find the node at the given index
        temp = self.get(index)
        
        # Check if node exists
        if temp:
            temp.value = value  # Update the value
            return True  # Update was successful
        else:
            return False

    def pop_first(self):
        # Check if the list is empty
        if self.length == 0:
            return None

        # Save the first node to return it later
        pop_node = self.head

        # Handle case where there is only one node in the list
        if self.length == 1:
            self.head = None
            self.tail = None

        # General case: More than one node in the list
        else:
            # Move head to the second node
            self.head = self.head.next

            # Update tail's next to point to the new head
            self.tail.next = self.head

            # Break the connection of the old head
            pop_node.next = None

        # Decrease length
        self.length -= 1

        # Return the removed node
        return pop_node
    
    def pop(self):
        # Check if the list is empty
        if self.length == 0:
            return None

        # Save the first node to return it later
        pop_node = self.tail

        # Handle case where there is only one node in the list
        if self.length == 1:
            self.head = None
            self.tail = None

        # General case: More than one node in the list
        else:
            # Move head to the second node
            temp = self.head

            while temp.next is not self.tail:
                temp = temp.next

        temp.next = self.head
        self.tail = temp
        # Decrease length
        self.length -= 1

        # Return the removed node
        return pop_node
    
    def remove(self, index):
        # Check if the list is empty
        if self.length == 0:
            return None
        
        pop_node = self.head
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()

        previous_node = self.get(index - 1)
        pop_node = previous_node.next
        previous_node.next = pop_node.next
        pop_node.next = None
        self.length -= 1
                
        return True
    
    def delete_all(self):
        if self.length == 0:
            return  # Early return if the list is already empty
        
        self.tail.next = None  # Break the circular link
        self.head = None       # Remove reference to the first node
        self.tail = None       # Remove reference to the last node
        self.length = 0        # Set the length of the list to zero

    def delete_by_value(self, value):
        if self.length == 0:  # If the list is empty
            return False
 
        # Handle the case where the list has only one node
        if self.head == self.tail and self.head.value == value:
            self.head = None
            self.tail = None
            self.length = 0
            return True
 
        prev = None
        current = self.head
        while True:
            if current.value == value:  # Node to delete is found
                if current == self.head:  # Node is at the head
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                    if current == self.tail:  # Node is at the tail
                        self.tail = prev
                
                self.length -= 1
                return True
 
            prev = current
            current = current.next
            if current == self.head:  # If we have traversed the entire list
                break
 
        return False
    
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        return count

# Initialize an empty circular singly linked list
circular_list = CircularSinglyLinkedList()

# Append some elements
circular_list.append(10)
circular_list.append(20)
circular_list.append(30)
circular_list.append(40)
print(circular_list)
print(circular_list.count_nodes())
print(circular_list.length)
circular_list.prepend(0)
print(circular_list)
circular_list.insert(1, 5)
print(circular_list)
print(circular_list.traverse())
element = 20
flag = "Yes" if circular_list.search(element) else "No"
print(f"Is {element} present: {flag}")
element = 50
flag = "Yes" if circular_list.search(element) else "No"
print(f"Is {element} present: {flag}")
index = 6
print(f"Value at {index} is {circular_list.get(index=index)}")
index = 2
print(f"Value at {index} is {circular_list.get(index=index)}")
print(circular_list)
print(circular_list.pop())
print(circular_list.pop_first())
print(circular_list)
print(circular_list.remove(1))
print(circular_list)
print(circular_list.delete_by_value(10))
print(circular_list.delete_by_value(20))
print(circular_list)






