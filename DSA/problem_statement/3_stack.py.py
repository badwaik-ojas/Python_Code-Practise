class MultiStack:
    def __init__(self, stack_size):
        self.num_stacks = 3
        self.stack_size = stack_size
        self.custom_list = [0] * (self.num_stacks * self.stack_size)
        self.sizes = [0] * self.num_stacks

    def isFull(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def isEmpty(self, stack_num):
        return self.sizes[stack_num] == 0

    def indexOfTop(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def push(self, stack_num, item):
        if self.isFull(stack_num):
            raise Exception("Stack is full")
        self.sizes[stack_num] += 1
        self.custom_list[self.indexOfTop(stack_num)] = item

    def pop(self, stack_num):
        if self.isEmpty(stack_num):
            raise Exception("Stack is empty")
        top_index = self.indexOfTop(stack_num)
        value = self.custom_list[top_index]
        self.custom_list[top_index] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.isEmpty(stack_num):
            raise Exception("Stack is empty")
        return self.custom_list[self.indexOfTop(stack_num)]


# Testing the MultiStack implementation
stack_size = 3
stacks = MultiStack(stack_size)

# Testing stack operations
stacks.push(0, 10)
stacks.push(0, 20)
stacks.push(0, 30)
stacks.push(1, 30)

print(stacks.peek(0))  # Output: 20
print(stacks.pop(0))   # Output: 20
stacks.push(0, 30)
print(stacks.peek(0))  # Output: 10
print(stacks.isEmpty(1))  # Output: False
print(stacks.isFull(0))   # Output: False
