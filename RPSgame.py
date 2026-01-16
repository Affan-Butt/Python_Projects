# Rock Paper Scissors Game
import random
print("winning rules of the game ")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors")
    choice = int(input("Enter your choice: "))
    while choice > 3 or choice < 1:
        choice = int(input("Invalid choice. Please enter 1, 2, or 3: "))
    if choice == 1:
        user_choice = 'Rock'
    elif choice == 2:
        user_choice = 'Paper'
    elif choice == 3:
        user_choice = 'Scissors'
    print('Your choice is', user_choice)
    print("\nNow it's computer's turn...")
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice_name = 'Rock'
    elif computer_choice == 2:
        computer_choice_name = 'Paper'
    elif computer_choice == 3:
        computer_choice_name = 'Scissors'
    print("Computer's choice is", computer_choice_name)
    print(user_choice, "vs", computer_choice_name)
    if user_choice == computer_choice_name:
        print("It's a tie!")
    elif (user_choice == 'Rock' and computer_choice_name == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice_name == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice_name == 'Paper'):
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break
