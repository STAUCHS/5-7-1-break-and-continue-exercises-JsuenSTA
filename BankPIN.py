#-------------------------------------------------------------------------
# Name:       Bank Pin
# Purpose:    Create a program that checks the PIN
# Author:     Suen. J
# Created:    07/05/2024
#-------------------------------------------------------------------------

print("WELCOME TO STA BANK!")

pin = 2024
pin_user = int(input("\nEnter your PIN: ")) 

while True:
    if pin != pin_user :
        print("Incorrect Pin. Try again.")
        pin_user = int(input("\nEnter your PIN: "))
    else:
        break

print("PIN accepted. You may now access your account.") 