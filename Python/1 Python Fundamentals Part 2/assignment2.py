# Part 2 - Python Fundamental's 

# Q1 - WAP that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:
# If salary < 30,000 -> 5%, If salary is 30,000 to 70,000 -> 15%, If Salary > 70,000 -> 25%


# try:
#     salary = int(input("Enter your Salary "))
#     if(salary < 30000):
#         print("Final tax rate is 5% ")
#     elif ((salary <= 30000) or (salary <= 70000)):
#         print("Final tax rate is 15% ")
#     elif (salary >70000):
#         print("Final rate is 25% ")
#     else:
#         print("Wrong Input")

# except ValueError:
#     print("Wrong input")

# Q2 - Write a function that takes two integer a and b and prints all even numbers between them (inclusive)

# def even_number(a,b):
#     for i in range(a,b+1):
#         if(i % 2 == 0):
#             print(i)

# even_number(1,10)

# Q3 - Write a function that prints the digits of a number, n. for e.g. n=312, there are 3 digits in it 3, 1, and 2 & we need to print them

# def count_digit(num):
#     count = 0

#     while(num > 0):
#         count +=1
#         num = num // 10
#     print("Total count =",count)

# count_digit(453)

# Q4- Write a function to return the count the number of digits in a number n. 
# refer 3rd question

# Q5 - Write a fucntion to return the sum of digits of a number n. 


# def sum_of_digit(num):
#     sum = 0

#     while(num > 0):
#         ld = num % 10
#         sum += ld
#         num //= 10
#     print("total sum of digit is =",sum)

# sum_of_digit(541)


# Q6 - write a program to print all numbers from 1 to 100 that are divisbile by both 3 and 5

# print("3 and 5 divisible number")
# for i in range(1, 101):
#     if((i % 3 == 0) or (i % 5 == 0)):
#         print(i)


# Q7 - Design a program to continuously input a number n from user and print if it is positive or negative until the user enters "Quit"

# while (True):
#     choice =input("enter your choice and want to Quit enter 'quit' ")
#     print("Your choice is ",choice)
    
#     if (choice == "quit"):
#         print("Thank you visit again")
#         break



# Q8 - Let's create a simple Calculate that performs arithmetic opeartions. create a function calculators (a,b,opeartion) that performs addition, substraction, multiplication or division based on the opeartion parameter. 
# [opeartion parameter can have values '+', -, * & /]

# def calculators():
#     while(True):
#         print("Welcome to our calculator")
#         print("for addition press 1 ")
#         print("for substraction press 2 ")
#         print("for multiplication press 3 ")
#         print("for division press 4 ")
#         print("for division press 0 ")

#         operation = int(input(""))

#         match operation:
#             case 1:
#                 print("Great, You choose addition opeartion ")
#                 a =int(input("enter number 1 "))
#                 b =int(input("enter number 2 "))
#                 print("Total addition of 2 number = ", a+b, "\n")
#             case 2:
#                 print("Great, You choose substraction opeartion  ( b-a ) ")
#                 a =int(input("enter number 1 "))
#                 b =int(input("enter number 2 "))
#                 print("Total substraction of 2 number (b-a) = ", b-a, "\n")
#             case 3:
#                 print("Great, You choose multiplication opeartion ")
#                 a =int(input("enter number 1 "))
#                 b =int(input("enter number 2 "))
#                 print("Total multiplication of 2 number = ", a*b, "\n")
#             case 4:
#                 try:
#                     print("Great, You choose divistion opeartion ( a/b )")
#                     a =int(input("enter number 1 "))
#                     b =int(input("enter number 2 "))
#                     print("Total divistion of 2 number = ", a//b, "\n")
#                 except ZeroDivisionError:
#                     print("Error: division by zero.")
#             case 0:
#                 print("Thank You visit again")
#                 break
#             case _:
#                 print("Wrong input \n")

# calculators()


# Q9 - Write a function is_prime(n) that return True if n is a prime number and False otherwise, using a loop. 

# [Hint 
# 1. We only check prime for 2 or numbers greater than 2. 2 is the smallest prime number. 
# 2. A non-prime number, n, will always get divided by atleast one number in range [2, n-1]

# Eg- For number 9 we'll check in range (2,8) & it'll get divided by 3. so 9 is non-prime & we'll return false for it.
# For number 7 we'll check in range (2,6) & it won't get divided by any. so 7 is prime & we'll return true for it ]. 


# def is_prime(n):
#     if(n >= 2):
#         if(n == 2):
#             print("number is prime number ")
#         else:
#            for i in range(2, n):
#               if(n % i == 0):
#                 print("number is not prime number")
#                 break
#               else:
#                 print("Number is prime number")
#                 break
#     else:
#         print("Number should be greater or greater than equal to 2 ")


# n = int(input("Enter number for check prime or not "))

# is_prime(n)


# Q-10 - Let's create a "Number Guessing Game". Given a secret number (alerady decided by you), Write a program that asks the user to guess it and print's:
# "Too high" if the guess is above the number
# "Too low" if the guess is below
# "Correct!" if the guess matches

while(True):
    guess = int(input("Enter guessed number "))
    num = 25

    if(guess == num):
        print(guess ,"is correct guess number")
        break
    else:
        if(guess > num):
            print("Too High guess number \n ")
        else:
            print("To Low guess number \n")
