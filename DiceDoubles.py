#-------------------------------------------------------------------------
# Name:       Dice double 
# Purpose:    Guess the dice 
# Author:     Suen. J
# Created:    07/05/2024
#-------------------------------------------------------------------------
import random

print("HERE COMES THE DICE!")

for i in range(4):
    roll_1 = random.randrange(1,7)
    roll_2 = random.randrange(1,7)

    print(f"\nRoll#1: {roll_1}")
    print(f"Roll#2: {roll_2}")
    sum = roll_1  + roll_2
    print(f"The total is {sum}")
