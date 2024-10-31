#!/usr/bin/env python3
# -*- coding: utf-8 -*-

StudentInfo = {}

def AddStudent(Name, ID, GPA, CreditsCompleted, Grades): # adds new students into StudentsInfo
    StudentInfo.update({Name : {
        "StudentID" : ID,
        "StudentGPA" : GPA,
        "CompletedCredits" : CreditsCompleted,
        "Grades" : Grades
        }})

def Main():
    
    AddStudent("Jim", 1, 3.1, 97.0, [80,50,100,98])# Adds Jim and his data to StudentInfo
    AddStudent("Sarah", 2, 3.6, 40.0, [80,98])# Adds Sarah and her data to  StudentInfo
    print("Student Info:", StudentInfo)

    print("----- Listing Student Names --------")
    for StudentName in StudentInfo:
        print(StudentName)
    
    print("------ Accessing Student Info -------")
    print("Student \t StudentID \t GPA \t Completed Credits \t Grades")
    for Student in StudentInfo:
        #print(Student)
        
        print(f"{Student} \t \t \t {StudentInfo[Student]["StudentID"]} \t \t {StudentInfo[Student]["StudentGPA"]} \t \t \t{StudentInfo[Student]["CompletedCredits"]} \t \t {StudentInfo[Student]["Grades"]} \n")
        
    
    print("Accessing student Information Using the Key in a loop")
    for StudentStuff in StudentInfo:
        print(f"{StudentStuff} {StudentInfo[StudentStuff]} \n")
        
    
    print("Sarah is dropping out, removing the student info")
    StudentInfo.pop("Sarah")
    print(f"{StudentInfo} \n")
    
    print("Getting Jims GPA")
    print(f"{StudentInfo["Jim"]["StudentGPA"]} \n")
    
    print("Clearing Student Registry")
    StudentInfo.clear()
    print(StudentInfo)
    
    print("------------- Completed By Valiant Hulsey ---------------")
    
Main()

