
# Project 2 – Number Guessing Game
# Author: Nilsu
import random

# TODO: generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)

# TODO: set up a guesses counter
guesses_count = 0

# TODO: get the user's first guess
guess = int(input("Guess a number between 1 and 10: "))
guesses_count += 1

# TODO: while loop – keep asking until the guess is correct
while guess != secret_number:
    # Print "Too low!" or "Too high!" on each wrong guess
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    
    # Get a new guess from the user
    guess = int(input("Try again: "))
    
    # Count each guess
    guesses_count += 1

# TODO: print the congratulations message with the number of guesses
print(f"Congratulations! You found it in {guesses_count} guesses.")