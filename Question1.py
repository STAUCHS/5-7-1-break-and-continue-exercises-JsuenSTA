#-------------------------------------------------------------------------
# Name:       Skip 7
# Purpose:    Print 1 to 10 but skip 7
# Author:     Suen. J
# Created:    07/05/2024
#-------------------------------------------------------------------------

for i in range(1, 11):
    if i == 7:
        continue
    else:
        print (f"{i}")