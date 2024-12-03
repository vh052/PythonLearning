#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:37:25 2024

@author: valiant
"""

def IsInString(MainString, SubString):
    MainStringLower = MainString # I was going to lower the string but I changed my mind.
    SubStringLower = SubString
    StringIndex = MainStringLower.find(SubStringLower) # Finds the string in MainString
    print("\n")
    if StringIndex == -1: # -1 means there is no string found
        print(f"The String '{SubString}' was not found! (Case Sensitive)")
        return False
    else:
        print(f"The String '{SubString}' was located at the index of {StringIndex}!")
        return True
    
def GetYOrN(Prompt): # Asks the user a y or n question
    while True:
        UsrInput = input(Prompt)
        UsrInput = UsrInput.lower() # lowers the users input
        UsrInput = UsrInput[0] # Gets the first char from the users input string
        if UsrInput == 'y':
            return True
        elif UsrInput == 'n':
            return False
        else:
            print("Please Enter a Valid Input!")
    
def GetUsrInput():
    print("\n")
    MainString = input("Enter the string to seach through: ")
    SearchString = input("Enter the string to seach for: ")
    if IsInString(MainString, SearchString):
        if GetYOrN(f"Do you want to replace '{SearchString}' (y/n): "): # Asks the user a y or n question
            ReplacementString = input("Enter the replacement String: ") 
            MainString = MainString.replace(SearchString, ReplacementString) # It replaces the old string
            print(f"The New String '{MainString}'")
        else:
            print("Not replacing any String.")
                
def Main():
    print("Welcome to the String Replacement Tool!")
    print("---------------------------------------")
    GetUsrInput() # I was going to format it differently but I got lazy, thats why its called that.
    print("\n")
    print("Thank you for using my program")
    print("-------- Completed by Valiant --------")
    
Main()