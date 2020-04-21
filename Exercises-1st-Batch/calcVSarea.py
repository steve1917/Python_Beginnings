# This program calculates the Volume and surface area of a sphere

# program
#   Get the radius of the circle from the user
#   calculate the volume and surface area 
#   Display the result to the user

import math

def main():
    print("This program calculates the Volume and surface area of a sphere.")
    r = eval(input("Input the radius of the circle: "))
    v = round(math.pi * (4/3 * r**3), 2)
    a = round(math.pi * r**2, 2)
    print("The radius of the circle is", r)
    print("The volume of the circle is", v)
    print("The area of the circle is", a)

main()