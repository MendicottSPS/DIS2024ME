import random

def guess_game():
    print("Welcome to the number guessing game!")
    difficulty = input("Choose difficulty level (easy, medium, hard): ")
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "medium":
        attempts = 7
    else:
        attempts = 5
    print(f"You have {attempts} attempts to guess the number.")
    number = random.randint(1, 100)
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print(f"Congratulations! You've won the game! The number was {number}!")
            break
        elif guess < number:
            print("The number is higher.")
        else:
            print("The number is lower.")
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left.")
    print(f"Thank you for playing the game. The number was {number} Better luck next time.")

guess_game()