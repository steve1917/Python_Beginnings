# Except input of kilometers
# convert kilometers to miles
# Output miles

def main():
	print("This program converts Kilometers to Miles.")

	kilometers = eval(input("Enter the amount of Kilometers to be converted? "))
	miles = kilometers * 0.621371192

	print(kilometers, "kilometers =", (round(miles, 2)), "miles")

main()