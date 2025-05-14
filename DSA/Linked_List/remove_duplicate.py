'''
The approach, often called the "fast and slow pointer" technique or "tortoise and hare" algorithm, allows you to 
traverse the list only once, instead of first counting the elements and then accessing the middle one.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __str__(self):
        temp = self.head
        result = ""
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += " -> "
            temp = temp.next
        return result

    def remove_dupliate(self):
        if self.head is None:
            return
        node_values = set()
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:
                current_node.next = current_node.next.next
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node
    
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

linked_list = LinkedList()
linked_list.prepend(10)
linked_list.prepend(20)
linked_list.prepend(30)
linked_list.prepend(20)
linked_list.prepend(20)
linked_list.prepend(30)
print(linked_list)
linked_list.remove_dupliate()
print(linked_list)