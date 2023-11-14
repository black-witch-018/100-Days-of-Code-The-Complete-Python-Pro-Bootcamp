from rock_paper_scissors_ascii import rock_paper_scissors
import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"You chose:\n{rock_paper_scissors[player_choice]}")

computer_choice = random.randint(0,len(rock_paper_scissors)-1)
# Below line for testing the code
# computer_choice = 2
print(f"Computer chose:\n{rock_paper_scissors[computer_choice]}")

if computer_choice == player_choice:
    print("It's a draw")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
elif player_choice > 2 and player_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("You lose!")
