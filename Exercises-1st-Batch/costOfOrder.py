# This Program calulates the cost of the order based on the cost of item and shipping 
# The User is buying pounds of coffee 
# 1 pound costs $10.50
# Shipping is $0.86 per pound + a flat fee of $1.50

#program
#   Diplay purpose of program
#   get the amount of pounds of coffee the user wants to buy
#   calxulate the cost of coffee
#   calculate the cost of shipping
#   calculate the total cost of order 
#   Display the total cost of order to buyer and break it up by cost of items and shipping Exspences
#end

def main():
    print("This program calculate the cost of Your order of coffee based on the ammount of pounds.")
    pounds = eval(input("Enter the amount of Pounds of Coffee you want to buy: "))
    coffee = pounds * 10.50
    shipping = (pounds * 0.86) + 1.50
    totalCost = coffee + shipping
    print("The total of cost of your order is $", round(totalCost, 2),) 
    print("The Coffee is $", round(coffee, 2), "and the Shipping is $", round(shipping, 2))

main()

