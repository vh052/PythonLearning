#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange
import sys

def ContinueGame(): # asks the user if they want to play again
    loop = True
    while loop:
        Continue = input("Would you like to play Again? (y/n): ")
        if len(Continue) != 0: # Checks if you inputted something
            Continue = Continue[0]
            Continue = Continue.lower()
            if Continue == "y": # continues if yes
                print("Continue...")
                return
            else:
                if Continue == "n": # Quits if no
                    print("Quiting...")
                    
                    print("-----Completed by Valiant-----")
                    
                    sys.exit() # Closes the program
                    return
                else:
                    print("Please enter a valid responce")
        else:
            print("Please enter a valid responce")
            
def GetUserWeapon(): # Gets the user weapon
    loop = True
    while loop:
        Weapon = input("Enter your weapon: ")
        if len(Weapon) != 0: # Makes sure you inputted something
            Weapon = Weapon[0]
            Weapon = Weapon.lower()
            if Weapon == "1" or Weapon == "r":
                return 1
            if Weapon == "2" or Weapon == "p":
                return 2
            if Weapon == "3" or Weapon == "s":
                return 3
            print("Please enter a valid responce")
        else:
            print("Enter a valid responce")

def GenerateOpResponce():
    return randrange(1,3) # a random range between 1-3

def GenWeapon(Num): # changes the number back to the weapon thing
    if Num == 1:
        return "Rock"
    if Num == 2:
        return "Paper"
    if Num == 3:
        return "Scissors"

def CalcWinner(You, Op): # Cals the winner
    
    OpWeapon = GenWeapon(Op)
    
    num = You - Op
    if num > 0:
        print("You beat", OpWeapon)
    if num == 0:
        print("You tied with", OpWeapon)
    if num < 0:
        print("You lost against", OpWeapon)
   
def WelcomeText():
    print("-------Rock, Paper, Scissors Game------")
    print("Choose Your Weapon!")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
   

def Main():
    WelcomeText() # Prints the welcome text
    while True:
        
        #print(Openent)
        
        UsrWeapon = GetUserWeapon()
        Oponent = GenerateOpResponce()
        CalcWinner(UsrWeapon, Oponent)
        
        ContinueGame()



if __name__ == "__main__": # Calls the Main function 
    Main()