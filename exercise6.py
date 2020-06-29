  ## EXERCISE 6.11 SOLUTIONS

        #1
#  Exercises
# 1. Write a program that asks the user to enter a string. The program should then print the
# following:
# (a) The total number of characters in the string
# (b) The string repeated 10 times
# (c) The first character of the string (remember that string indices start at 0)
# (d) The first three characters of the string
# (e) The last three characters of the string
# (f) The string backwards
# (g) The seventh character of the string if the string is long enough and a message otherwise
# (h) The string with its first and last characters removed
# (i) The string in all caps
# (j) The string with every a replaced with an e
# (k) The string with every letter replaced by a space

#SOLUTION

# user = input("Enter a string: ")
# #(a)
# num = (len(user))
# print(num)
#(b)
# for i in range(10):
#     print(i+1," -- ",user)
#(c)
# print(user[:1])
#(d)
# print(user[:3])
#(e)
# print(user[-3:])
#(f)
# print(user[-1: :-1])
#(g)
# if len(user) > 7:
#     print(user[6:7])
# else:
#     print("User letter not up to seven characters.")
#(h)
# print(user[: : -1])
#(i)
# user = user.upper()
# print(user)
#(j)
# user = user.replace("a", "e")
# print(user)
#(k)
# for i in user:
#     user = user.replace(i, " ")
# print(user, end="")

#         #2
# 2. A simple way to estimate the number of words in a string is to count the number of spaces
# in the string. Write a program that asks the user for a string and returns an estimate of how
# many words are in the string.
#         SOLUTION
# countt = 0
# for a in user:
#     if a == " ":
#         countt = countt + 1
# print("You just entered ",countt + 1," words on the screen")

        #3
# 3. People often forget closing parentheses when entering formulas. 
# a program that asks the user to enter a formula and prints out whether
# the formula has the same number of opening and closing parentheses.
# countt = " "
# for i in user:
#     if len("(") == len(")"):
#         countt = countt + i
# print("closed")
    
#         4
# 4. Write a program that asks the user to enter a word and prints out whether that word contains
# any vowels.
# num = ""
# num2 = ""
# for i in user:
#         if i == "aeiou":
#         num ="Your word contain vowel."
# print(num)
#         else:
#         num2 = "you dont have a vowel letter in", user
# print(num2)

# print("hello," + user)
from random import randint
# timez = randint(1,5)
# for i in range (timez):
#         print("hello," + user)

# print(user, "printed ",timez+1,"times.")

# Example 3 Let us write a program that generates 10000 random numbers between 1 and 100 and
# counts how many of them are multiples of 12. Here are the things we will need:

# cou = 0
# for i in range(1000):
#         gen = randint(1,100)
#         if 12 % gen == 0:
#                 cou = cou + 1
# # print(cou)
# print(f"Hello, { user}.")

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# key = 'xznlwebgjhqdyvtkfuompciasr'
# secret_message = input('Enter your message: ')
# secret_message = secret_message.lower()
# for c in secret_message:
#         if c.isalpha():
#                 print(key[alphabet.index(c)],end='')
#         else:   
#                 print(c, end='')


# 1. Write a program that asks the user to enter a string. The program should then print the
# following:
# (a) The total number of characters in the string
# (b) The string repeated 10 times
# (c) The first character of the string (remember that string indices start at 0)
# (d) The first three characters of the string
# (e) The last three characters of the string
# (f) The string backwards
# (g) The seventh character of the string if the string is long enough and a message otherwise
# (h) The string with its first and last characters removed
# (i) The string in all caps
# (j) The string with every a replaced with an e

# user = input("Enter a string: ")
# # # for i in range(10):
# # #         print(user)
# # if "a" in user:
# #         print(user.replace("a","c"))

# (a) Without using the in operator, write a program that asks the user for a string and a letter
# and prints out whether or not the letter appears in the string.

# if index() == "a":
#         print("hello...")
# print(user[1:-1])

# s = 'abcdefghijklmnopqrstuvwxyz'
# for i in range(10):
#         print(s[randint(0, len(s)-1)], end='')
# # print()
# s = input('Enter a string: ')
# t = ''
# for i in range(10):
#         t = t + s[randint(0, len(s)-1)]
# print(t)
# name = input('Name: ')
# gender = input('Gender: ')
# formality = input('Formal/Informal: ')
# breakpoint = name.index(' ')
# first = name[:breakpoint]
# last = name[breakpoint+1:]
# if formality.lower() == 'formal':
#         if gender.lower() == 'male':
#                 print('Hello, Mr. ', last, '.', sep='')
#         else:
#                 print('Hello, Ms. ', last, '.', sep='')
# else:
#  print('Hello, ', first, '.', sep='')
# result=[]
# for i in [2]:
#         for j in [1,2,3,4]:
#                 result.append(i*j)
# print(result)
# help(result.append)

# spam = ""
# while True:
#         print("what is your name: ", )
#         spam = input()
#         if spam == "Dauda":
#                 break
# print("Thank you", spam)
# x = 0
# while x < 10:
#         if x == 4:
#                 continue
#         print(f"The value of X is {x}")
#         x +=1

# x = "Mathematics"
# for item in x:
#         if item == "e":
#                 break
# #         print(item)
# x = 1
# while x <= 5:
#         print(x)
#         x +=1
# else:
#         print("Thanks {}".format(x))


# def my_func():
#         x = 0
#         for i in range(1,20,2):
#                 x = x +1
#         return (x)

# result = my_func()
# print(result)
# x = 2
# while x <= 100:
#          print( x )
#          x +=2

# print("    *")
# print(" *     *")
# print("* * * * *")
# print("*        *")
# print("*        *")

# num1 = float(input(f">"))
# num2 = float(input(f">"))
# num3 = float(input(f">"))
# num4 = float(input(f">"))
# num5 = float(input(f">"))
# print(f"{num1} {num2} {num3} {int(num4)} {int(num5)}", sep="   ")
# for i in range(1, 20):
#         for j in range(i):
#                 print(randint(0,1), end='')
#         print() 
#Write a program that asks the user to enter 
# a number and prints out all the divisors of that
# number.
#  [Hint: the % operator is used to tell if a number is divisible by something. See Section
# 3.2.]


# from random import randint
# for i in range(2):
#         ram = randint(1,4)
#         print("I am thinking of a number, Guess the number: ")
#         com = randint(1,4)
#         compurer = print("Computer >>> ", com)
#         print()
#         user = eval(input("Dauda >>> "))
#         if user == ram:
#                 print("Dauda is correct! ")
#         elif com == ram:
#                 print("Compter is Correct!")
#         else:
#                 print(f"None is correct, I was thinking of {ram}")

max_num = 0
for i in range(4):
        user = eval(input("Enter a number: "))
        if user > max_num:
                max_num = user
print("The largest number is: ", max_num)




























































































