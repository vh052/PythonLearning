#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randrange

IsGuessing = True
GuessedAttempts = 1
MaxGuessAttempts = 10

IsPlaying = True

print("Welcome to the number guessing game!")

while IsPlaying:
    
    RandomNumber = randrange(0,100)
    #print(RandomNumber)
    GuessedAttempts = 1
    
    print("Guess a random number between 0 - 100 within 10 attempts!")
    Guess = int(input("Enter your guess: "))
    
    while IsGuessing:
        if GuessedAttempts <+ MaxGuessAttempts:
            if RandomNumber != Guess:
                print("Sorry, that guess was incorrect, please try again. (" + str(MaxGuessAttempts - GuessedAttempts), "attempt(s) left)")
        
                
                if RandomNumber > Guess:
                    print("The number is higher than", str(Guess) + ".")
                else:
                    print("The number is lower than", str(Guess) + ".")
                
                Guess = int(input("Enter your guess: "))
                GuessedAttempts += 1
                
            else:
                IsGuessing = False
                print("You have guessed the number Correctly! ")
                print("It took you", GuessedAttempts, "attempt(s) to guess the number", str(RandomNumber) + ".")
                
                if GuessedAttempts == 1:
                    print("How did you do that, did you cheat?")
                    
                
        else:
            print("You had sadly ran out of attempts to guess the number.")
            IsGuessing = False
            
    PlayAgain = input("Would you like to play again? (y/n): ")
    PlayAgain = PlayAgain[0]
    PlayAgain = PlayAgain.lower()
    
    Asking = True
    while Asking:
        
        if PlayAgain == "n":
            IsPlaying = False
            Asking = False
            break
        if PlayAgain == "y":
            IsGuessing = True
            Asking = False
            break
        print("Please enter yes or no")
        PlayAgain = input("Would you like to play again? (y/n): ")
        
            
print("\n-----------Completed by Valiant Hulsey----------")
