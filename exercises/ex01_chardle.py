"""chardle, wordle knock off"""

__author__="730614197"

word: str = input("enter a 5 letter word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("enter a single character: ")
if len(character) != 1:
    print("Error: character must be a single character")
    exit()
print("Searching for " + character + " in  " + word)

i: int = 0

if character[0] == word[0]:
    print(character + " found at index 0")
    i += 1
if character[0] == word[1]:
    print (character + " found at index 1")
    i += 1
if character[0] == word[2]:
    print (character + " found at index 2")
    i += 1
if character[0] == word[3]:
    print (character + " found at index 3")
    i += 1
if character[0] == word[4]:
    print (character + " found at index 4")
    i += 1
print(str(i) + " instances of " + character + " found in " + word)

