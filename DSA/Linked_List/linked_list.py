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
        self.len = 0

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

    def __str__(self):
        # Initialize a temporary node pointing to the head
        temp_node = self.head
        # Result string to accumulate node values
        result = ""
        
        # Traverse the linked list
        while temp_node is not None:
            # Append the current node's value to result
            result += str(temp_node.value)
            # Add an arrow if there is another node after this one
            if temp_node.next is not None:
                result += " -> "
            # Move to the next node
            temp_node = temp_node.next
            
        return result

    def append(self, value):
        """Append a new node with the given value to the end of the list."""
        new_node = Node(value)
        
        # If the list is empty, set the new node as head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Traverse to the end of the list and add the new node
            last_node = self.head
            print(value)
            print(self.head.value)
            self.tail.next = new_node
            self.tail = new_node 
        self.len += 1


    def prepend(self, value):
        # Step 1: Create a new node
        new_node = Node(value)

        # Step 2: Check if the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Step 3: Link new node to the current head and update head
            new_node.next = self.head
            self.head = new_node

        # Step 4: Increment the length of the list
        self.len += 1

    def insert(self, index, value):
        # Edge case: invalid index (negative or greater than length)
        if index < 0 or index > self.len:
            return False
        
        # Create the new node
        new_node = Node(value)
        
        # Edge case: inserting into an empty list
        if self.len == 0:
            self.head = new_node
            self.tail = new_node
            print("head: ",self.head.value)
            print("tail: ",self.tail.value)

        # Edge case: inserting at the beginning of the list
        elif index == 0:
            self.prepend(value)
            print("head prepend: ",self.head.value)
            print("tail prepend: ",self.tail.value)
            #new_node.next = self.head
            #self.head = new_node
        
        # Edge case: inserting at the end of the list
        elif index == self.len:
            self.append(value)
            print("head append: ",self.head.value)
            print("tail append: ",self.tail.value)
            #self.tail.next = new_node
            #self.tail = new_node
        
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
        self.len += 1
        return True
    
    def traverse(self):
        current = self.head  # Initialize the traversal from the head node
        while current:       # Continue until current becomes None
            print(current.value)  # Print the value of the current node
            current = current.next

    def search(self, target):
        current = self.head  # Initialize the pointer to the head
        while current:       # Continue until current is None
            if current.value == target:  # Check if current node has target value
                return True              # Target found
            current = current.next       # Move to the next node
        return False 
    
    def search_with_index(self, target):
        current = self.head
        index = 0  # Initialize index
        while current:
            if current.value == target:
                return index  # Return index if target is found
            current = current.next
            index += 1  # Increment index as we move to the next node
        return -1 

    def get(self, index):
        if index < -1 or index >= self.len:
            return None
        elif index == -1:
            return self.tail
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        temp_node = self.get(index)  # Retrieve the node at the specified index
        if temp_node is not None:
            temp_node.value = value  # Update the value
            return True
        return False 
    
    def pop_first(self):
        # Case 1: If the list is empty
        if self.len == 0:
            return None
        
        # Case 2: Store the first node in a temporary variable
        pop_node = self.head
        
        # Case 3: Move the head to the next node
        self.head = self.head.next
        
        # Disconnect the pop_node from the list
        pop_node.next = None
        
        # Case 4: If there was only one node, set tail to None
        if self.len == 1:
            self.tail = None
            
        # Decrease the length and return the removed node
        self.len -= 1
        print("Inside pop first: ",self.tail.value)
        return pop_node
    
    def pop(self):
        # Case 1: Empty list, return None
        if self.len == 0:
            return None

        # Case 2: Single node in the list
        pop_node = self.tail
        if self.len == 1:
            self.head = None
            self.tail = None
        else:
            # Case 3: More than one node
            temp = self.head
            # Loop to find the second-to-last node
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp    # Set the new tail to the second-to-last node
            self.tail.next = None  # Remove reference to the popped node
        
        self.len -= 1  # Decrease length of list
        return pop_node   # Return the popped node
    
    def remove(self, index):
        # Case 1: Index is out of bounds
        print(self.len)
        if index < 0 or index >= self.len:
            return None
        
        # Case 2: Removing the head node
        if index == 0:
            return self.pop_first()

        # Case 3: Removing the last node
        if index == self.len - 1:
            return self.pop()

        # General case: Removing a node in the middle
        previous_node = self.get(index - 1)
        print("Remove: ",previous_node.value)
        pop_node = previous_node.next
        previous_node.next = pop_node.next
        pop_node.next = None  # Remove the link from pop_node
        self.len -= 1

        return pop_node
    
    def delete_all(self):
        self.head = None  # Remove reference to the head node
        self.tail = None  # Remove reference to the tail node
        self.len = 0

    def nth_to_last(self, n):
        pointer1 = self.head
        pointer2 = self.head

        # Move pointer2 n nodes ahead
        for _ in range(n):
            if pointer2 is None:
                return None
            pointer2 = pointer2.next

        # Move both pointers until pointer2 reaches the end
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1  # pointer1 is now at the nth to last node

    def partition(self, x):
        head = self.head
        tail = self.head
        current = self.head

        while current:
            next_node = current.next
            current.next = None  # Isolate the current node

            if current.value < x:
                # Insert node at the beginning (left partition)
                current.next = head
                head = current
            else:
                # Insert node at the end (right partition)
                tail.next = current
                tail = current

            current = next_node

        # Update the list head and tail
        self.head = head
        tail.next = None  # Ensure the last element's next is None

