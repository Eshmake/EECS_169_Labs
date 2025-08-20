'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 19/09/2023
Lab: lab02
Last modified: 19/09/2023
Purpose: Secret Word Game with an addition that requests a count of guesses
from the user, and then limits them to the specified number of guesses.

'''

#Secret Word Game (Advanced)

phrase = "bringcoffee"

guess = ""

guessLimit = int(input("How many guesses do you predict you will need? "))

count = 0
while(guess.lower() != phrase and count < guessLimit):
    guess = input("Guess the secret phrase! ")
    guess = guess.lower()

    if(len(guess) == len(phrase)):
        numLetters = 0

        phraseList = []
        phraseList2 = []

        for c in phrase:
            phraseList.append(c)
            phraseList2.append(c)

        rightPlace = 0

        for n in guess:
            if(n in phraseList):
                numLetters += 1
                if(guess.find(n) == phraseList2.index(n)):
                    rightPlace += 1
                phraseList.remove(n)

        if(guess.lower() != phrase):
            print("Correct letters: " + str(numLetters))
            print("Letters in right places: " + str(rightPlace))
        else:
            print("Correct!")

    else:
        if(len(guess) > len(phrase)):
            print("Too many characters.")

        else:
            print("Too few characters.")
    count += 1


