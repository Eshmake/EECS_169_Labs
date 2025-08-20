
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 11/28/2023
Lab: lab10
Last modified: 11/28/2023
Purpose: A program that defines a class representing a DMV service as a data type,
which also provides the user with a menu.
'''

#DMV Class

from driversLicense import DriversLicense

class DMV:

    def __init__(self, fileName):
        self.driverList = []
        self.fileName = fileName

        file = open(self.fileName, "r")

        for line in file:
            contentsList = line.strip().split(",")
            self.driverList.append(DriversLicense(contentsList[0], contentsList[1], int(contentsList[2]), contentsList[3], int(contentsList[4])))

        file.close()        


    def allDrivers(self):
        sortDrivers = []
        copyDrivers = []

        for n in self.driverList:
            copyDrivers.append(n)

        while(len(sortDrivers) < len(self.driverList)):

            minVal = copyDrivers[0]

            for driver in copyDrivers:
                if(driver.age < minVal.age):
                    minVal = driver

            sortDrivers.append(minVal)
            copyDrivers.pop(copyDrivers.index(minVal))


        for driver in sortDrivers:
            print(driver)


    def youngDrivers(self):

        for driver in self.driverList:
            if(18 <= driver.age <=20 and driver.voter == "N"):
                print(driver)


    def initalsDrivers(self, firstInitial, lastInitial):
        count = 0
        
        for driver in self.driverList:
            if(driver.firstName[0].lower() == firstInitial.lower() and driver.lastName[0].lower() == lastInitial.lower()):
                print(driver)
                count += 1

        if(count == 0):
            print("No record found.")


    def agedDrivers(self, lowerAge, upperAge):

        count = 0
        
        for driver in self.driverList:
            if(lowerAge <= driver.age <= upperAge):
                print(driver)
                count += 1

        if(count == 0):
            print("No record found.")
        
    
        
    def voterRegis(self, driversLicense, fileName):
        check = False
        
        for driver in self.driverList:
            if(driver.liceNum == driversLicense):
                check = True
                if(driver.voter == "N"):
                    driver.voter = "Y"

                    file = open(self.fileName, "w")

                    for obj in self.driverList:
                        file.write(f"{obj.lastName},{obj.firstName},{obj.age},{obj.voter},{obj.liceNum}\n")

                    file.close()

                else:
                    print("Driver currently registered")

        if(check == False):
            print("No record found")


    def run(self):

        print("""
Select an option:
1) Print all Drivers Info, sorted by age
2) Print all 18-20 year old, unregistered voters
3) Print drivers by first and last initial
4) Print drivers of a specific age range
5) Quit
6) Register a driver to vote
""")
        choice = 0


        while(choice != 5):

            while(choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6):
                try:
                    choice = int(input("Enter your choice: "))
                    if(choice < 1 or choice > 6):
                        print("Invalid choice.")

                except ValueError:
                    print("Invalid choice.")

            if(choice == 1):
                self.allDrivers()
                choice = 0


            elif(choice == 2):
                self.youngDrivers()
                choice = 0


            elif(choice == 3):
                firstInitial = input("Enter a first initial: ")
                lastInitial = input("Enter a last initial: ")
                
                self.initalsDrivers(firstInitial, lastInitial)
                choice = 0


            elif(choice == 4):
                check = False


                while(check == False):
                    
                    try:
                        lowerAge = int(input("Enter a lower age bound: "))
                        upperAge = int(input("Enter an upper age bound: "))
                        check = True

                    except ValueError:
                        print("Invalid choice.")

                
                self.agedDrivers(lowerAge, upperAge)
                choice = 0


            elif(choice == 6):
                driversLicense = 0
                check = False

                while(check == False):
                    
                    try:
                        driversLicense = int(input("Enter a drivers license number: "))
                        check = True

                    except ValueError:
                        print("Invalid choice.")
                    
                self.voterRegis(driversLicense, self.fileName)
                choice = 0


            


        
        
