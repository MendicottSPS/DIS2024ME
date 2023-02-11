# Show you how to read from or write to an external file

with open("myTextfile.txt", "r") as file:  # open the file with READ access
    print(file.read())  # read from the file and output to screen
# Where r is for read
mylist = ["a", "b", "c"]  # create a list and populate with items
name = input("What is your name? ")
mylist.append(name)

for item in mylist:  # iterate over each item in the list
    with open("myTextfile.txt", "a") as file:  # open the file with APPEND access
        file.write(item)  # each item in the list (.write(item) is a function or a method
        file.write("\n")  # write a new line (\n writes a new line)

with open("myTextfile.txt", "r") as file:
    print(file.read())


'''
output:
THis is my text file.
a
b
c
THis is another line
a
b
c

'''