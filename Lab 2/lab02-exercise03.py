
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 19/09/2023
Lab: lab02
Last modified: 19/09/2023
Purpose: Simulates flu scenario based on fibonacci algorithm, where user
receives number of sick individuals for specified day.

'''

#Outbreak Game

dayVal = int(input("What day do you want a sick count for? "))


sickDay1 = 1
sickDay2 = 4
sickDay3 = 64

if(dayVal <= 0):
    print("Invalid day.")

else:
    if(dayVal == 1):
        print("Total people with flu:", sickDay1)
    elif(dayVal == 2):
        print("Total people with flu:", sickDay2)
    elif(dayVal == 3):
        print("Total people with flu:", sickDay3)
    elif(dayVal > 3):

        sickVal = 0
        
        for _ in range(4, dayVal+1):
            sickVal  = (sickDay1 + sickDay2 + sickDay3)
            sickDay1 = sickDay2
            sickDay2 = sickDay3
            sickDay3 = sickVal

        print("Total people with flu:", sickVal)





