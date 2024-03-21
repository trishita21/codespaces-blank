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

#Write your code below this line 👇

import random

map = [ rock, paper, scissors ]

user_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

print("Your choice is:")
print(map[user_choice])
print("Computer choice is:")
print(map[computer_choice])

if user_choice == computer_choice:
  print("Draw!")
elif user_choice == 0:
  if computer_choice == 1:
    print("You lose!")
  else:
    print("You win!")
elif user_choice == 1:
  if computer_choice == 0:
    print("You win!")
  else:
    print("You lose!")
elif user_choice == 2:
  if computer_choice == 0:
    print("You win!")
  else:
    print("You lose!")
else:
  print("Invalid input!")