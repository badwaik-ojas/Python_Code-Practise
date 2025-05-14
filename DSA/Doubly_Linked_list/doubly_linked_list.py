class Node:
    def __init__(self, value):
        self.value = value      # Store the value of the node
        self.next = None        # Reference to the next node in the list
        self.previous = None    # Reference to the previous node in the list

    def __str__(self):
        # Custom string representation to show previous, current, and next references
        prev_val = self.previous.value if self.previous else "None"
        next_val = self.next.value if self.next else "None"
        return f"{prev_val} <- {self.value} -> {next_val}"

# Example usage:
node = Node(10)
print(node)  # Output: None <- 10 -> None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link nodes
node1.next = node2
node2.previous = node1
node2.next = node3
node3.previous = node2

# Print each node to see the structure
print(node1)  # Output: None <- 10 -> 20
print(node2)  # Output: 10 <- 20 -> 30
print(node3)  # Output: 20 <- 30 -> None    