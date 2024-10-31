#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def InputGrades():
    
    Grades = []
    InputGrades = True
    
    while InputGrades:
        
        Grade = int(input("Enter Grade (-1 to stop): "))
        
        if Grade == -1:
            print("Grades", Grades)
            return Grades
        else:
            Grades.append(Grade)
    

def RemoveGrade(Grades, Grade):
    Grades.remove(int(Grade))
    return Grades
    

def RemoveLowestGrade(Grades):
    
    print("Removing Lowest Grade From List")
    
    LowestGrade = Grades[0]
    
    AmountOfGrades = int(len(Grades))
    
    for i in range (0,AmountOfGrades):
        
        Grade = Grades[i]
        if Grade < LowestGrade:
            LowestGrade = Grade
    
    RemoveGrade(Grades, LowestGrade)
    print("Removed", LowestGrade)
    print("New Grade List", Grades)
    return Grades

def EditGradeList(Grades):
    print("-----Editing the Grade List----")
    
    AmountOfGrades = int(len(Grades))
    
    for i in range (0, AmountOfGrades):
        
        print("[" + str(i + 1) + "] =", Grades[i])
        
    while True:
        if AmountOfGrades > 0:
            Input = int(input("What grade do you want to change? : ")) - 1
            
            if Input > AmountOfGrades:
                print("You entered a number larger than the grade list.")
            else:
                #GradeValue = Grades[Input]
                Input2 = int(input("What is the new grade? : "))
                Grades[Input] = Input2
                print("Grades", Grades)
                return Grades
        else:
            print("There are not enough Grades remaining")
            break

def RemoveRandomGrade(Grades):
    
    print("Removing a Random Grade")
    
    RandomChoice = random.choice(Grades)
    
    print("Removed", RandomChoice)
    
    RemoveGrade(Grades, RandomChoice)
    print("Grades", Grades)
    return Grades

def SortNumericly(Grades):
    
    print("Sorting Grade List")
    
    GradesSorted = []
    
    while True:
        if Grades:
            AmountOfGrades = int(len(Grades))
            
            HighestGrade = Grades[0]    
            
            for i in range (0, AmountOfGrades):
                Grade = Grades[i]
                if Grade > HighestGrade:
                    HighestGrade = Grade
            
            GradesSorted.append(HighestGrade)
            Grade = RemoveGrade(Grades, HighestGrade)
        else:
            print("Grades", GradesSorted)
            return GradesSorted
         
def ReverseGradeOrder(Grades):
    
    print("Reversing Grade List")
    
    AmountOfGrades = int(len(Grades))
    
    GradesReversed = []
    
    for i in range(0, AmountOfGrades):
        index = (AmountOfGrades - (i + 1))
        
        if index <= AmountOfGrades and index >= 0:
            GradesReversed.append(Grades[index])
    
    print("Grades", GradesReversed)
    
    return GradesReversed

def GradeTotal(Grades):
    
    print("Getting Total of Grades")
    
    AmountOfGrades = int(len(Grades))
    Total = 0
    
    for i in range(0, AmountOfGrades):
        Total += Grades[i]
    
    print("Total:", Total)
    return Total

def GradeAverage(GradeTotal, Grades):
    
    AmountOfGrades = int(len(Grades))
    GradeAverage = GradeTotal / AmountOfGrades
    
    print("Grade Average:", GradeAverage)
    

def Main():
    
    Grades = InputGrades()
    Grades = RemoveLowestGrade(Grades)
    Grades = RemoveRandomGrade(Grades)
    Grades = EditGradeList(Grades)
    Grades = SortNumericly(Grades)
    Grades = ReverseGradeOrder(Grades)
    GradeTotalVar = GradeTotal(Grades)
    GradeAverage(GradeTotalVar, Grades)
    
    print("--------Completed by Valiant----------")
    
Main()