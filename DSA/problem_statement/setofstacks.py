class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum capacity of each stack
        self.stacks = []          # List of stacks

    def push(self, item):
        # If no stacks or the last stack is full, create a new stack
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])  # Create a new stack
        self.stacks[-1].append(item)  # Push item onto the last stack

    def pop(self):
        # If no stacks, return None
        if not self.stacks:
            return None
        item = self.stacks[-1].pop()  # Pop from the last stack
        if len(self.stacks[-1]) == 0:  # Remove the stack if it's empty
            self.stacks.pop()
        return item

    def popAt(self, index):
        # Validate the index
        if index < 0 or index >= len(self.stacks) or len(self.stacks[index]) == 0:
            return None
        item = self.stacks[index].pop()  # Pop from the specific stack
        if len(self.stacks[index]) == 0:  # Remove the stack if it's empty
            del self.stacks[index]
        return item

    def __str__(self):
        return str(self.stacks)  # Visualize the stacks for debugging

stacks = SetOfStacks(2)  # Each stack has a capacity of 2
stacks.push(1)  # Push onto stack 1
stacks.push(2)  # Push onto stack 1
stacks.push(3)  # Stack 1 is full; create stack 2 and push
stacks.push(4)  # Push onto stack 2
print(stacks)   # Output: [[1, 2], [3, 4]]

print(stacks.pop())  # Output: 4 (from stack 2)
print(stacks)        # Output: [[1, 2], [3]]

print(stacks.popAt(0))  # Output: 2 (from stack 1)
print(stacks)           # Output: [[1], [3]]
