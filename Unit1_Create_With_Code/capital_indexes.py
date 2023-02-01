# 1/2/23
# Challenge
# Capital indexes
# Write a function named capital_indexes.
# The function takes a single parameter, which is a string.
# Your function should return a list of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(s):
        if l in upper:
            result.append(i)
    return result
print(capital_indexes("TiTo"))