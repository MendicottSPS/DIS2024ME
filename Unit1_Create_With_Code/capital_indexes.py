# 1/2/23
# Challenge
# Capital indexes
# Write a function named capital_indexes.
# The function takes a single parameter, which is a string.
# Your function should return a list of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].


print("Welcome to this program!")
print("Here I will let you know the number of capital letters in the title of a book.")
title = input("Please enter the title of the book here: ")

def capital_indexes(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(s):
        if l in upper:
            result.append(i+1)
            return result
print("The capital letters in your title are", capital_indexes(title))



'''
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
'''