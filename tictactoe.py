from os import system

class Board():


    board = []
    for i in range(1,10):
        board.append(i)

    @classmethod
    def draw(cls):
        print("     |     |    ")
        print(" ",cls.board[0]," | ",cls.board[1]," | ",cls.board[2]," ")
        print("_____|_____|____")
        print("     |     |    ")
        print(" ",cls.board[3]," | ",cls.board[4]," | ",cls.board[5]," ")
        print("_____|_____|____")
        print("     |     |    ")
        print(" ",cls.board[6]," | ",cls.board[7]," | ",cls.board[8]," ")
        print("     |     |    ")

    @classmethod
    def mark(cls,num,mark):
        cls.board[num] = mark
    


class Game(Board):

    mark1 = "X"
    mark2 = "o"
    
    turn = mark1
    marksleft = 9

    @classmethod
    def EndTurn(cls):
        if cls.turn == cls.mark1:
            cls.turn = cls.mark2
        else:
            cls.turn = cls.mark1
    
    @classmethod
    def mark(cls):
        Marked = False
        error = False
        while not(Marked):
            try :
                if error == True:
                    system("cls")
                    print("Sorry The said square is Invalid")
                else:
                    system("cls")

                Game.draw()
                num = int(input("Enter a grid square no to mark >> "))-1
                if cls.validate(num) == True:
                    Game.board[num] = cls.turn
                    cls.marksleft -= 1
                    Marked = True
                else:
                    raise InvalidInput
                
            except:
                error = True
            else:
                cls.win()
                cls.EndTurn()
    
    @classmethod
    def validate(cls,num):
        if num < 0 or num > 8:
            return False
        elif Game.board[num] == cls.mark1 or Game.board[num] == cls.mark2:
            return False
        else:
            return True

   

    @classmethod
    def win(cls):
        if (cls.board[0] == cls.board[1] and cls.board[1] == cls.board[2]) or (
            cls.board[3] == cls.board[4] and cls.board[4] == cls.board[5]) or (
            cls.board[6] == cls.board[7] and cls.board[7] == cls.board[8]) or (
            cls.board[0] == cls.board[3] and cls.board[3] == cls.board[6]) or (
            cls.board[1] == cls.board[4] and cls.board[4] == cls.board[7]) or (
            cls.board[2] == cls.board[5] and cls.board[5] == cls.board[8]) or (
            cls.board[0] == cls.board[4] and cls.board[4] == cls.board[8]) or (
            cls.board[2] == cls.board[4] and cls.board[4] == cls.board[6]):
                system("cls")
                Game.draw()
                print(cls.turn , " has won")
                input()
                exit()
        else:
            cls.CheckDraw()
        
    @classmethod
    def CheckDraw(cls):
        if cls.marksleft == 0:
            system("cls")
            Game.draw()
            print("Game is Draw")
            input()
            exit()

    
            
        
class InvalidInput(Exception):
    pass


while True:
    Game.mark()
