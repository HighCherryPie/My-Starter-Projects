"""
Set a Number To be guessed

User Inputs a number   --- Validate If user entered a numeber  -- Done


It Shows Guess was correct If guess was correct   --- Checking if user won -- Done

If it was not correct tell how off the guess was    --- What to do if user didnt win -- Done

Limit The number of guesses  ---  A counter to count the attempts -- Done

"""
import os
import random

class validate():
    
    def NumInput():
        while True:
            try:
                a = int(input())
                return a
            except:
                print("Sorry that was a Invalid Input Please Enter Number \n>>>",end="")

class UserInputs():
    
    def first():
        print("A Number has been generated in between 0 and 100 \nTry Guessing>>>",end="")
        a = validate.NumInput()
        return a
    
    def afterFirst():
        print("Try Guessing Again >>>",end="")
        a = validate.NumInput()
        os.system("cls")
        return a


class Logic():

    def WinCondition(InputNumber):
        SetNum = NumberGuess.number
        GuessNum = InputNumber

        if SetNum == GuessNum:
            print("Congratulations You Guessed Sucessfully")
            print("The number was ",NumberGuess.number)
            input()
            exit()
        else:
            if GuessNum not in range(0,100):
                print("You missed by a Not reading Instructions,\nThe Number is Between 0 & 100")

            elif abs(SetNum - GuessNum) <= 1:
                print("You missed by a Needle")

            elif abs(SetNum - GuessNum) <= 5:
                print("You missed by Centimeters")

            elif abs(SetNum - GuessNum) <= 10:
                print("You missed by Inches")

            elif abs(SetNum - GuessNum) <= 25:
                print("You missed by a Metere")

            elif abs(SetNum - GuessNum) <= 50:
                print("You missed by a Kilometer")

            elif abs(SetNum - GuessNum) <= 100:
                print("You missed by a Mile")

            NumberGuess.GuessLeft()
        

class NumberGuess():

    @classmethod
    def Start(cls):
        cls.number = random.randint(0,100)
        cls.guessLeft = 10
        Logic.WinCondition(UserInputs.first())
        while cls.guessLeft != 0:
            cls.guessLeft -= 1
            Logic.WinCondition(UserInputs.afterFirst())
    
    @classmethod
    def GuessLeft(cls):
        print("You Have ",cls.guessLeft," Guess Left")

        if cls.guessLeft == 0:
            print("The number was ",cls.number)

NumberGuess.Start()