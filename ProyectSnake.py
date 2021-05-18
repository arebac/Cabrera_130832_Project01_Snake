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