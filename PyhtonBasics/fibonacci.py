def fibonacci_sequence(n):
    sequence = [0, 1]  # Initialize sequence with the first two Fibonacci numbers

    # Generate the Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]  # Calculate the next term
        sequence.append(next_term)

    return sequence

# Example usage:
n_terms = 10  # Number of terms in the Fibonacci sequence
fib_sequence = fibonacci_sequence(n_terms)
print("Fibonacci sequence:")
print(fib_sequence)
