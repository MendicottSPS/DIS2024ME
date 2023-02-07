# Number guessing game
# Track the number of guesses it takes for the user to get the answer
# Print how many times it took for the user to get the correct answer
# Try 6 guesses to start with
# Wordle is a great example of this

import random
num = random.randint(0, 100)
guess = int(input("Take a guess here: "))

while guess != num:
    if guess < num:
        print("No, that's too low, try guessing a higher number.")
        guess = int(input("Try a different guess: "))
    elif guess > num:
        print("No, that's too high, try guessing a lower number.")
        guess = int(input("Try a different guess: "))
    else:
        break
print("How amazing are you?! You guessed the number correctly!")


'''
print ("Welcome to The Number Guessing game!")
start = input("Do you want to start the game? ")

if  start == 'y' or 'yes':
    guess = input("Okay! Guess the number here: ")
    elif guess = num
    print("How Amazing are you?! You guessed the number correctly!")

    elif guess = > num
    # would add in something like total = total+1
    print("No, that's too high, try guessing another number")

    elif guess = < num
    print("No, that's too low, try guessing another number")

'''




'''
# here need to determine is the number is higher or lower than the user guess
# if the guess is greater than the number then tell the user that the number is lower
# if the guess is lower than the number then tell the user that the number is higher
# if the guess is equal to the number then tell the user that the guess is right

'''