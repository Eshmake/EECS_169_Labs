
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 10/10/2023
Lab: lab05
Last modified: 10/11/2023
Purpose: A program which receives a matrix of integers from the user, and returns
specific statistics and modifications of it.
'''

#Matrix Simulator:

fileInputName = input("Enter a file name: ")

file_input = open(fileInputName, "r")


firstLine = file_input.readline()

rows = ""
cols = ""

space = False
for n in firstLine.strip():
    if(n == " "):
        space = True
    elif(space == False):
        rows += n
    else:
        cols += n
   
rows = int(rows)
cols = int(cols)
numElements = rows*cols

matrixList = []

for n in file_input:
    matrixList.append(n.strip().split(" "))

for i in range(rows):
    for j in range(cols):
        matrixList[i][j] = float(matrixList[i][j])


file_input.close()


#average file
average_file = open("averages.txt", "w")


result = 0

for n in matrixList:
    result += sum(n)

average_file.write("Total average: " + str(result/numElements) + "\n")

for i in range(rows):
    average_file.write("Row " + str(i+1) + " average: " + str((sum(matrixList[i])/cols)) + "\n")


average_file.close()


#reverse file
reverse_file = open("reverse.txt", "w")

reverseMatrixList = []
reverseMatrix = ""

for i in range(rows):
    reverseMatrixList.append(matrixList[i][::-1])

for i in range(rows):
    for j in range(cols):
        reverseMatrix += str(reverseMatrixList[i][j]) + " "
    reverseMatrix += "\n"
    
reverse_file.write(reverseMatrix)

reverse_file.close()


#flipped file

flipped_file = open("flipped.txt", "w")

flippedMatrixList = []
flippedMatrix = ""


for i in range(rows):
    matrixRow = []
    for j in range(cols):
        matrixRow.append(matrixList[i][j])
        
    flippedMatrixList.append(matrixRow)

for i in range(rows):
    for j in range(cols):
        flippedMatrixList[i][j] = matrixList[(rows-1)-i][j]

for i in range(rows):
    for j in range(cols):
        flippedMatrix += str(flippedMatrixList[i][j]) + " "
    flippedMatrix += "\n"

flipped_file.write(flippedMatrix)

flipped_file.close()


#diagonal file

mirroredMatrixList = []
mirroredMatrix = ""

if(rows == cols):


    for i in range(rows):
        matrixRow = []
        for j in range(cols):
            matrixRow.append(matrixList[i][j])
        
        mirroredMatrixList.append(matrixRow)

    
    for i in range(rows):
        for j in range(cols):
            mirroredMatrixList[i][j] = matrixList[j][i]

    for i in range(rows):
        for j in range(cols):
            mirroredMatrix += str(mirroredMatrixList[i][j]) + " "
        mirroredMatrix += "\n"

    
    diagonal_file = open("diagonal.txt", "w")

    diagonal_file.write(mirroredMatrix)
    
    diagonal_file.close()


#transpose file

transpose_file = open("transpose.txt", "w")

transMatrixList = []
transMatrix = ""



for j in range(cols):
    transRow = []
    for i in range(rows):
        transRow.append(matrixList[i][j])
    transMatrixList.append(transRow)
    

for i in range(rows):
    for j in range(cols):
        transMatrix += str(transMatrixList[i][j]) + " "
    transMatrix += "\n"

transpose_file.write(transMatrix)
    
transpose_file.close()
        


