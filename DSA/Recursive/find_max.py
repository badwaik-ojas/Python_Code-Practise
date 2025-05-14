def find_max_recursive(A, N):
    # Base case: If there's only one element
    if N == 1:
        return A[0]
    # Recursive case: Compare last element with max of the rest
    return max(A[N-1], find_max_recursive(A, N-1))

a = [12,45,23,1,56,10, 44,25]
print("max: ",find_max_recursive(a, len(a)))