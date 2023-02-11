# one of the last attempts using a txt file to store information about game users

import random
# allows the import of a random number


# This is where the game will write the player's score in a txt file to store until they play the game again
def write_to_file(name, score):
    with open("scores.txt", "a") as file:
        file.write(f"{name},{score}\n")


# This is used to check if the user that is playing has played before, and if they have, it will return their score
def get_previous_score(name):
    with open("scores.txt", "r") as file:
        # This part was difficult, each time I played the game, it was not telling me my most recent score
        # I found a solution that splits the line into two 'parts' based on the comma
        # The split method meant that parts[0] would contain the user's name and parts[1] would contain their score
        lines = file.readlines()
        lines.reverse()
        for line in lines:
            parts = line.strip().split(",")
            # Here if the part[0] which is the user's name was equal to the name that had just been input,
            # The function would return the score which is stored in parts[1]
            if parts[0] == name:
                return int(parts[1])
    return None


def game_start():
    number = random.randint(1, 100)
    guesses_left = 0
    while guesses_left not in [7, 5, 3]:
        difficulty = input("Select a number of guesses to determine your difficulty (easy=7, medium=5, hard=3): ")
        try:
            guesses_left = int(difficulty)
        except ValueError:
            pass

    print(f"I'm thinking of a number between 1 and 100. You have {guesses_left} guesses.")

    name = input("What is your name? ")
    previous_score = get_previous_score(name)

    if previous_score is not None:
        print(f"Hi {name}, welcome back! Last time you played, you scored {previous_score}.")

    while guesses_left > 0:
        guess = int(input("Guess a number here: "))
        if guess == number:
            score = 7 - guesses_left + 1
            print(f"You got it! The number was {number}!")
            write_to_file(name, score)
            break
        elif guess < number:
            print(f"The number is higher. You have {guesses_left} guesses remaining.")
        else:
            print(f"The number is lower. You have {guesses_left} guesses remaining.")
        guesses_left -= 1

    if guesses_left == 0:
        print(f"You have run out of guesses! The number was {number}.")


game_start()
