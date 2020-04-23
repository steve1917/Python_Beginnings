#Create a triangle with this program

from graphics import *

def main():
    win = GraphWin("Draw a Triangle", width=400, height=400)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on Three Points")
    message.draw(win)

    #get and draw three verticles of a triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    #Use polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("blue")
    triangle.setOutline("cyan")
    triangle.draw(win)
    
    #wait for another click to exit
    message.setText("Click anywhere to quit.")
    message.setTextColor("red")
    win.getMouse()

main()
