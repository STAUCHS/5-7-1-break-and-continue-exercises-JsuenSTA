#-------------------------------------------------------------------------
# Name:       Sum of the range of the number
# Purpose:    Calculate the sum of all the numeber picked whitin user range 
# Author:     Suen. J
# Created:    07/05/2024
#-------------------------------------------------------------------------

start = int(input("Enter the starting number: "))

end = int(input("Enter the ending number: "))

sum = 0

for i in range(start, end+1):
    i += 1
    if i == 13 or i == 31:
        continue
    else:
        sum += i

print (f"{sum}")