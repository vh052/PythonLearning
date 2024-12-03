#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:52:49 2024

@author: valiant
"""

def ConvArrayToNum(Array):
    Num = ("".join(Array)) #Joins the array to one string variable
    if Num != "":
        Num = float(Num)
        return Num
    else:
        print("ERROR") # Errors if string is empty
        return 0

def GetUserInput(Text):
    while True:
        Error = False
        UsrInput = input(Text)
        UpdatedInput = []
        if UsrInput != "":
            for num in range(len(UsrInput)): # Runs through the length of UsrInput
                if not Error:
                    if UsrInput[num] == '$':
                        pass # Does nothing (allows functions to have nothing in them)
                    elif UsrInput[num] == '-':
                        print("Input Error: Enter a positive value!")
                        Error = True
                    elif UsrInput[num] == '.':
                        UpdatedInput.append(UsrInput[num]) # pushes the char to the array
                    elif UsrInput[num].isdigit(): # Checks if the char is a number
                        UpdatedInput.append(UsrInput[num])
                    else:
                        print("Input Error: Invalid input!")
                        Error = True
            if not Error:
                return(ConvArrayToNum(UpdatedInput)) # Returns the Converted array back 
        else:
            print("Input Error: Invalid input!")
  
def GetUsersExpenses():
    UsrExpanses = []
    while True:
        UsrInput = GetUserInput("Enter an expense amount (or 0 to exit): ")
        if UsrInput != 0: # Checks if the usr inputed something
            UsrExpanses.append(UsrInput) # pushes the value to the array
        else:
            return UsrExpanses

def AddUsrExpenses(Expenses):
    Total = 0
    for Expense in Expenses:
        Total += Expense # Adds and puts that new value back into Expense
    return Total
   
def PrintBudgetResults(MonthlyIncome, TotalExpenses):
    print("\nBudget Results")
    print("---------------------------------------")
    print(f"Total Income : ${MonthlyIncome:.2f}") # the :.2f Rounds the num to 2 dec points
    print(f"Total Expenses : ${TotalExpenses:.2f}")
    print(f"Budget Remaining : ${MonthlyIncome - TotalExpenses:.2f}")

def PrintExpenseList(Expenses):
    print("\nComplete Expense List")
    print("---------------------------------------")
    for Num in range(len(Expenses)):
        print(f"{Num+1}. ${Expenses[Num]:.2f}") # Prints the expenses out up to 2 dec points

def Main():
    print("Welcome to the Simple Budget Tracker")
    print("---------------------------------------")
    MonthlyIncome = GetUserInput("Enter your total Income: ")
    UsrExpenses = GetUsersExpenses()
    TotalExpenses = AddUsrExpenses(UsrExpenses) # Combines the usrs Expenses together
    PrintBudgetResults(MonthlyIncome, TotalExpenses) # prints them out
    PrintExpenseList(UsrExpenses) # prints the expenses in list form
    print("\n----- Completed By Valiant Hulsey -----")

Main()