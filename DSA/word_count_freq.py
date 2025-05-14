
def count_word_frequency(words):
    place_holder = {}
    for word in words:
        if word in place_holder:
            place_holder[word] = place_holder.get(word, 0) + 1
    
    return place_holder

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words))
