def find_duplicates(numbers):
    frequency = {}
    duplicates = []

    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    for num, count in frequency.items():
        if count > 1:
            duplicates.append(num)

    if duplicates:
        print("Duplicate numbers:", duplicates)
    else:
        print("No duplicates found")

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9]
find_duplicates(numbers_list)
