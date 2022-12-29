from random import randint
from os import system

class game():
    
    options = ["rock","paper","siscors"]
    tries = 0
    score = 0

    def __init__():
        system("cls")

    @staticmethod
    def launch():
        while True:
            computer.result(computer.calculate(computer.UserInputValidated(),computer.think()))
    
class computer():

    # @staticmethod
    # def validate(UserInput):
    #         try:
    #             if UserInput == "quit":
    #                 system("cls")
    #                 print("Thank You For Playing")
    #                 print("You have {} Score in {} Tries".format(game.score,game.tries))
    #                 input()
    #                 return False
    #             elif UserInput not in game.options:
    #                 raise Exception
    #             else:
    #                 return True
    #         except:
    #             system("cls")
    #             print("The input was invalid Please try again")


    # @staticmethod
    # def UserInput():
    #     system("cls")
    #     UserInput = input("Enter \"rock\", \"paper\", \"siscors\" or \"quit\" to quit >>> ")
    #     if computer.validate(UserInput) == True:
    #         return UserInput
    #     else:
    #         exit()


    # _____________________________________________


    @staticmethod
    def UserInputValidated():
        while True:
            try:
                UserInput = input("Enter \"rock\", \"paper\", \"siscors\" or \"quit\" to quit >>> ")
                if UserInput == "quit":
                    system("cls")
                    print("Thank You For Playing")
                    print("You have {} Score in {} Tries".format(game.score,game.tries))
                    input()
                    break
                elif UserInput not in game.options:
                    raise Exception
                else:
                    return UserInput
            except:
                system("cls")
                print("The input was invalid Please try again")
        exit()

    @staticmethod
    def think():
       option = randint(0,2)
       print("Computer used",game.options[option])
       return game.options[option]

    @staticmethod
    def calculate(option1,option2):
        if option1 == option2:
            return 2        
        elif option1 == game.options[0] and option2 == game.options[2]:
            return 1
        elif option1 == game.options[1] and option2 == game.options[0]:
            return 1
        elif option1 == game.options[2] and option2 == game.options[1]:
            return 1
        else:
            return 0
    
    @staticmethod
    def result(code):

        if code == 0:
            print("You Lost")
        elif code == 2:
            print("Round Draw")
        elif code == 1:
            print("You Won")
            game.score += 1
        game.tries += 1
        input()
        system("cls")


game.launch()
