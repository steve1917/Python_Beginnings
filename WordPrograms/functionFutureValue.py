#This Program Visualizes the Future Value of your money by using a Graph

#Program
#   Print Introduction
#   Get the apr and principal from the User
#   Create a GraphicsWin
#   Draw Scale labels on the side
#   Draw the bar at position 0 with height corresponding to principal
#   Calculate the Future Value of Money
#   Wait for the User to press enter
#End

from graphics import *

def drawBar(window, year, height):
    #draw a bar in window starting at year with given height
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():

    #Print intro
    print("This program calculates the future value of a 10-year investment.")

    #Get principal and apr
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the anual interest rate: "))
    money = principal

    #Create graphics window
    win = GraphWin("Investment Growth Chart", width=500, height=500)
    win.setBackground("White")
    win.setCoords(0,0,120,100)
    Text(Point(10, 10), "0.0k").draw(win)
    Text(Point(10, 30), "2.5k").draw(win)
    Text(Point(10, 50), "5.0k").draw(win)
    Text(Point(10, 70), "7.5k").draw(win)
    Text(Point(10, 90), "10.0k").draw(win)

    #Text on top
    message = Text(Point(60, 95), "The Future Value of your Money")
    message.draw(win)
    messageExit = Text(Point(60, 4), "Exit Text")
    messageExit.setTextColor("red")
    messageExit.draw(win)

    #Draw bar for the initial principal
    height = money * 0.008
    drawBar(win, 0, height)

    #Draw bars for succesive years
    for year in range(1,11):
        #calculate value for the next year
        money += money * (apr/100)
        #draw bar for this value
        x11 = year * 10 + 10
        height = money * 0.008 + 10
        bar = Rectangle(Point(x11, 10), Point(x11+10, 10+height)) 
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    #wait for another click to exit
    messageExit.setText("Click anywhere to quit.")
    messageExit.setTextColor("red")
    win.getMouse()

main()
