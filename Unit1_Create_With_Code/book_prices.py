print("Welcome to Amazon's price checker!")
title = input("What is the title? ")
count = len(title.split())
print("The number of words in string are is " + str(count))

if count == 1 or count == 2:
    print("This book is selling really well!")
else:

    print("I would consider purchasing a different book.")