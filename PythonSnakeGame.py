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




def createsnake():
    snake = [0]*4
    size=4
    for i in range(size):
        snake[i] = Rectangle(Point(300-(i*15), 247),Point(300-(i*15)+14, 261))
        snake[i].setFill("black")
        snake[i].setOutline("red")
        snake[i].draw(snakegame)

    return snake


def move(snake, k, snakegame):
    max = size-1
    snake[max].undraw()
    
    while max > 0:
        snake[max] = snake[max-1]
        max = max -1
        
    snake[0] = snake[1].clone()
    if Direction == 1:
        snake[0].move(15,0)
    elif Direction == 2:
        snake[0].move(0,15)
    elif Direction == 3:
        snake[0].move(-15,0)
    elif Direction == 4:
        snake[0].move(0,-15)

    snake[0].draw(snakegame)


def checkBounds(snake):
    if (snake[0].getCenter().getX() > 540 or
        snake[0].getCenter().getX() < 53 or
        snake[0].getCenter().getY() < 59 or
        snake[0].getCenter().getY() > 546):
        return True

    elif (snake[0].getCenter().getX() == Apple.getCenter().getX() and
          snake[0].getCenter().getY() == Apple.getCenter().getY()):
        newApple()
        grow(snake)
        
        
    for j in range(3, size):
        if (snake[0].getCenter().getX() == snake[j].getCenter().getX() and
            snake[0].getCenter().getY() == snake[j].getCenter().getY()):
            return True


def grow(snake):

   snake.append(snake[size-3].clone())
   snake.append(snake[size-3].clone())
    
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

    asnake=createsnake()
    newApple()
    
  
    while(Lost!=True):
        k=snakegame.checkKey()
        time.sleep(0.10)
        if checkBounds(asnake) == True:
            Lost = True
        elif ((k == "d" or k == "Right") and Direction!=3):
            Direction = 1
            move(asnake, k, snakegame)
        elif ((k == "s" or k == "Down") and Direction!=4):
            Direction = 2
            move(asnake,k, snakegame)
        elif ((k == "a" or k == "Left") and Direction!=1):
            Direction  = 3
            move(asnake, k, snakegame)
        elif ((k == "w" or k == "Up") and Direction!=2):
            Direction  = 4
            move(asnake, k, snakegame)
        else:
            move(asnake, k, snakegame)
   


    input("press enter to quit: ")
main() 