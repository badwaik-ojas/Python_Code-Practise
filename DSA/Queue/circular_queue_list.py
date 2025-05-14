class CircularQueue:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.start = -1
        self.top = -1

    def isFull(self):
        return (self.top + 1) % self.max_size == self.start

    def isEmpty(self):
        return self.top == -1

    def enqueue(self, value):
        if self.isFull():
            return "Queue is full"
        if self.start == -1:  # First element
            self.start = 0
        self.top = (self.top + 1) % self.max_size
        self.items[self.top] = value
        return "Inserted"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        removed_item = self.items[self.start]
        self.items[self.start] = None  # Optional cleanup
        if self.start == self.top:  # Queue becomes empty
            self.start = -1
            self.top = -1
        else:
            self.start = (self.start + 1) % self.max_size
        return removed_item

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items[self.start]

    def delete(self):
        self.items = [None] * self.max_size
        self.start = -1
        self.top = -1

# Initialize a Circular Queue
queue = CircularQueue(3)

# Enqueue Operations
print(queue.enqueue(1))  # Inserted
print(queue.enqueue(2))  # Inserted
print(queue.enqueue(3))  # Inserted
print(queue.enqueue(4))  # Queue is full

# Peek and Dequeue Operations
print(queue.peek())      # 1
print(queue.dequeue())   # 1
print(queue.peek())      # 2
print(queue.enqueue(3))  # Inserted
print(queue.enqueue(4))  # Queue is full

# Check Queue Status
print(queue.isEmpty())   # False
print(queue.isFull())    # False

# Delete Queue
queue.delete()
print(queue.isEmpty())   # True
