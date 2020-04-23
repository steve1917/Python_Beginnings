# futval.py
# A program to compute the value of an investment
# carried 10 years into the future

def main():
	print("This program calculates the future value")
	print("of a 10-year investment.")
	

	principal = eval(input("Enter the initial principal: "))
	apr = eval(input("Enter the anual interest rate: "))
	money = principal

	for i in range(10):
		money += money * (apr/100)

	print("The Value in 10 years is: ", principal)

main()