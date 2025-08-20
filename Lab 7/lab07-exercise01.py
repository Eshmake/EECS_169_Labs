
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 10/31/2023
Lab: lab07
Last modified: 10/31/2023
Purpose: A program that accepts a file from the user and produces 2 files,
with one containing the number of appearances of each word in the file,
and the other all uniquely appearing words in the file.
'''

#File Analyzer


def build_count(text):

    wordDict = {}
    
    for line in text:
        wordList = line.strip().split(" ")

        for word in wordList:
            newWord = clean_word(word)

            if(newWord != ""):
                if(newWord not in wordDict.keys()):
                    wordDict[newWord] = 1
                else:
                    wordDict[newWord] += 1

    return wordDict

def clean_word(word):
    
    word = word.lower()
    word = word.strip()

    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace(":", "")
    word = word.replace(";", "")
    word = word.replace(",", "")
    word = word.replace("|", "")
    word = word.replace(".", "")
    word = word.replace("[", "")
    word = word.replace("]", "")
    word = word.replace("(", "")
    word = word.replace(")", "")
    word = word.replace("--", "")


    if(word != "" and word[0] == "'" and word[-1] == "'"):
        word = word[1:-1]

    return word


def unique_words(word_counts):
    uniqueList = []

    for word in word_counts.keys():
        if(word_counts[word] == 1):
            uniqueList.append(word)

    return uniqueList


def main():
    welcome = "Welcome to the word counter!"
    welcomePrime = welcome.center(50, "=")
    print(welcomePrime)

    fileName = input("Enter a file name: ")

    print("The file", fileName, "has been processed.\nOutput stored in word_data.txt and unique_words.txt\nExiting...")

    fileInput = open(fileName, "r")


    fileDict = build_count(fileInput)
    fileInput.close()
    
    uniqueList = unique_words(fileDict)


    wordsOutput = open("word_count.txt", "w")
    uniqueOutput = open("unique_words.txt", "w")

    output = ""
    
    for word in fileDict.keys():
        output = word + " : " + str(fileDict[word]) + "\n"
        wordsOutput.write(output)


    uniqueOutput.write("Here is a list of words that appear exactly one time in the file: \n")

    for word in uniqueList:
       uniqueOutput.write(word + "\n") 
        

    wordsOutput.close()
    uniqueOutput.close()



main()
    
    
