class Queue:
    def __init__(self):
        self.items = []  # Initialize an empty list to represent the queue.

    def __str__(self):
        return ' '.join([str(item) for item in self.items])
    
    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)
        return f"Element {value} added to the queue."

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty. Cannot dequeue."
        return self.items.pop(0)  # Removes and returns the first element.

    def peek(self):
        if self.isEmpty():
            return "Queue is empty."
        return self.items[0]  # Returns the first element without removing it.
    
    def delete(self):
        self.items = None  # Removes all elements by setting the queue to None.
        return "Queue deleted."
    
# Create an empty queue
queue = Queue()

# Check if the queue is empty
print(queue.isEmpty())  # Output: True

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)  # Output: 1 2 3

# Peek the first element
print(queue.peek())  # Output: 1

# Dequeue an element
print(queue.dequeue())  # Output: 1
print(queue)  # Output: 2 3

# Delete the queue
print(queue.delete())  # Output: Queue deleted.


