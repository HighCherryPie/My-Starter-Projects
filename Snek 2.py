"""

Creating Display -- Done

Creating Snake Body -- Done

Moving Snake --

Making Food -- 

Detecting Collisons --












"""

from os import system
from random import randint
from time import sleep
############################################################################3 The Display

class display:

    # The Initialisation
    pixels = []
    YRES = 8
    XRES = 10
    unit = "."


    #This Sets up the display and Draws object according to drawList
    
    @classmethod
    def update(cls):
        cls.pixels = []
        for i in range(cls.YRES):
            temp = []
            for x in range(cls.XRES):
                temp.append(cls.unit)
            cls.pixels.append(temp)
        cls.drawFromList()
        
    
    
    #This draws the display

    @classmethod
    def draw(cls):
        for i in cls.pixels:
            print(*i)
    
    #This Draws Components in display

    drawList = []

    @classmethod
    def drawFromList(cls):
        for i in cls.drawList:
            if i.__class__ == [].__class__:
                for j in i:
                    cls.pixels[j.ypos][j.xpos] = j.name
            elif i.__class__ == object.__class__:
                cls.pixels[i.ypos][i.xpos] = i.name
        display.drawList = []



################################################################### Snake


# The snake's Body

class snakeBody:
    xpos = 0
    ypos = 0
    name = "0"
    direction = 0


# The Snake Head

class snakeHead(snakeBody):
    name = "X"


# The entire Snake

class snake:

    #Initialise Body
        
    body = []

    # Adding Head and 2 Body Parts

    body.append(snakeHead())
    for i in range(2):
        body.append(snakeBody())

    #Randomising The start position


    body[0].ypos = randint(display.YRES//2-1,display.YRES//2+1)
    body[0].xpos = randint(display.XRES//2-1,display.XRES//2+1)

    #Deploying other body Parts

    for i in range(1,len(body)):
        body[i].ypos = body[0].ypos+i
        body[i].xpos = body[0].xpos

    #Adding Components to draw list
    
    @classmethod
    def addToDraw(cls):
        display.drawList.append(cls.body)
    
    #Changing The Direction of body parts (Recommended Tail First)

    @classmethod
    def updateDir(cls):
        for i in range(len(cls.body)-1,0,-1):
            cls.body[i].direction = cls.body[i-1].direction
    
    #The Movement of any part  ( Recommeneded Head First )

    @staticmethod
    def carryOut(object):

        # 0 - UP   ,  1 - Down
        # 2 - Left ,  3 - Right
        
        if object.direction == 0:
            object.ypos -= 1
        elif object.direction == 1:
            object.ypos += 1
        elif object.direction == 2:
            object.xpos -= 1
        elif object.direction == 3:
            object.xpos += 1
    
    # The Moving of Entire Snake

    @staticmethod
    def snakeMove():
        for i in snake.body:
            snake.carryOut(i)


######################################################## User Inputs


class userInput():

    @staticmethod
    def TakeValidInput():
        invalid = False
        while True:
            try:
                system("cls")
                
                snake.addToDraw()  # adds Snake body to Draw
                display.update()   # Draws canvas according to draw list and clears draw list
                display.draw()     # Outputs Draw
                

                if invalid == True:
                    print(">>> Sorry, The Previous input was invalid <<<")

                TheInput = input("""
Enter Order in format (Command <space> Repetition time)
0 - Up  1 - Down 2 - Left 3 - Right  , eg >>> 0 5 moves 5 steps in down direction
>>>""")         
                invalid = False
                SplitInput = TheInput.split()
                if len(SplitInput) < 1 or len(SplitInput) > 2:
                    raise ValueError

                

                if len(SplitInput) == 1:
                    SplitInput1 = int(SplitInput[0])
                    runtimev2.once(SplitInput1)
                    invalid = False
                elif len(SplitInput) == 2:
                    SplitInput1 = int(SplitInput[0])
                    SplitInput2 = int(SplitInput[1])
                    runtimev2.two(SplitInput1,SplitInput2)
                    invalid = False
                else:
                    raise ValueError
    
            except ValueError :
                invalid = True





class runtime():

    @staticmethod
    def mainloop():
        
        system("cls")   
        snake.snakeMove()
        snake.addToDraw()  # adds Snake body to Draw
        display.update()   # Draws canvas according to draw list and clears draw list
        display.draw()     # Outputs Draw
        snake.updateDir()
        sleep(0.25)




class runtimev2():
    
    @staticmethod
    def once(direction):
        snake.body[0].direction = direction
        runtime.mainloop()
    
    @staticmethod
    def two(directon,amount):
        for i in range(amount):
            runtimev2.once(directon)
 
################################################################# Deployment

userInput.TakeValidInput()