import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

human_input = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for Scissor\n"))
print("Human Input: ",game_images[human_input])

computer_input = random.randint(0,2)
print("Computer Input: ",game_images[computer_input])

if human_input >= 3:
    print("Invalid Input")
elif human_input == computer_input:
    print("Its a Tie!")
elif human_input == 2:
    if computer_input == 0:
        print("Compter Won!")
    else:
        print("Human Won!")
elif human_input == 1:
    if computer_input == 2:
        print("Compter Won!")
    else:
        print("Human Won!")
elif human_input == 0:
    if computer_input == 2:
        print("Compter Won!")
    else:
        print("Human Won!")
