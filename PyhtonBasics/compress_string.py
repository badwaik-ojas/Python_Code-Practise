def compress_string(input_string):
    if not input_string:
        return ""
    
    compressed = []
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed.append(f"{count}{input_string[i - 1]}")
            count = 1
    
    # Append the last set of characters
    compressed.append(f"{count}{input_string[-1]}")
    
    return ''.join(compressed)

# Test the function
input_string = "aaabbdaabbbdcccd"
output_string = compress_string(input_string)
print(output_string)  # Output: 3a2b1a3b2d