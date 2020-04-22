# convert.py
# 	A program to convert Celsius temps to Fahrenheit
#by: Steve B

def main():

	# print("Type in 5 temperatures seprerated by comas")
	# celsius1, celsius2, celsius3, celsius4, celsius5 = eval(input("What are the Celsius Temperatures? " ))

	celsius = 0

	for i in range(10):
		celsius += 10
		farenheit = 9/5 * celsius + 32

		print(celsius, "degrees celsius =", farenheit, "degrees farenheit")

main()

# print("The answer is", end=" ")
# print(3 + 4, end=" ")
# print("I love you")

# input celsius 5 times
# take each celsius temperature and calculate it to Farenheit
# display five converted temperatures