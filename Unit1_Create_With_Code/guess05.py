import random
num = random.randint(0, 100)


print(f'''
========================================
Welcome to this number guessing game!''')
name = input("Tell me your name: ")
print(f'''
Alright, {name}, you will have 7 changes to guess the number correctly. Good Luck!!
========================================
''')
count = 0
game_guesses = 7
print(num)

guess = int(input("Guess a number between 1 and 100. Take a guess here: "))

while True:
    count = count+1
    game_guesses = game_guesses-1
    if count == 7:
        print("Oh dear, you have exceeded the number of guesses! The number was", num)
        break
# while guess != num:
    if guess == num:
        print("How amazing are you?! You guessed the number correctly in", count, "tries! You had", game_guesses, "tries left!")
        break
    elif guess < num:
        print("No, that's too low, try guessing a higher number.")
        guess = int(input("Try a different guess: "))
    elif guess > num:
        print("No, that's too high, try guessing a lower number.")
        guess = int(input("Try a different guess: "))
    else:
        print("!")
