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
