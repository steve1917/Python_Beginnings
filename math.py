# This is a Math file for Practicing Math Code

# print(list(range(10)))
# print(list(range(5,10)))
# print(list(range(5,10,2)))
# n = 2
# print(list(range(2 ,n+1)))

# math.py
#   Program to compute the factorial of a number !!!
#   Illustrates for loop with an accumulator
# def main():
#     print("This Program computes the factorial of a number")
#     n = eval(input("Please enter a whole number: "))
#     fact = 1
#     for factor in range(n,1,-1):
#         fact = fact * factor
#     print("The factorial of", n, "is", fact)

# main()

# Inport Math !!!
import math

# Pi
print(math.pi)

# 4.0 / 10.0 + 3.5 * 2
print((int(4.0)) / (int(10.0)) + 3.5 * 2)

# 10%4 + 6/2
print(10%4 + int(6/2))

# abs(4 - 20 // 3) ** 3
print(abs(4 - 20 // 3) ** 3)

# sqrt(4.5 - 5.0) + 7 * 3
# print(sqrt(4.5 - 5.0) + 7 * 3) # Not Possible because you cannot square root a negative number

# 3 * 10 // 3 + 10 % 3
print(3 * 10 // 3 + 10 % 3)

# 3 ** 3
print(3 ** 3)

# (3 + 4)(5)
print((3 + 4) *(5))

# n(n-1) / 2
n = 2
print((n * (n - 1))  / 2)

# 4 * pi * r**2
r = 2
print(4 * math.pi * r**2)

# sqrt(r(cos a)**2 + r(sin a)**2)
r = 5
a = 5
print(math.sqrt((r * (math.cos(a)))**2 + (r * (math.sin(a))**2)))

# y2(final) - y1(init) / x2(final) - x1(init)
# y1 = eval(input("Enter your Initail y value: "))
# y2 = eval(input("Enter your final y value: "))
# x1 = eval(input("Enter your Initail x value: "))
# x2 = eval(input("Enter your final x value: "))
# print("The difference between", "(", y2,"-", y1, ")", "/", "(",x2, "-", x1, ")")
# print("is equal to", (y2 - y1) / (x2 - x1))

# Range
# for i in range(15, 5, -2):
#     print(i)

# Range For
for i in range(1, 11):
    print(i*i)

for i in (1,3,5,7,9):
    print(i, ":", i**3)
print(i)

x = 2
y = 10
for j in range(0, y, x):
    print(j, end="")
    print(x + y)
print("Done")

ans = 0
for i in range(1, 11):
    ans = ans + i * i
    print(i)
print(ans)

print(round(314.159265, -2))


