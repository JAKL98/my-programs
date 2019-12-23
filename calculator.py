# This program acts as a calculator when prompting a user to enter a calculation

import time
import math
import tkinter

# adding two numbers
def add(x,y):
    return x + y
# subtracting two numbers
def subtract(x,y):
   return x - y
# multiplying two numbers
def multiply(x,y):
    return x * y
# divide two numbers
def divide(x,y):
    return x / y

    
while True:
    Ask_User=input("Would you like to add (a), subtract (s), multiply (m), or divide (d)?  ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if Ask_User == "a":
        print(num1, "+", num2, "=", add(num1,num2))

    elif Ask_User == "s":
            print(num1, "-", num2, "=",subtract(num1,num2))

    elif Ask_User == "m":
        print(num1, "+", num2, "=", multiply(num1,num2))

    elif Ask_User =="d":
        print(num1, "+", num2, "=", divide(num1, num2))
    
    else:
        print("Invalid input")
        



    # main program
    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print ("Invalid input")
    if answer == 'y':
        continue
    else:
        print ("Goodbye")
        break



    
