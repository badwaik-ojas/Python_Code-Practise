'''
Design a Python function named count_word_frequency to count the frequency of words in a sentence and store the counts in a dictionary.

Input: "hello world hello"
Output: {'hello': 2, 'world': 1}

Input: "the quick brown fox jumps over the lazy dog"
Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
'''

def count_word_frequency(sentence):
    # Your code goes here
    words = sentence.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0)+1
    
    return word_count