# This program caluculates the cost per square inch of a circular pizza.

#program
#   get the cost of the pizza, and get the diameter of the pizza in inches
#   find the radius (r = D/2)
#   Now calulate the area of the pizza by using the equation (A = 4pi * (r)squared)
#   calculate the cost per square inch by using the equation (CostperInch = cost / Area)
#   Display the result to the User
#end

import math

def main():
    print("This program caluculates the cost per square inch of a circular pizza.")
    cost = eval(input("Enter the cost of the pizza($): "))
    D = eval(input("Enter the Size(diameter) of the pizza in inches: "))
    r = D/2
    A = (math.pi * r**2)
    print("Area =", A)
    costPI = cost/A
    print("The cost per square inch of this pizza is $", round(costPI, 2))

main()
    

