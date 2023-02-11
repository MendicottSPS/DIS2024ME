# one of the last attempts using a txt file to store information about game users

import random

def write_to_file(name, score):
    with open("scores.txt", "a") as file:
        file.write(f"{name},{score}\n")

def get_previous_score(name):
    with open("scores.txt", "r") as file:
        for line in file:
            line_name, score = line.strip().split(",")
            if line_name = name:
                return int(score)
            return None

def game_start():
    number = random.randint(1,100)
    guesses_left = 0
    while guesses_left not in [7, 5, 3]:
        difficulty = input("Select a difficulty to play (easy=7, medium=5, hard=3): ")
        try:
            guesses_left = int(difficulty)
        except ValueError:
            pass

    print(f"I'm thinking of a number between 1 and 100. You have {guesses_left} guesses.")

    name = input("What is your name? ")
    previous_score = get_previous_score(name)

    if previous_score is not None:
        print(f"Last time you played, you scored {previous_score}.")

    while guesses_left > 0:
        guess = int(input("Guess a number here: "))
        if guess == number:
            score = 7 - guesses_left + 1
            print(f"You got it! The number was {number}!")
            write_to_file(name, score)
            break
        elif guess < number:
            print("The number is higher.")
        else:
            print("The number is lower.")
        guesses_left -= 1

    if guesses_left == 0
        print(f"You have run out of guesses! The number was {number}.")

game_start()
