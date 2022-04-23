circlesanalysis.txt

Analysis
    I need to make a program that will draw a specified number of 2D circles in alternating fill colors to fit the window.

Specs
    n- number of circles, given through int(input)
    r- radius to be calculated through each loop

Psuedocode
    create graphwin 400x400
    setCoords(0,0,100,100) 
    #center is (50,50)
    
    intial radius of circle is 50
   
    #For loop
    for i range of (n)
        circle (50,50, r)
        if i % 2:
            setfill black
        else:
            setfill red
        draw circle

        #Change r and n for next loop
        r = r - (r/n)
        n= n -1

Code

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


Debugging
