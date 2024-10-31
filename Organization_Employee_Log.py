#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:13:04 2024

@author: valiant
"""

Employees = {}

def CreateNewEmployee(Name, EmployeeID): # This Adds the new employee to Employees
    Employees.update({Name : {
        "ID" : EmployeeID
        }})

def DoesNameExist(Name): # returns true if Name already exists
    for EmployeeName in Employees:
        if EmployeeName == Name:
            return True
    return False

def GenID(): # Creates an ID a new ID that does not exist yet
    from random import randrange
    ID = None
    while True:
        ID = randrange(1,500)
        Exists = False
        for Employee in Employees:
            if Employees[Employee]["ID"] == ID:
                Exists = True
        if not Exists:
            break
    return ID

def AddNewEmployees(NumOfNewEmployees): # Creates all the new employees
    for i in range(NumOfNewEmployees):
        while True:
            EmployeeName = input(f"Employee #{i} Name: ")
            EmployeeName = EmployeeName.lower()
            if not DoesNameExist(EmployeeName):
                CreateNewEmployee(EmployeeName, GenID())
                break
            else:
                print(f"The name {EmployeeName} already exists!")
            
def PrintEployeeData(): # Prints out all the employee info
    print("\n")
    print("Employees")
    print("=========================")
    for Employee in Employees:
        print(f"Employee Name: \t \t {Employee}")
        print(f"Employee ID: \t \t {Employees[Employee]["ID"]}")
        print("=========================")
    

def Main(): # Calls all the script functions
    print("============ Organization Employee Log ============")
    NumOfNewEmployees = int(input("\nHow many new employees are being added? : "))
    print("\n======= Enter New Employee Info =============")
    AddNewEmployees(NumOfNewEmployees)
    PrintEployeeData()
    print("\n============= Completed By Valiant =============")
    
Main()