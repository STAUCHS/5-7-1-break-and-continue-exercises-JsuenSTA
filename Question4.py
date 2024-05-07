#-------------------------------------------------------------------------
# Name:       Infinite copy and paste
# Purpose:     Copy and paste the word user typed until user says stop
# Author:     Suen. J
# Created:    07/05/2024
#-------------------------------------------------------------------------

while True:
    word = str(input("Enter a word: ")) 

    if word == "stop":
        break
    else:
        print(f"Your word: {word}") 

print("Good Bye!")

    