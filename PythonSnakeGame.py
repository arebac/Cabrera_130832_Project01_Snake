
from graphics import *
from random import *


def createhabitat(snakegame):
    square=Rectangle(Point(0,0),Point(600,600))
    square.setOutline("black")
    square.setWidth(85)
    square.setFill('green')
    square.draw(snakegame)
    
def instructions(snakegame):
    wel_msg=Text(Point(300,10), "Welcome to the snake game!")
    wel_msg.setTextColor('white')
    wel_msg.setStyle("bold")
    wel_msg.draw(snakegame)
    click_msg=Text(Point(300,50), "Press space bar to begin: ")
    click_msg.setStyle("bold")
    click_msg.setTextColor("white")
    click_msg.draw(snakegame)
    Arrowkeys=Text(Point(300, 30), "Use arrow keys to move in the desired direction: ")
    Arrowkeys.setTextColor("white")
    Arrowkeys.setStyle("bold")
    Arrowkeys.draw(snakegame)
    snakegame.getKey()
    Arrowkeys.undraw()
    click_msg.undraw()
    wel_msg.undraw()

size=4
snake=[0]*4
snakegame=GraphWin('Snake Game', 600,600)
createhabitat(snakegame)
instructions(snakegame)




class Snake():
    def __init__(tempsnake):
        tempsnake.size = 4
        tempsnake.snake = [0]*4
    

    def createsnake(tempsnake):
        tempsnake.snake = [0]*4
        tempsnake.size = 4
        for i in range(tempsnake.size):
            tempsnake.snake[i] = Rectangle(Point(300-(i*15), 247),Point(300-(i*15)+14, 261))
            tempsnake.snake[i].setFill("red")
            tempsnake.snake[i].draw(snakegame)


    def grow(tempsnake):
        tempsnake.size = tempsnake.size +2
        tempsnake.snake.append(tempsnake.snake[tempsnake.size-3].clone())
        tempsnake.snake.append(tempsnake.snake[tempsnake.size-3].clone())

    def move(tempsnake, k, win):
        max = tempsnake.size-1
        tempsnake.snake[max].undraw()
        
        while max > 0:
            tempsnake.snake[max] = tempsnake.snake[max-1]
            max = max -1
            
        tempsnake.snake[0] = tempsnake.snake[1].clone()
        if Direction == 1:
            tempsnake.snake[0].move(15,0)
        elif tempsnake == 2:
            tempsnake.snake[0].move(0,15)
        elif Direction == 3:
            tempsnake.snake[0].move(-15,0)
        elif Direction == 4:
            tempsnake.snake[0].move(0,-15)

        tempsnake.snake[0].draw(win)

    def checkBounds(tempsnake):
        if (tempsnake.snake[0].getCenter().getX() > 545 or
            tempsnake.snake[0].getCenter().getX() < 60 or
            tempsnake.snake[0].getCenter().getY() < 175 or
            tempsnake.snake[0].getCenter().getY() > 545):
            return True

        elif (tempsnake.snake[0].getCenter().getX() == Apple.getCenter().getX() and
              tempsnake.snake[0].getCenter().getY() == Apple.getCenter().getY()):
            newApple()
            tempsnake.grow()
    
            
        for j in range(3, tempsnake.size):
            if (tempsnake.snake[0].getCenter().getX() == tempsnake.snake[j].getCenter().getX() and
                tempsnake.snake[0].getCenter().getY() == tempsnake.snake[j].getCenter().getY()):
                return True



def newApple():
    
    dx = (randint(0, 31))*15
    dy = (randint(0, 24))*15
    valid = True
    
    global Apple
    try :
        Apple.undraw()  
    except :
        pass
    Apple = Rectangle(Point(60+dx, 172+dy),Point(74+dx, 186+dy))
    Apple.setFill("blue")
    Apple.setOutline("darkblue")
    Apple.draw(snakegame)

def main():

    global Lost
    Lost=False
    global Direction
    Direction=1

    razer=Snake()
    razer.createsnake()
    newApple()
    
  
    while(Lost!=True):
        k=snakegame.checkKey()
        time.sleep(0.10)
        if razer.checkBounds() == True:
            Lost = True
        elif ((k == "d" or k == "Right") and Direction!=3):
            Direction = 1
            razer.move( k, snakegame)
        elif ((k == "s" or k == "Down") and Direction!=4):
            Direction = 2
            razer.move(k, snakegame)
        elif ((k == "a" or k == "Left") and Direction!=1):
            Direction  = 3
            razer.move(k, snakegame)
        elif ((k == "w" or k == "Up") and Direction!=2):
            Direction  = 4
            razer.move(k, snakegame)
        else:
            razer.move(k, snakegame)
   


    input("press enter to quit: ")
main() 
