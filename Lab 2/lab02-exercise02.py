
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 13/09/2023
Lab: lab02
Last modified: 19/09/2023
Purpose: More practice with iteration and string methods.
User attempts to guess secret phrase of "bringcoffee" without case
sensitivity, and receives feedback on accuracy of each guess.

'''

#Secret Word Game

phrase = "bringcoffee"

guess = ""

while(guess.lower() != phrase):
    guess = input("Guess the secret phrase! ")
    guess = guess.lower()

    if(len(guess) == len(phrase)):
        numLetters = 0

        phraseList = []

        for c in phrase:
            phraseList.append(c)

        for n in guess:
            if(n in phraseList):
                numLetters += 1
                phraseList.remove(n)

        if(guess.lower() != phrase):
            print("Correct letters: " + str(numLetters))

    else:
        if(len(guess) > len(phrase)):
            print("Too many characters.")

        else:
            print("Too few characters.")

print("Correct!")
