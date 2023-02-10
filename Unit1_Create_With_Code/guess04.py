# what do i need to add?

'''

- need to count turns and end the game or tell the user when they had exceeced the number of urns they have been given
- want to tell the user that they have this many goes and tells them how many they used when the game was finished
    e.g it took you 5 goes to get this number
    how do I do this in a useful way?
    how do I do this in a way that works?
- want to give a difficulty
    e.g different amount of turns based on different difficulties
    how do I do this?
    what is json


'''

import random
num = random.randint(0, 100)
guess = int(input("Take a guess here: "))

while guess != num:
    if guess > 100:
        print("Woah! I said 1-100!")
        guess = int(input("Try a different guess: "))
    elif guess > num:
        print("No, that's too high, try guessing a lower number.")
        guess = int(input("Try a different guess: "))
    elif guess < num:
        print("No, that's too low, try guessing a higher number.")
        guess = int(input("Try a different guess: "))
    else:
        break
print("Yes! That's correct! How amazing are you?! The number was", num, )
