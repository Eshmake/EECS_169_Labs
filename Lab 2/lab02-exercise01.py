
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 13/09/2023
Lab: lab02
Last modified: 13/09/2023
Purpose: Introduction to iteration and string count method. User inputs a phrase
and a sequence to be searched within the phrase with option to toggle case
sensitivity, and receives the number of occurrences of the sequence within
the phrase as the output.
'''

#Sequence Search

phrase = input("Enter a string of characters: ")
phraseCopy = phrase

response = input("Would you like a case-sensitive search? ")

while(response != 'n' and response != 'N' and response != 'y' and response != 'Y'):
    response = input("Enter a valid response: ")

sequence = input("Enter a sequence to count: ")
sequenceCopy = sequence

numOfOccur = 0

if(response == 'n' or response == 'N'):
    phrase = phrase.lower()
    sequence = sequence.lower()
    numOfOccur = phrase.count(sequence)

elif(response == 'y' or response == 'Y'):
    numOfOccur = phrase.count(sequence)


print("In the string \'" + phraseCopy + ",\' the sequence \'" + sequenceCopy + "\' occurs " + str(numOfOccur) + " times.")



    





    
