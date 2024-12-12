import random

def start_game():
    secret_number = random.randint(1, 10)
    guess = None
    attempts = 0
    max_attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    print(f"You have {max_attempts} attempts.")

    while guess != secret_number and attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")

    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
    else:
        print(f"Sorry! The correct number was {secret_number}. Better luck next time.")

# Ask if the user wants to play again
while True:
    start_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
