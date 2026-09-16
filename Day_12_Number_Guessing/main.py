import art
import random

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)

def play_guessing_game(attempts_left):

    while attempts_left > 0:
        guess = int(input("Make a guess: "))

        if guess == secret_number:
            print(f"You got it! The answer was {secret_number}.")
            return  #
        elif guess > secret_number:
            print("Too high.")
        elif secret_number > guess:
            print("Too low.")

        attempts_left -= 1

        if attempts_left > 0:
            print("Guess again.")
            print(f"You have {attempts_left} attempts remaining to guess the number.")
        else:

            print(f"You've run out of guesses, you lose. The number was {secret_number}.")


while True:
    difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_choice == "easy":
        total_attempts = 10
        break
    elif difficulty_choice == "hard":
        total_attempts = 5
        break
    else:
        print("Invalid input. Please type 'easy' or 'hard'.")

print(f"You have {total_attempts} attempts remaining to guess the number.")
play_guessing_game(total_attempts)