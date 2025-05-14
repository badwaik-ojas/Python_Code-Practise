def count_words(string):
    # Split the string into words
    words = string.split()

    # Create an empty dictionary to store word counts
    word_counts = {}

    # Iterate through each word and update its count in the dictionary
    for word in words:
        # Remove punctuation and convert to lowercase
        word = word.strip(",.?!").lower()
        # Increment the count of the word in the dictionary
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

# Example usage:
string = "Hello world, hello Python! Python is a powerful programming language."
word_counts = count_words(string)
print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
