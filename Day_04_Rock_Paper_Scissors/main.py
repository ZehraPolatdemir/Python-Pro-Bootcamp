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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
game_images=[rock,paper,scissors]
computer_choice = random.randint(0, 2)

if user_choice in [0,1,2]:
    print("\nComputer chose:")
    print(game_images[computer_choice])
    print("Your choose:")
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)


    if user_choice ==  computer_choice:
        print("It's a draw")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")

else:
    print("\nPlease use valid numbers.")