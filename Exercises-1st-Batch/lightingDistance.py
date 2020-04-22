# This program determines the distance to a lightning strike based on the time
# elapse between the flash and the sound of thunder.

#program
#   Get the input time elapse from the user in seconds
#   calulate the distance from the lightning strike using the equations:
#   distance = 1100ft * seconds
#   miles = distance / 5280ft
#   Display the distance to the User
#end

def main():
    print("This program determines the distance from a lightning strike based on the")
    print("time elapse between the flash of lightning and the sound of the thunder.")
    seconds = eval(input("Enter the time elapse in seconds between lighting and thunder: "))
    distance = 1100 * seconds
    miles = distance / 5280
    print("You are", round(miles, 2), "miles away from the lightning strike!")
    if miles < 1:
        print("You were very close to the lighting strike. Beware!")

main()
