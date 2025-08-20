'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 26/09/2023
Lab: lab03
Last modified: 26/09/2023
Purpose: Program that allows user to fill two integer lists with values, and then
mathematically compare their contents.
'''

#List Comparisons

valList1 = []

valList2 = []


response1 = ""
response2 = ""

while(response1 != "y" and response1 != "Y"):
    num1 = int(input("Enter a value for the first list: "))
    valList1.append(num1)

    response1 = input("Are you done? (y|Y): ")


while(response2 != "y" and response2 != "Y"):
    num2 = int(input("Enter a value for the second list: "))
    valList2.append(num2)

    response2 = input("Are you done? (y|Y): ")


print("List statistics: ")

if(sum(valList1) > sum(valList2)):
    print("The first list has the larger sum of " + str(sum(valList1)))
elif(sum(valList1) < sum(valList2)):
    print("The second list has the larger sum of " + str(sum(valList2)))
else:
    print("The two lists have the same sum of " + str(sum(valList1)))


avg1 = sum(valList1) / len(valList1)
avg2 = sum(valList2) / len(valList2)

if(avg1 > avg2):
    print("The first list has the larger average of " + str(avg1))
elif(avg1 < avg2):
    print("The second list has the larger average of " + str(avg2))
else:
    print("The two lists have the same average of " + str(avg1))


repeat = 0

repList = []

for i in range(len(valList1)):
    for j in range(len(valList2)):
        if((valList1[i] == valList2[j]) and (valList1[i] not in repList)):
            repeat += 1
            repList.append(valList1[i])

print("Count of values that appear in both lists: " + str(repeat))


if(valList1 == valList2[::-1]):
    print("The lists are mirrors of each other.")
else:
    print("The lists are not mirrors of each other.")


print("The values that appear in both lists are: " + str(repList))


valList1Copy = []

for n in valList1:
    if(n not in valList1Copy):   
        valList1Copy.append(n)



##for i in range(len(valList1)):
##    for j in range(len(dupList)):
##        if(valList1[i] == dupList[j]):
##            valList1.remove(valList1[i])
##            i -= 1
        
print("The unique values in the first list are: " + str(valList1Copy))


valList2Copy = []

for n in valList2:
    if(n not in valList2Copy):   
        valList2Copy.append(n)

##for i in range(len(valList2)):
##    for j in range(len(dupList)):
##        if(valList2[i] == dupList[j]):
##            valList2.remove(valList2[i])
##            i -= 1
        
print("The unique values in the second list are: " + str(valList2Copy))

   

    
