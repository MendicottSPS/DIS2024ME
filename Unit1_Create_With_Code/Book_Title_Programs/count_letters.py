# this is a counter

print ("Welcome to my book title counter!")

runagain = "y"
while runagain == "y":
    answer = input("Do you want me to count the characters in the title of the book? ").lower()
    if answer == "yes":
        book = input("What is the title of the book? ")
        length = str(len(book))
        print(f"There are {len(book)} characters in the book title {book} including the spaces.")
    else:
        runagain = "n"
        print("Ok see you next time!")
