#-------------------------------------------------------------------------
# Name:       Add the number
# Purpose:    Add the number from 5 to 20 
# Author:     Suen. J
# Created:    07/05/2024
#-------------------------------------------------------------------------

sum = 0

for i in range(4, 21):
    i += 1
    if i % 3 == 0:
        continue
    else: 
        sum += i

print (f"{sum}")