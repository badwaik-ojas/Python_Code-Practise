class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]


class QueueViaStack:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        # Move elements from in_stack to out_stack if out_stack is empty
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.push(self.in_stack.pop())

        # If out_stack is still empty, the queue is empty
        if len(self.out_stack) == 0:
            return None

        # Pop the top of out_stack (oldest element in the queue)
        return self.out_stack.pop()

    def __str__(self):
        # Debugging visualization of the queue
        in_stack_items = list(self.in_stack.items)
        out_stack_items = list(self.out_stack.items)
        return f"In-Stack: {in_stack_items}, Out-Stack: {out_stack_items}"

queue = QueueViaStack()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)  # Output: In-Stack: [1, 2, 3], Out-Stack: []

queue.enqueue(4)
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3
print(queue)            # Output: In-Stack: [4], Out-Stack: []
