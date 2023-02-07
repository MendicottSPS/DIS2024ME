
import random
num = random.randint(0, 100)
print("Welcome to the number guessing game!")
print("Here you will have 7 chances to guess the number correctly. Good luck!")
print(num)

count = 0

while True:
    count = count +1
    if count > 7:
        print("You have exceeded the number of guesses! THe number was", num)
    guess = int(input("Guess a number between 1 and 100. Take a guess here: "))

    '''
    while guess != num:
        if guess == num:
        print("How amazing are you?! You guessed the number correctly in", count, "turn(s)!")
        break

        elif guess < num:
        print("No, that's too low, try guessing a higher number.")
        guess = int(input("Try a different guess: "))

        elif guess > num:
        print("No, that's too high, try guessing a lower number.")
        guess = int(input("Try a different guess: "))

        else:
        print("I'm not sure whats going on!")
        '''
