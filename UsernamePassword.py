#-------------------------------------------------------------------------
# Name:       Username and password
# Purpose:    Enter the right username and password
# Author:     Suen. J
# Created:    07/05/2024
#-------------------------------------------------------------------------

username = "StAugustineCHS"
password = "Coding123!"

username_user = str(input("\nEnter your username: "))
password_user = str(input("Enter your password: "))

while True:
    if username != username_user and password != password_user:
        print("Username and password incorrect.")
        username_user = str(input("\nEnter your username: "))
        password_user = str(input("Enter your password: "))
    elif username != username_user:
        print("Username incorrect. ")
        username_user = str(input("\nEnter your username: "))
        password_user = str(input("Enter your password: "))
    elif password != password_user:
        print("Password inccorect!")
        username_user = str(input("\nEnter your username: "))
        password_user = str(input("Enter your password: "))
    else:
        break

print("Welcome!")