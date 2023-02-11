# fourth trial test of the number guessing game using a scoring system
# This one doesn't tell you if you got the answer right or not, when you get the answer right, the program just ends

import random
num = random.randint(0, 100)
guess = int(input("Take a guess here: "))
made_guesses = 7
count = 0

print(num)

while guess != num:
    if count == 6:
        print("You have exceeded the number of guesses! The number was", num)
        guess = int(input("Guess a number between 1 and 100. Take a guess here: "))
    elif guess > num:
        print("No, that's too high, try guessing a lower number.")
        guess = int(input("Try a different guess: "))
        made_guesses = made_guesses - 1
        count += 1
    elif guess < num:
        print("No, that's too low, try guessing a higher number.")
        guess = int(input("Try a different guess: "))
        count += 1
    elif guess > 100:
        print("Woah! I said 1-100!")
        guess = int(input("Try a different guess: "))
        made_guesses = made_guesses - 1
        count += 1
    else:
        count += 1
        print("Yes! That's correct! How amazing are you?! ")
        print("The number was", num, "!")
        print("It took you", count, "guesses")
        break

