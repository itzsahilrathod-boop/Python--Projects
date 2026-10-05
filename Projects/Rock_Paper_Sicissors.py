import random


game_images = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]
choices = [0,1,2]


while True:
    user_choice = int(input("What do you choose? Type 0 for Rock,1 for Paper, 2 for Scissors\n "))
    if user_choice  <0 or user_choice > 2:
        print("invalid choice!Try again")
        continue

    print("you chose:")
    print(game_images[user_choice])

    computer_choice = random.choice(choices)
    print("computer chosse")
    print(game_images[computer_choice])


    if user_choice == computer_choice:
        print("It's a tie! Play again.\n")
        continue
    elif(
        (user_choice == 0 and computer_choice == 2)
        or(user_choice == 1 and computer_choice == 0)
        or (user_choice == 2 and computer_choice == 1)
    ):
        print("You  win!")
        break

    else:
        print("Computer Wins!")
        break
