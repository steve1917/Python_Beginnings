#Create a Polygon with this program

from graphics import *

def main():
    win = GraphWin("Polygon Program | Create any Shape", width=400, height=400)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on Six Points")
    message.draw(win)

    #Intructions
    messageIntro = Text(Point(5, 9.5), "Create a 6 dimentional Object")
    messageIntro.draw(win)

    #get and draw three verticles of a triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)
    p5 = win.getMouse()
    p5.draw(win)
    p6 = win.getMouse()
    p6.draw(win)

    #Use polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3,p4,p5,p6)
    triangle.setFill("blue")
    triangle.setOutline("cyan")
    triangle.draw(win)
    
    #wait for another click to exit
    message.setText("Click anywhere to quit.")
    message.setTextColor("red")
    win.getMouse()

main()