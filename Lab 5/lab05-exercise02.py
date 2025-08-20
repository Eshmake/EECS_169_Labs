'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 10/10/2023
Lab: lab05
Last modified: 10/10/2023
Purpose: A program in which the user attempts to guess a three-word phrase
in two guesses, one with five letters and the second with the entire phrase.
'''

#Wheel of Python:

phrase = "Java is better"
phraseList = []

for i in range(len(phrase)):
    if(phrase[i] == " "):
        phraseList.append(" ")
    else:
        phraseList.append("?")

guess1 = ""

while(len(guess1) != 5):
    guess1 = input("Choose 5 letters to help: ")

    if(len(guess1) != 5):
        print("Invalid length.")

for n in guess1:
    if(phrase.lower().find(n.lower()) != -1):
        phraseList[phrase.lower().find(n.lower())] = n


print("Here is your phrase: ")

newPhrase = ""

for n in phraseList:
    newPhrase += n

print(newPhrase)


guess2 = input("Enter your guess: ")

if(guess2.lower() == phrase.lower()):
    print("You win!")

else:
    print("You lose!")





    
        
        
