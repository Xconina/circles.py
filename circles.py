#circles.py
#This program draws a specified number of 2D circles in alternating fill
#colors to fit in the window.
#By Ashley Cook

import graphics
from graphics import*


def main():
    #set up window/coordinates
    win= graphics.GraphWin("Circles", 400, 400)
    win.setCoords(0,0,100,100)
    win.setBackground('gray')
    r = 50
    n= int(input("please enter a number:"))
    for i in range (n):
        
        circle= Circle(Point(50,50),r)
        
        if i % 2:
            circle.setFill('red')
        else:
            circle.setFill('black')
        circle.draw(win)
        r  = r - (r/n)
        n = n-1


main()


