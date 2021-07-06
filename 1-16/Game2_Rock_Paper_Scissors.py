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

names = ['rock', 'paper', 'scissors']

deck = [rock, paper, scissors]
ai_choice = random.randint(0, 2)

print("This is a game, Rock paper scissors")
user_input = int(input("if you wanna play, Write '1' for Rock, '2' for Paper, '3' for scissors: "))
user_correction = user_input-1


# Player choice
print(f"Your choice is: {user_input} " + names[user_correction] + deck[user_correction])

# Ai choice
print(f"AI choice is: {ai_choice+1} " + names[ai_choice] + deck[ai_choice])
print(user_input, ai_choice+1)

if user_input == 1:
    if ai_choice == 0:
        print("Even")
    elif ai_choice == 2:
        print("You win")
    elif ai_choice == 1:
        print("You lose")

elif user_input == 2:
    if ai_choice == 1:
        print("Even")
    elif ai_choice == 1:
        print("You win")
    elif ai_choice == 2:
        print("You lose")

elif user_input == 3:
    if ai_choice == 2:
        print("Even")
    elif ai_choice == 1:
        print("You win")
    elif ai_choice == 0:
        print("You lose")

