
runagain = 'y'
while runagain == 'y':
    answer = input("Do you want me to run? ")
    if answer == "yes" or "Yes":
        title = input("Please enter the title of the book here: ")
        def capital_indexes(s):
            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = []
            for i, l in enumerate(s):
                if l in upper:
                    result.append(i)
                    return result
        print("The capital letters in your title are", capital_indexes(title))
else:
    runagain == 'n'
    print("Ok see you next time!")
