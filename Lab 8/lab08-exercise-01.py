
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 11/07/2023
Lab: lab08
Last modified: 11/08/2023
Purpose: A program that simulates a pokedex and pokemon battles.
'''

#Pokedex

import random as rand

outputFile = None

logToggle = False


def build_pokedex(filename):
    pokeFile = open(filename, "r")
    pokedex = {}

    for line in pokeFile:
        pokeList = line.strip().split("\t")
        pokedex[pokeList[0]] = pokeList[1]

    return pokedex

def build_team(pokedex, size=6, is_unique=False):
    pokeTeam = []

    if(is_unique == False):
        pokeTeam = rand.choices(list(pokedex.keys()), k=size)

    else:
        if(size <= len(pokedex)):
            pokeTeam = rand.sample(list(pokedex.keys()), k=size)

        else:
            print("invalid team size")
            return None

    return pokeTeam


def battle(team1, team2):

    battleLog = ""
    battleResult = ""
    count = 1

    global logToggle

    while(team1 != [] and team2 != []):
        matchList = [team1[0], team2[0]]
        
        winner = rand.choice(matchList)

        battleLog = "+++Round " + str(count) + "+++\n" + matchList[0] + " VS " + matchList[1] + "\n" + winner + " wins!\n"
        
        if(winner == matchList[0]):
            team2.pop(0)
        else:
            team1.pop(0)

        count += 1

        print(battleLog)

        if(logToggle == True):
            outputFile.write(battleLog + "\n")


    if(team1 == []):
        battleResult = "+++Team 2 Wins!+++\n"
        for n in team2:
            battleResult += n + "\n"

    else:
        battleResult = "+++Team 1 Wins!+++\n"
        for n in team1:
            battleResult += n + "\n"


    print(battleResult)
        
    if(logToggle == True):
        outputFile.write(battleResult + "\n")
        logToggle = False
        outputFile.close()



def main():

    choice = ""

    while(choice != 5):

        print("1) Print Pokedex\n2) Translate\n3) Build a team\n4) Pokemon battle\n5) Exit\n6) Fight log")

        choice = int(input("Choose an option: "))

        pokedex = build_pokedex("pokedex.txt")


        if(choice == 1):
            
            print("POKEDEX".center(27, "=") + "\n" + "-US-".center(13, " ") + "+" + "-JPN-".center(13, " ") + "\n")

            for pairs in pokedex.items():
                print(pairs[0].center(13, " ") + "|" + pairs[1].center(13, " "))
   
            print("\n")


        elif(choice == 2):

            pokemon = input("What pokemon's name would you like translated into the Japanese equivalent? ")

            if(pokemon in pokedex.keys()):
                print("Japanese name of " + pokemon + ": " + pokedex[pokemon])

            else:
                print("Given name not found in pokedex.")


        elif(choice == 3):

            pokeTeam = build_team(pokedex)

            if(pokeTeam != None):
                
                print("+++Pokemon Team+++")

                for pokemon in pokeTeam:
                    print(pokemon)

                print("\n")


        elif(choice == 4):
            
            pokeTeam1 = build_team(pokedex, is_unique = True)
            pokeTeam2 = build_team(pokedex, is_unique = True)

            battle(pokeTeam1, pokeTeam2)


        elif(choice == 6):

            global logToggle
            global outputFile

            outputFileName = input("Enter an output file name: ")

            outputFile = open(outputFileName, "w")
            
            logToggle = True


        elif(choice != 5):
            print("Invalid choice.")


main()







        
