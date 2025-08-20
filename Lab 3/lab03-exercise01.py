
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 26/09/2023
Lab: lab03
Last modified: 26/09/2023
Purpose: Program that simulates a digital grocery list, allowing the user to
print and edit their personal list.
'''

#Going to Grocery Store

choice = 0
groceryList = []
groceryString = ""

while (choice != 4):
    print('''
        Welcome to your Shopping List!
        1) Add item
        2) Check off item
        3) Print list
        4) Exit
        ''')

    choice = int(input("Enter a choice: "))



    if(choice == 3):

        for n in range(len(groceryList)):
            groceryString += str(n+1) + ") " + groceryList[n] + "\n"
        
        print("Here is your list: ")
        print(groceryString)


    elif(choice == 2):
        itemToCross = int(input("Which item will you check off?: "))
        crossedItem = groceryList[itemToCross-1][0] + ((len(groceryList[itemToCross-1])-2) * "-") + groceryList[itemToCross-1][-1]
        groceryList[itemToCross-1] = crossedItem
    

    elif(choice == 1):
        itemToAdd = input("What will you add to the string?: ")
        groceryList.append(itemToAdd)


print("Goodbye!")

    






    
