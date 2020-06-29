        ## EXERCISE 5.9 SOLUTIONS

        #1
# 1. Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
# 1.

# count = 0
# for i in range(1,100):
#     if ((i+1) % 2)== 1:
#         count = count + 1

# print(count)

        #2
# 2. Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
# 4 and how many end in a 9.

# count = 0
# count2 = 0
# for i in range(1,100):
#     if ((i+1) % 2)== 4:
#         count = count + 1
#     elif ((i+1) %  2) == 9:
#         count2 = count2 + 1

# print("ends with 4",count)
# print("ends with 9",count2)

                #3
# 3. Write a program that asks the user to enter a value n, and then computes (1 + 1/2 + 1/3 +···+ 1/n) − ln(n). The ln function is log in the math module.

# count = 1
# user = eval(input("Enter a number: "))
# for i in range (user):
#         compute = count / (i+1)
# print(compute + (i))

                #4
# 4. Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000.
# num1 = -1
# num2 = 1
                #TO BE SOLVE LATER.....

#                 #5
# 5. Write a program that asks the user to enter a number and prints the sum of the divisors of
# that number. The sum of the divisors of a number is an important function in number theory


# sum = 0
# user = eval(input("Enter a number: "))

# for i in range(user):
#         if user // 2 == 0:
#                 sum = sum + 1
# print(sum)

                #7
# 7. An integer is called squarefree if it is not divisible by any perfect squares other than 1. For
# instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
# numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
# divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
# tells them if it is squarefree or not

#  user = eval(input("Enter a number: "))
#  for i in range(user):
#          if user % i == 0 and user 

                #8
# 8. Write a program that swaps the values of three variables x, y, and z, so that x gets the value
# of y, y gets the value of z, and z gets the value of x.

# x = 2
# y = 3
# z = 4
# x,y,z = y,z,x
# print(x)
# print(y)
# print(z)

                #9
# 9. Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect
# cubes, or perfect fifth powers.

# sum1 = 0
# for i in range(1,1000):
#         if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
#                 sum1 = sum1 + 1
# print(sum1)

                #10
# 10. Ask the user to enter 10 test scores. Write a program to do the following:
# (a) Print out the highest and lowest scores.
# (b) Print out the average of the scores.
# (c) Print out the second largest score.
# (d) If any of the scores is greater than 100, then after all the scores have been entered, print
# a message warning the user that a value over 100 has been entered.
# (e) Drop the two lowest scores and print out the average of the rest of them.

# highest = 0
# lowest = 0
# for i in range(3):
#         user = int(input("Enter your test scores: "))
#         if user > highest:
#                 highest = user
#         if user :
#                 lowest = highest
# print("The highest Number is ", highest)
# print("The lowest Number is ", lowest)

                # 11
# 11. Write a program that computes the factorial of a number. The factorial, n!, of a number n is the
# product of all the integers between 1 and n, including n. For instance, 5! = 1 · 2 · 3 · 4 · 5 = 120.
# [Hint: Try using a multiplicative equivalent of the summing technique.]

# from math import factorial
# user = eval(input("Enter a factorial (!n): "))
# print(factorial(user))

#                 12
# 12. Write a program that asks the user to guess a random number between 1 and 10. If they guess
# right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give
# the user five numbers to guess and print their score after all the guessing is done.

from random import randint

# user_score = 1
# print("Welcome to the computer GUESSING GAME.....")
# name = input("What is your name: ")
# print(f"welcome { name }")
# for i in range(5):
#         guess = randint(1,2)
#         user = eval(input(f"{ name }, I am thinking of a number, Guess the numbers: "))
#         if user == guess:
#                 user_score = user_score + 10
#                 print("Correct, 10 points added...keep it up ")
#                 print(f'Your scores is: { user_score}')
#                 print(" ")
#         else:
#                 user_score = user_score - 1
#                 print(f"Wrong, I was thinking of {guess}: 1 point has been deducted from your scores")
#                 print(f'Your scores is: { user_score}')
#                 print(" ")
# print("Total scores is ", user_score)

                # 13
# 13. In the last chapter there was an exercise that asked you to create a multiplication game for
# kids. Improve your program from that exercise to keep track of the number of right and
# wrong answers. At the end of the program, print a message that varies depending on how
# many questions the player got right.


# correct = 0
# wrong = 0
# times = eval(input("How many questions do you which to solve? "))
# for i in range(times):
#         x = randint(1,10)
#         y = randint(1,10)
#         z = x * y
#         print(f"Questino {i +1} : { x } * { y }: ")
#         user = eval(input(">> "))
#         if user == z:
#                 correct = correct + 1
#         else:
#                 wrong = wrong + 1
# print(f"Out of {times } Questions, you scored { correct} and failed { wrong }")
# if correct > wrong:
#         print(f"Good job, you have won the Quiz with { times - wrong } points ")
# elif correct == wrong:
#         print("Good job, you have neither lost nor won")
# else:
#         print(f"Sorry, you lost the game with { times - correct } points lost. ")


                #14
# 14. This exercise is about the well-known Monty Hall problem. In the problem, you are a contestant on a game show. 
# The host, Monty Hall, shows you three doors. Behind one of those
# doors is a prize, and behind the other two doors are goats. You pick a door. Monty Hall, who
# knows behind which door the prize lies, then opens up one of the doors that doesn’t contain
# the prize. There are now two doors left, and Monty gives you the opportunity to change your
# choice. Should you keep the same door, change doors, or does it not matter?
#         (a) Write a program that simulates playing this game 10000 times and calculates 
# what percentage of the time you would win if you switch and what percentage of the time you
# would win by not switching.
#         (b) Try the above but with four doors instead of three. There is still only one prize, and
# Monty still opens up one door and then gives you the opportunity to switch.














































































