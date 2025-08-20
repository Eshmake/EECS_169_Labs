
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 11/28/2023
Lab: lab10
Last modified: 11/28/2023
Purpose: A program that defines a class representing a drivers license as a data type.
'''

#Drivers License Class

class DriversLicense:

    def __init__(self, firstName, lastName, age, voter, liceNum):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.voter = voter
        self.liceNum = liceNum

    def __lt__(self, other):
        return self.liceNum < other.liceNum

    def __gt__(self, other):
        return self.liceNum > other.liceNum

    def __le__(self, other):
        return self.liceNum <= other.liceNum

    def __ge__(self, other):
        return self.liceNum >= other.liceNum

    def __eq__(self, other):
        return self.liceNum == other.liceNum

    def __ne__(self, other):
        return self.liceNum != other.liceNum

    def __str__(self):
        
        if(self.voter == "Y"):
            votingStatus = "registered"
        else:
            votingStatus = "not registered"
            
        return f"{self.liceNum}: {self.lastName}, {self.firstName} ({self.age}) {votingStatus}"
    

    def __repr__(self):
        return f"DriversLicense({self.firstName}, {self.lastName}, {self.age}, {self.is_voter}, {self.licNum})"









    
