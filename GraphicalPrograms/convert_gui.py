#This program converts the Temperature from Celsius to Farenheit

#Program
#   Create Graphics GUI for elements
#   calculate
#   Display the coverted back to the User
#End

from graphics import *

def main():
    #GUI
    win = GraphWin("Celsius to Farenheit Coverter", width=500, height=500)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    #Draw the interface
    Text(Point(1,3), "  Celsius Temperature: ").draw(win)
    Text(Point(1,1), "Farenheit Temperature: ").draw(win)
    input = Entry(Point(2,3), 5)
    input.draw(win)
    output = Text(Point(2,1), "")
    output.draw(win)
    button = Text(Point(1.5,2), "Convert It")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    #Wait for Mouse click
    win.getMouse()

    #Convert the Input
    celsius = eval(input.getText())
    farenheit = 9.0/5.0 * celsius + 32

    #Display output and Change button
    output.setText(farenheit)
    button.setText("Quit")

    #Wait for click then close
    win.getMouse()
    win.close()

main()
