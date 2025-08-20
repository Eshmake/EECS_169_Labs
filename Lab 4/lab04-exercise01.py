
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 10/02/2023
Lab: lab04
Last modified: 10/02/2023
Purpose: A program that simulates a web browser history, allowing the
user to navigate to different sites, go backwards or forwards within
their web history, and print their history as output.
'''

#Web History Simulator

file_input = input("Enter a file name: ")

web_comms = open(file_input, 'r')

file_output = open("webhistory.txt", "w")

websites = []

webVal = -1

for line in web_comms:
        
        if(line[0:8] == "NAVIGATE"):
            if(line[9:17] == "https://"):
                currentWeb = (line.strip())[9:]
                if(currentWeb not in websites):
                    if(webVal != len(websites)-1):
                        websites = websites[0:webVal+1]
                        websites.append(currentWeb)
                    else:
                        websites.append(currentWeb)
                    webVal = websites.index(currentWeb)
                    
        elif(line[0:4] == "BACK"):
            if(webVal != 0):
                webVal -= 1

        elif(line[0:7] == "FORWARD"):
            if(webVal != len(websites)-1):
                webVal += 1


        elif(line[0:7] == "HISTORY"):
            
            
            file_output.write("Oldest\n===========\n")

            for site in websites:
                if(webVal == websites.index(site)):
                    file_output.write(site + " <==\n")
                else:
                    file_output.write(site + "\n")
            
            file_output.write("===========\nNewest\n\n")

           

        elif(line.strip() == "EXIT"):
            file_output.close()
            web_comms.close()
            break




                
    
