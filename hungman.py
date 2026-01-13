import random

words = ["apple", "banana", "mango", "orange", "grapes", "peach"]

secret_word = random.choice(words)
word_length = len(secret_word)

chances = word_length + 2

guessed_letters = []
display_word = ["_"] * word_length

print("Welcome to Hangman Game!")
print("Guess the fruit name")
print("You have", chances, "chances\n")

while chances > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Chances left:", chances)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!\n")
        for i in range(word_length):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!\n")
        chances -= 1
if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game Over! The word was:", secret_word)
