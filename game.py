import random


def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Welcome to Number Guessing Game")
    print("Guess the number between 1 and 10\n")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number\n")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    number_guessing_game()
