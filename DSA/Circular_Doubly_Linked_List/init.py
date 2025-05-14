class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)  # Create new node with value
        
        if self.length == 0:  # Case 1: Empty List
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # Point to itself for circularity
            new_node.previous = new_node  # Point to itself for circularity
        else:  # Case 2: Non-Empty List
            new_node.previous = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.previous = new_node
            self.tail = new_node  # Update tail to new node
        
        self.length += 1  # Increment length of the list

    def __str__(self):
        # Step 1: Start from the head of the list
        temp_node = self.head.next
        result = str(self.head.value) + " <-> "
        
        # Step 2: Loop through each node in the list
        while temp_node is not self.head:
            # Append the current node's value to the result
            result += str(temp_node.value)
            
            # Check if there's a next node; if so, add the arrow
            if temp_node.next is not self.head:
                result += " <-> "
            
            
            # Move to the next node
            temp_node = temp_node.next

        # Return the final string representation
        return result
    
    def prepend(self, value):
        new_node = Node(value)  # create new node with given value
        if self.length == 0:
            # Empty list case
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # circular link to itself
            new_node.previous = new_node  # circular link to itself
        else:
            # Non-empty list case
            self.tail.next = new_node  # last node's next points to new node
            self.head.previous = new_node  # first node's previous points to new node
            new_node.previous = self.tail  # new node's previous points to tail
            new_node.next = self.head  # new node's next points to current head
            self.head = new_node  # move head to new node
        self.length += 1

    def traversal(self):
        current_node = self.head  # start from the head node
        while current_node:
            print(current_node.value)  # print the current node’s value
            current_node = current_node.next  # move to the next node
            if current_node == self.head:  # check if we are back at the head
                break  # exit loop when traversal is complete

    def reverse_traversal(self):
        current_node = self.tail  # start from the last node
        while current_node:
            print(current_node.value)  # print the current node’s value
            current_node = current_node.previous  # move to the previous node
            if current_node == self.tail:  # check if we are back at the tail
                break  # exit loop when traversal is complete

    def search(self, target):
        current_node = self.head  # start from the first node
        while current_node:
            if current_node.value == target:  # check if target matches current node’s value
                return True
            current_node = current_node.next  # move to the next node
            if current_node == self.head:  # if we are back to the head, exit the loop
                break
        return False  # target not found
    
    def get(self, index):
        # Edge case handling for invalid index
        if index < 0 or index >= self.length:
            return None

        current_node = None
        
        # Check if index is in the first half
        if index < self.length // 2:
            current_node = self.head
            # Traverse forward from head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            # Traverse backward from tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.previous

        return current_node
    
    def set_value(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Error: Index out of bounds")
            return
        
        new_node = Node(value)
        
        if index == 0:
            self.prepend(value)
            return
        
        if index == self.length:
            self.append(value)
            return

        temp_node = self.get(index - 1)
        new_node.next = temp_node.next
        new_node.previous = temp_node
        temp_node.next.previous = new_node
        temp_node.next = new_node

        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None

        pop_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            pop_node.previous = None
            pop_node.next = None
            self.head.previous = self.tail
            self.tail.next = self.head

        self.length -= 1
        return pop_node
    
    def pop(self):
        if self.length == 0:
            return None

        pop_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            pop_node.next = None
            pop_node.previous = None
            self.tail.next = self.head
            self.head.previous = self.tail

        self.length -= 1
        return pop_node
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        pop_node = self.get(index)
        pop_node.previous.next = pop_node.next
        pop_node.next.previous = pop_node.previous
        pop_node.next = None
        pop_node.previous = None

        self.length -= 1
        return pop_node 
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

cdll = CircularDoublyLinkedList()
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.append(40)
cdll.append(50)
cdll.append(60)
cdll.append(70)
cdll.append(80)
print(cdll)
cdll.prepend(0)
cdll.prepend(-10)
print(cdll)
cdll.traversal()
cdll.reverse_traversal()
print("search 10", cdll.search(10))
print("search 100", cdll.search(100))
print("get element at 0", cdll.get(0).value)
print("get element at 20", cdll.get(20))
cdll.set_value(0, -100)
print("Linked List after set value: ", cdll)
cdll.insert(3, 15)
print("Linked List after insert value value: ", cdll)
print(cdll.pop_first().value)
print("Poped first element, new list: ", cdll)
print(cdll.pop().value)
print("Poped last element, new list: ", cdll)
print(cdll.remove(2))
print("Remove element at 2, new list: ", cdll)
cdll.delete_all()
print(cdll)

