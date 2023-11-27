import random
print("Welcome to Rock Paper and Scissors game")
rock = """
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
PAPER
         _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
SCISSORS
       _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices_list = [rock, paper, scissors]

user_choice = choices_list[int(input("Enter your choice: 0 for rock, 1 for paper, 2 for scissors"))]
computer_choice = choices_list[random.randint(0, len(choices_list))]
print("Computer Choice: ", computer_choice)
print("User Choice: ", user_choice)

if computer_choice == user_choice:
    print("Its a Draw")
if computer_choice == choices_list[0] and user_choice == choices_list[1]:
    print("User Won")
if computer_choice == choices_list[0] and user_choice == choices_list[2]:
    print("Computer Won")
if computer_choice == choices_list[2] and user_choice == choices_list[0]:
    print("User Won")
if computer_choice == choices_list[1] and user_choice == choices_list[2]:
    print("User Won")
if computer_choice == choices_list[2] and user_choice == choices_list[1]:
    print("Computer Won")
if computer_choice == choices_list[1] and user_choice == choices_list[0]:
    print("Computer Won")




