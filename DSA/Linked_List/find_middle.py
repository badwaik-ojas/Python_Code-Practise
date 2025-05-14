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
            print(temp.value)
            result += str(temp.value)
            if temp.next is not None:
                result += " -> "
            temp = temp.next
        return result

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    
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
            print(self.head.value)
            print(self.tail.value)

        # Step 4: Increment the length of the list
        self.len += 1

linked_list = LinkedList()
linked_list.prepend(10)
linked_list.prepend(20)
linked_list.prepend(30)
linked_list.prepend(40)
linked_list.prepend(50)
linked_list.prepend(60)
print(linked_list)
print(linked_list.find_middle())