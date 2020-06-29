        ## EXERCISE 3.8 SOLUTIONS

        #1
from random import randint
# for i in range(50):
#     random_number = randint(3,6)
#     print(random_number)

        #2
# x = randint(1,50)
# y = randint(2,5)
# print(x**y)

        #3
# number = randint(1,10)
# name = input(f"Enter your name: ")
# for i in range(number):
#     print(name)

        #4
# deci = randint(1.00,10.00)
# print(round(deci, 2))

        #5
# num = 0
# for num in range(50):
#     print(randint(num,(num+1)))

        #6
# x = int(input("Enter a number 'X': "))
# y = int(input("Enter a number 'Y': "))
# print((x-y)/(x+y))

        #7
# angle1 = int(input("Enter an Angle between -180 and 180: "))
# equivalent = (angle1%1)
# print(equivalent)

        #8
#60 seconds = 1 minute
# user = int(input("Enter a seconds: "))
# minute = user//60
# seconds = user%60
# print(f"We have {minute} minute, and {seconds} seconds. ")

        #9
# user = int(input("Enter hour: "))
# future = int(input("How many hours in future: "))
# future2 = (user + future) % 12
# print(f"New hour: {future2}.")

        #10
#         #a
# user = int(input("Enter a power: "))
# power = 10%(user**2)
# print(power)
#         #b
# user = int(input("Enter a power: "))
# power = 100%(user**2)
# print(power)
#         #c
# user = int(input("Enter a number: "))
# power = int(input("Enter the power: "))
# power2 = power%(user**2)
# print(power2)

        #11
# weight = float(input("Enter your weight in Kilogram: "))
# convert = weight*2.20
# print(round(convert,2))

        #12
from math import sin,cos,tan
# user = int(input("Enter the number you want the Factorial: "))
# facto = factorial(user)
# print(f"The Factorial of {user} is {facto}. ")

        #13
# user = int(input("Enter the number you want the sine, cosine and tangent: "))
# print(f"The sine is {sin(user)}, the cosine is {cos(user)} and the tangent is {tan(user)}.")

        #14
# user = int(input("Enter an Angle in degree: "))
# print(f"The sine of the Angle is {sin(user)}")

        #15
# for i in range(0,345,15):
#     number = (f"{i} --- {sin(i)}  {cos(i)}")
#     print(number)

        #16
        #TO BE ANSWERED LATER

        #17
        #TO BE ANSWERED LATER

        #18
# 1. A Nickel is worth 5 penny
# 2. A Dime is worth 10 penny
# 3. A Quarter is worth 25  penny
# 4. example: How many penny are there dime worth? 3*10=30
