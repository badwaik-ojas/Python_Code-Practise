class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSingleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node  # Points to itself
        self.head = new_node
        self.tail = new_node
        self.length = 1

circular_list = CircularSingleLinkedList(10)
print(circular_list.head.value)  # Output: 10

class CircularSingleLinkedList_Empty:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

circular_list_Empty = CircularSingleLinkedList_Empty()
val = circular_list_Empty if circular_list_Empty is not None else "None"
print(val)