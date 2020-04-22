# get the farenheit
# calculate the celsius 
# output x amount of farenheit is = y amount of celcius

def main():
	
	print("This program will calculate the temperature from Farenheit to Celsius.")
	farenheit = eval(input("Enter the temperature in degrees Farenheit?: "))
	celsius = (farenheit - 32) * 5/9 
	print(farenheit, "degrees farenheit =", celsius, "degrees celsius")

main()