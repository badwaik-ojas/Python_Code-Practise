def word_count_from_file(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;:"\'')
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(word_count_from_file('PyhtonBasics\word_count_text.txt'))

