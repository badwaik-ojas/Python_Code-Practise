import random
import hangman_words
import hangman_logo

# intro
print(f"Welcome to the Game!\n {hangman_logo.logo}")

# variables
choosen_word = random.choice(hangman_words.my_list)
word_length = len(choosen_word)
display = []
guess_count = int(len(hangman_logo.stages)) - 1
print(f"You have {guess_count} guesses")

# hint
print("Choosen Word: ",choosen_word)

# display word length using underscore
for _ in range(word_length):
    display.append("_")
print(display)

# set flag
flag = False
while (not flag):
    # take input from user
    guess = input("Guess a letter:\n").lower()
    for ind in range(word_length):
        letter = choosen_word[ind]
        if letter == guess:
            display[ind] = letter
    if guess not in display:
        print(hangman_logo.stages[guess_count])
        guess_count -= 1
        print("guess left: ",guess_count )
        if guess_count == 0:
            flag = True
            print("You don't have lives left, You lost")
    if "_" not in display:
        flag = True
        print("Congrats! You Won")
        
    print(display)