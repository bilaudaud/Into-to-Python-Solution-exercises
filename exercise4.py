        ## EXERCISE 4.5 SOLUTIONS
        #1
# length = eval(input("Enter a length: "))
# if length < 0:
#     print(f"{length } is an Invalid number,pls enter a positive number ")
# else:
#     print(f"The result of { length } lenght is {length * 2.54 } in inch")

        #2
# temperature = eval(input("Pls, enter a temperature: "))
# unit = input("pls,enter either Celsious or Fahrenheit: ")
# if unit == "Celsious":
#     print(f"The convertion of temperature to celsious is {(9/5)*temperature + 32}")
# elif unit == "Fahrenheit":
#     print(f"The convertion of temperature to fahrenheit is {(5/9)*(temperature - 32)}")
# else:
#     print("Invalid syntax...")

        #  QUESTION 3
# 3. Ask the user to enter a temperature in Celsius. The program should print a daudssage based
# on the temperature:
# • If the temperature is less than -273.15, print that the temperature is invalid because it is
# below absolute zero.
# • If it is exactly -273.15, print that the temperature is absolute 0.
# • If the temperature is between -273.15 and 0, print that the temperature is below freezing.
# • If it is 0, print that the temperature is at the freezing point.
# • If it is between 0 and 100, print that the temperature is in the normal range.
# • If it is 100, print that the temperature is at the boiling point.
# • If it is above 100, print that the temperature is above the boiling point.

# temperature = eval(input("Pls, enter a temperature: "))
# if temperature < -273.5:
#     print("temperature is invalid because its below zero. ")
# elif temperature == -273.15:
#     print("temperature is absolute zero(0)")
# elif temperature > -273.15 and temperature <= 0:
#     print("temperature is below Freezing.")
# elif temperature == 0:
#     print("temperature is freezing point.")
# elif temperature > 0 and temperature < 100:
#     print("temperature is in normal range.")
# elif temperature == 100:
#     print("temperature is at the boiling point.")
# elif temperature > 100:
#     print("temperature above the boiling point.")

        # QUESTION 4
# 4. Write a program that asks the user how many credits they have taken. If they have taken 23
# or less, print that the student is a freshman. If they have taken between 24 and 53, print that
# they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over

# credit = eval(input("How many credits have you taken: "))
# if credit < 23:
#     print("You are a freshman. ")
# elif credit >=24 and credit <=53:
#     print("You are a sophomore.")
# else:
#     print("Welcodaud...")

        #  QUESTION 5
# 5. Generate a random number between 1 and 10. Ask the user to guess the number and print a
# daudssage based on whether they get it right or not.

# from random import randint
# rand_number = randint(1,10)
# user = eval(input("I am thinking of a number, Guess the number. "))
# if user == rand_number:
#     print("You are absolute correct! ")
# else:
#     print("You are wrong, the number is", rand_number)

         #  QUESTION 6
# 6. A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
# items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
# program that asks the user how many items they are buying and prints the total cost.

# buy = eval(input("How many items did you buy: "))
# if buy < 10:
#     print(f"The price for your items is ${buy*12}")
# elif buy >= 10 and buy <= 99:
#     print(f"The price for your items is ${buy*10}")
# elif buy > 100:
#     print(f"The price for your items is ${buy*7}")

        #  QUESTION 7
# 7. Write a program that asks the user for two numbers and prints Close if the numbers are
# within .001 of each other and Not close otherwise.

# user1 = eval(input("Enter the first Number: "))
# user2 = eval(input("Enter the second Number: "))
# if user1 + user2 < 0.001:
#     print("Closed")
# else:
#     print("OPEN")

        #  QUESTION 8
# 8. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Write a program that asks the user for a year and prints
# out whether it is a leap year or not

# year = eval(input("Please, enter a year. "))
# if (year%4)== 0:
#     print("You just entered a leap year. ")
# elif (year % 400 or year % 100)== 0:
#     print("you just entered a year that doesnt have a leap year. ")

        #  QUESTION 9
# Write a program that asks the user to enter a number and prints out all the divisors of that
# number. [Hint: the % operator is used to tell if a number is divisible by sodaudthing.

# year = eval(input("Please, enter a year. "))
# num = (year%2)
# if num == 0:
#     print(num)
    
        #  QUESTION 10
# 10. Write a multiplication gadaud program for kids. The program should give the player ten randomly generated multiplication questions to do. After each, the program should tell them
# whether they got it right or wrong and what the correct answer is.
# Question 1: 3 x 4 = 12
# Right!
# Question 2: 8 x 6 = 44
# Wrong. The answer is 48.
# ...
# ...
# Question 10: 7 x 7 = 49
# Right.

# from random import randint
# for i in range(10):
#     x = randint(0,20)
#     y = randint(0,20)
#     z = (x * y)
#     user = eval(input(f"Question {i+1}: {x} X {y} = "))
#     if user == z:
#         print("Right! ")
#     else:
#         print("Wrong. The answer is", z)

        #  QUESTION 11
# 11. Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
# and asks them how many hours into the future they want to go. Print out what the hour will
# be that many hours into the future, printing am or pm as appropriate. An example is shown
# below
# Enter hour: 8
# am (1) or pm (2)? 1
# How many hours ahead? 5
# New hour: 1 pm

# user = eval(input("Enter hour: "))
# am = "1"
# pm = "2"
# unit_tidaud = input("am (1) or pm (2)? ")
# hour = eval(input("How many hours ahead? " ))
# if unit_tidaud == am:
#     ahead = user + hour
#     print(f"New hour: { ahead % 12 } pm")
# elif unit_tidaud == pm:
#     ahead = user + hour
#     print(f"New hour: { ahead % 12 } am")

#          QUESTION 12
# 12. A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly
# how much candy is in the bowl, then you win all the candy. You ask the person in charge the
# following: If the candy is divided evenly among 5 people, how many pieces would be left
# over? The answer is 2 pieces. You then ask about dividing the candy evenly among 6 people,
# and the amount left over is 3 pieces. Finally, you ask about dividing the candy evenly among
# 7 people, and the amount left over is 2 pieces. By looking at the bowl, you can tell that there
# are less than 200 pieces. Write a program to determine how many pieces are in the bowl.

# bowl = eval(input(" enter a number: "))
# if bowl < 200:
#     five_people = bowl // 5
#     six_people = bowl // 3
#     seven_people = bowl // 7
#     if five_people == 2:
#         print(five_people)
#     elif six_people == 3:
#         print(six_people)
#     elif seven_people == 2:
#         print(seven_people)
#     print(five_people+six_people+seven_people)

#          QUESTION 13
# 13. Write a program that lets the user play Rock-Paper-Scissors against the computer. There
# should be five rounds, and after those five rounds, your program should print out who won
# and lost or that there is a tie.

# from random import *

# print("Daud, I am thinking of a number....")
# for i in range(2):
#     guess = randint(0,100)
#     daud = eval(input("Daud guess the number: "))
#     computer = randint(0,100)
#     print("Computer Guess the number:", computer)
#     if computer == guess and daud == guess:
#         print("Computer and Daud are correct..")
#     elif computer != guess and daud != guess:
#         print("Computer and Daud are wrong..")
#         print("The guessed number is ", guess)
#     elif daud != guess and computer == guess:
#         print("Daud is wrong. ")
#         print("computer is correct. ")
#     elif computer != guess and daud == guess:
#         print("computer is wrong. ")
#         print("Daud is correct. ")
   
    
































