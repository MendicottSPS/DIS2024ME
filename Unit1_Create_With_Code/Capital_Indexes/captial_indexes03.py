'''
NOTES:
eg.
for index, name in enumerate(names):
    print(index)
    print(name)

myname = "Mollie"
print(myname[3])
=== l

[:2] == up to the second index value
[2:] == from the second value onwards

for i, char in enumerate(myname):
print(i, char)
{at i+1 to make the list more meaningful for a human to understand}

enumerate allows you to see the name and the index values for the item in the list

mytitle = input("Let me know the title of the book: ")
for i, char in enumerate(mytitle):
    print(i+1, char)

'''

# This one works the best
# Still doesnt work the way I want it to
# Does not loop
# Does not ask the user to input over and over again


print("Welcome to this program!")
print("Here I will let you know the number of capital letters in the title of a book.")
title = input("Please enter the title of the book here: ")
def capital_indexes(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(s):
        if l in upper:
            result.append(i)
    return result
print(capital_indexes(title))
