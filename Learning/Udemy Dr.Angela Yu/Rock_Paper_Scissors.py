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

rps = [rock, paper, scissors]

user_choice = rps[int(input("What do you chose?\nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors\n"))]
compare_user = rps.index(user_choice)

computer_choice = random.choice(rps)
compare_computer = rps.index(computer_choice)

print("You chose\n" + user_choice + "\nComputer chooses\n" + computer_choice)

if compare_user == 0:
    if compare_computer == 0:
        print("\nIts a Tie")
    elif compare_computer == 1:
        print("\nComputer Wins")
    else:
        print("\nUser Wins")
elif compare_user == 1:
    if compare_computer == 0:
        print("\nUser Wins")
    elif compare_computer == 1:
        print("\nIts a Tie")
    else:
        print("\nComputer Wins")
else:
    if compare_computer == 0:
        print("\nComputer Wins")
    elif compare_computer == 1:
        print("\nUser Wins")
    else:
        print("\nIts a Tie")