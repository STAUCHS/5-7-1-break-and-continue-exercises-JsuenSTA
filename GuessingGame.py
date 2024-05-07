#-------------------------------------------------------------------------
# Name:        Guessing game
# Purpose:     Guest the correct number under 5 tries
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

import random 
number = random.randrange(1, 101)
print("*** Guess the Number *** ")
print("Welcome to the guess the number game.")
print("You have 5 chances to guess the number between 1 and 100.")

answer = int(input("\nEnter a number between 1 and 100: "))
for i in range(5):
    if number < answer : 
        print("Too high, guess again") 
        answer = int(input("\nEnter a number between 1 and 100: "))
    elif number > answer : 
        print("Too low, guess again")
    else:
        break
    if i == 5:
        print(f"Sorry, you've guessed incorrectly, the number is {number}.")

print("Congrats!")




