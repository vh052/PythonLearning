#!/usr/bin/env python3
# -*- coding: utf-8 -*-

InvestmentIsValid = False
InterestRateIsValid = False
InvestmentDurationIsValid = False

# Gets the Investment Amount

Invenstment = int(input("Enter an investment amount between $0 - $50,000: "))

while InvestmentIsValid == False:
    if Invenstment < 0 or Invenstment > 50000:
        print("You entered an investment number below $0 or more than $50,000")
        Invenstment = int(input("Please enter a valid investment amount: "))
    else:
        InvestmentIsValid = True

# Gets the Investment Rate

InterestRate = int(input("Enter an interest rate between 0% - 15%: "))

while InterestRateIsValid == False:
    if InterestRate < 0 or InterestRate > 15:
        print("You entered an interest below 0% or higher than 15%")
        InterestRate = int(input("Please enter a valid interest rate: "))
    else:
        InterestRateIsValid = True

# Gets the Investment Duration in years

InvestmentDuration = int(input("Enter an Investment duration in years above 0: "))

while InvestmentDurationIsValid == False:
    if InvestmentDuration <= 0:
        print("You entered an investment duration in years below or 0")
        InvestmentDuration = int(input("Please enter a valid duration: "))
    else:
        InvestmentDurationIsValid = True

# Calc the interest Rate per month

InterestRateOrg = InterestRate

InterestRate = InterestRate / 12
InterestRate = InterestRate / 100

InvestmentAmount = Invenstment

for Years in range(1,InvestmentDuration +1):
    
    for Month in range(1, 12+1):
        
        InvestmentAmountAdd = InvestmentAmount * InterestRate
        InvestmentAmount = InvestmentAmount + InvestmentAmountAdd
        
    print("Year", Years, ": $" + str(round(InvestmentAmount, 2)))
    
print("Investment Duration: ", InvestmentDuration)   
print("Yearly Interest rate:", str(InterestRateOrg) + "%")
print("Investment amount: $" + str(Invenstment))
print("Total amount of Investment after compounding: $" + str(round(InvestmentAmount, 2)))

print("\nMade by Valiant")
