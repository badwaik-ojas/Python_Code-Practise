class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.len = 1

    def __str__(self):
        temp = self.head
        result = ""
        while temp is not None:
            result = str(temp.value)
            if temp.next is not None:
                result += " -> "
            temp = temp.next
        return result
    
print(LinkedList(10))