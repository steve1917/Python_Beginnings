# Input user expression
# calculate user expression
# Output user expression = answer
# loop program so user can keep on typing in Expressions and getting 
# 	results

def main():
	print("This program calculates your Equation. Ex.( 5 + 4/5 )")
	for i in range(100):
		calculate = (input("Input your Equation: "))
		calculated = eval(calculate)
		print(calculate, "=", calculated)

main()


