
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 11/29/2023
Lab: lab10
Last modified: 11/29/2023
Purpose: A program that defines a main module in which the DMV and DriversLicense
can run.
'''

#main

from dmv import DMV
from driversLicense import DriversLicense


def main():

    fileName = input("Enter a fileName: ")

    myDMV = DMV(fileName)
    myDMV.run()


if __name__ == "__main__":
   main()
