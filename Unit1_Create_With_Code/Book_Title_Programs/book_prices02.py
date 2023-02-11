# Second Attempt
print("Welcome to Amazon's price checker!")

runagain = 'y'
while runagain == 'y':
    answer = input("Do you want me to count the words in the title? ").lower()
    if answer == "yes":
        title = input("What is the title? ")
        count = len(title.split())
        print("The number of words in string are is " + str(count))
        if count == 5:
            print("This book is selling really well!")
        else:
            print("I would consider purchasing a different book.")