def sum_lists(listA, listB):
    n1, n2 = listA.head, listB.head
    carry = 0
    result_list = LinkedList()

    while n1 or n2 or carry:
        result = carry

        if n1:
            result += n1.value
            n1 = n1.next

        if n2:
            result += n2.value
            n2 = n2.next

        result_list.append(result % 10)
        carry = result // 10

    return result_list

def find_intersection(listA, listB):
    if listA.tail != listB.tail:
        return None  # No intersection if tails are different

    # Find lengths of both lists
    lenA = listA.len
    lenB = listB.len
    print(lenA)
    # Identify shorter and longer lists
    shorter = listA if lenA < lenB else listB
    longer = listB if lenA < lenB else listA

    # Calculate difference in lengths and advance the longer list
    diff = abs(lenA - lenB)
    longer_node = longer.head
    shorter_node = shorter.head

    for _ in range(diff):
        longer_node = longer_node.next

    # Traverse both lists together to find intersection node
    while shorter_node != longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node

def add_same_node(listA, listB, value):
    same_node = Node(value)
    listA.tail.next = same_node
    listA.tail = same_node
    listB.tail.next = same_node
    listB.tail = same_node    

linked_list = LinkedList()

linked_list.insert(0, 10)  # Inserting into an empty list
linked_list.insert(1, 20)  # Insert at end
linked_list.insert(1, 15)  # Insert in the middle
linked_list.insert(0, 5)   # Insert at beginning

print("Linked List after insertions:", linked_list)  # Expected: [5, 10, 15, 20]
print(linked_list.traverse())
print(linked_list.search(10)) 
print(linked_list.search(70)) 
print(linked_list.search_with_index(10)) 
print(linked_list.search_with_index(70)) 
print(linked_list.get(1).value) 
print(linked_list.get(3).value) 
print(linked_list.get(10)) 

print("Set value", linked_list.set_value(3, 50))
print("Get value", linked_list.get(3).value)
print(linked_list) 
print(linked_list.pop_first()) 
print(linked_list) 

print(linked_list) 
print(linked_list.pop()) 
print(linked_list)

linked_list.append(5)
linked_list.append(30)
linked_list.append(45)
linked_list.append(60)

print(linked_list)

# Testing the prepend method
linked_list = LinkedList()
linked_list.prepend(10)
linked_list.prepend(20)
linked_list.prepend(30)

print(linked_list) 

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# Printing the linked list, expecting "10 -> 20 -> 30"
print(linked_list)

linked_list.remove(1)
print(linked_list)


linked_list.delete_all()
print(linked_list)

linked_list.append(5)
linked_list.append(10)
linked_list.append(15)
linked_list.append(20)
linked_list.append(25)
linked_list.append(30)
print(linked_list)

print(linked_list.nth_to_last(2).value)
linked_list.delete_all()

linked_list.append(1)
linked_list.append(3)
linked_list.append(8)
linked_list.append(2)
linked_list.append(5)
linked_list.append(7)
print(linked_list)
linked_list.partition(5)
print(linked_list)

ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(8)

ll2 = LinkedList()
ll2.append(2)
ll2.append(5)
ll2.append(11)

result = sum_lists(ll1, ll2)
print("result: ",result)
intersection = find_intersection(ll1, ll2)
if intersection:
    print("Intersecting node value:", intersection.value)
else:
    print("No intersection found")

ll2.append(8)
add_same_node(ll1, ll2, 7)
print(ll1)
print(ll2)
intersection = find_intersection(ll1, ll2)
if intersection:
    print("Intersecting node value:", intersection.value)
else:
    print("No intersection found")
