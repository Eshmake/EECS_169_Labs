
'''
Author: Sina Asheghalishahi
KUID: 3127403
Date: 10/17/2023
Lab: lab06
Last modified: 10/23/2023
Purpose: A program which contains multiple functions that modify a given
integer value.
'''

#Functions Lab:


def last_digit(num):
    return num % 10

def remove_last_digit(num):
    return num // 10

def add_digit(current_num, new_digit):
    return current_num*10 + new_digit

def reverse(num):
    numReverse = 0
    while(num != 0):
        numReverse = add_digit(numReverse, last_digit(num))
        num = remove_last_digit(num)
    return numReverse

def is_palindrome(num):
    if(num == reverse(num)):
       return True
    else:
        return False

def count_digits(num):
    count = 0

    while(num != 0):
       count += 1
       num = remove_last_digit(num)
    return count

def sum_digits(num):
    result = 0
    while(num != 0):
        result += last_digit(num)
        num = remove_last_digit(num)
    return result

def is_prime(num):
    output = True
    
    if(num == 1):
        return output
    else:
        for n in range(2, (num//2)+1):
            if(num % n == 0):
                output = False
    return output
    

def print_menu():
    print("1) Count digits\n2) Sum digits\n3) Is Palindrome\n4) Reverse\n5) Is Prime\n6) Exit\nChoice: ")


def main():

    choice = 0
    
    while(choice != 6):
        print_menu()
        choice = int(input())

        if(choice == 1):
            num = int(input("Enter a positive integer: "))
            print("There are", count_digits(num), "digits in the number")

        elif(choice == 2):
            num = int(input("Enter a positive integer: "))
            print("The sum of the digits of the number is", sum_digits(num))

        elif(choice == 3):
            num = int(input("Enter a positive integer: "))
            if(is_palindrome(num) == True):
                print("The number is a palindrome")
            else:
                print("The number is not a palindrome")

        elif(choice == 4):
            num = int(input("Enter a positive integer: "))
            print("The reverse of the number is", reverse(num))

        elif(choice == 5):
            num = int(input("Enter a positive integer: "))
            if(is_prime(num) == True):
                print("The number is prime")
            else:
                print("The number is not prime")
            

main()









    
