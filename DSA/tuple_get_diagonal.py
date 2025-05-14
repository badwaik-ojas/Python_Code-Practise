
def get_diagonal(tup):
    output = []
    for i in range(len(tup)):
        output.append(tup[i][i])
        
    return tuple(output)

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)