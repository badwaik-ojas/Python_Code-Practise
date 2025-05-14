def reverse_sentence(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_sentence = ' '.join(reversed(words))  # Reverse the order of words and join them back
    return reversed_sentence

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog"
reversed_sentence = reverse_sentence(sentence)
print("Original sentence:", sentence)
print("Reversed sentence:", reversed_sentence)

print("reverse"+sentence[::-1])
