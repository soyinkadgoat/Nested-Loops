string = input("Enter your own word: ")
character = input("Enter your own character to search: ")

i = 0
count = 0

while i < len(string):

    if string[i] == character:
        count = count + 1
    i = i + 1

print("The total number of times ", character, " has occured = ", count)