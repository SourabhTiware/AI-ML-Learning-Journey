#-----------------------------------------------------------------------------
# Lec 1: Conditional Statement
#-----------------------------------------------------------------------------
# print("\nLec 1: Conditional Statement\n")


# print("Python conditional statement keyword\nif\nelif\nelse")

# print("\nVoting Program")

# age = int(input("\nEnter you age: "))

# if age >= 18:
#     print("You can vote")
#     print("you can drive")
# else:
#     print("You can't vote")
#     print("You can't drive")

# print("\nTraffic light Program")

# color =input("Enter traffic light color: ")

# if color == "yellow":
#     print("look")
# elif color == "red":
#     print("wait")
# elif color == "green":
#     print("go")
# else:
#     print("Wrong color input")


#-----------------------------------------------------------------------------
# Lec 2: Practice Example on Conditional Statement
#-----------------------------------------------------------------------------
# print("\nLec 2: Practice Example on Conditional Statement\n")

# print("Ques 1: age less than 13 print child \nage is between 13-18 print teenager \nand age is greater than 18 print adult")

# age = int(input("Enter you age: "))

# if(age >= 0 and age < 13):
#     print("child")
# elif (age >= 13 and age <18):
#     print("teenager")
# elif(age >= 18 and age <=60):
#     print("adult")
# elif(age >60):
#     print("oldage")
# else:
#     print("Your input age is wrong")

# print("\nQues 2: Design login system using python ")

# username = "sourabhtiware"
# password = 1234

# user_name = input("\nEnter your username : ")
# pass_word = int(input("\nEnter you password : "))

# if(username == user_name and password == pass_word):
#     print("\nLogin successfully")
# else:
#     print("\nWrong username or password")


# print("\nQues3: check number is multiple of 5 or not")

# num = int(input("enter number "))

# if(num % 5 == 0):
#     print("number is multiple of 5")
# else:
#     print("number is not multiple of 5")


#-----------------------------------------------------------------------------
# Lec 3: Odd or Even
#-----------------------------------------------------------------------------
# print("\n Lec 3: Odd or Even\n")


# print("\nPrint any give number is odd or even")

# num = int(input("\nEnter number to check odd or even : "))

# if( num <= 0):
#     print("Wrong input")
# elif ( num % 2 == 0):
#     print("Even number ")
# else:
#     print("Odd number")


#-----------------------------------------------------------------------------
# Lec 4: Nesting
#-----------------------------------------------------------------------------
# print("\n Lec 4: Nesting\n")

# print("Ques: check user name and password, it's correct print sucess else check again username wrong and password wrong")

# user_name = input("\nenter uesrname : ")
# pass_word = input("\nenter password : ")

# if(user_name == "admin" and pass_word == "pass"):
#     print("\nSuccess")
# else:
#     if( (user_name != "admin") and (pass_word != "pass")):
#         print("\nusername and password both are wrong")
#     elif (user_name != "admin"):
#         print("\nWrong username")
#     else:
#         print("\nWrong password")


# -----------------------------------------------------------------------------
# Lec 5: Match Case in python
# -----------------------------------------------------------------------------
# print("\nLec 5: Match Case in python\n")

# color = input("enter color: ")

# match color:
#     case "Green":
#         print("\nGo")
#     case "Yellow":
#         print("\nLook")
#     case "Red":
#         print("\nStop")
#     case _:
#         print("Wrong input")


# -----------------------------------------------------------------------------
# Lec 6: Loops using while
# -----------------------------------------------------------------------------
# print("\nLec 6: Loops using while\n")

# print("\nQues: print 'Hello World' 10 times using while loops\n")

# i = 1; #iterator

# while(i <=10):
#     print("Hello World", i)
#     i += 1

# print("\nafter end of the loop, i value = ", i)


# -----------------------------------------------------------------------------
# Lec 7: Practice Example (Loops)
# -----------------------------------------------------------------------------
# print("\nLec 7: Practice Example (Loops)\n")

# print("Ques 1: WAP to print 1 to 10\n")

# i = 1

# while( i <= 10 ):
#     print(i)
#     i += 1

# print("Ques 2: WAP to print 10 to 1\n")

# j = 10

# while( j >=1):
#     print(j)
#     j -=1


# -----------------------------------------------------------------------------
# Lec 8: Multiplication Table of n 
# -----------------------------------------------------------------------------
# print("\nLec 8: Multiplication Table of n\n")


# n = int(input("Enter number "))

# i = 1

# while(i <=10):
#     print( n * i)
#     i +=1


# -----------------------------------------------------------------------------
# Lec 9: Break and Continue 
# -----------------------------------------------------------------------------
# print("\nLec 9: Break and Continue\n")

# print("Break keyword work like if condition is true then terminate the loop and \ncontinue keyword work like if condition is true then it's skip the following work and go towards to the loops\n")

# i = 1

# print("Break statement / keyword use")
# while( i <= 10):
#     if(i % 6 == 0):
#         break
#     print(i)
#     i += 1

# print("Continue Statemetn / keyword use")

# while (i <= 10):
#     if( i % 3 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


# -----------------------------------------------------------------------------
# Lec 10: for Loop 
# -----------------------------------------------------------------------------
# print("\nLec 10: for Loop \n")

# print("\nIt is use for the sequential traversal like - tuple, string, dict & array etc\n")

# word = "Hello World"

# 'in' => it is a membership operator => to check presence of value / variable. 
# also 'in' operator use with conditional operator.

# for var in word: 
#     print(var)

# if 'o' in word:
#     print("\n o exist into the word \n ")

# print("1 to 10 numbers using for loop + range function. \n range function create a sequence and it's start from 0 to n-1")

# for i in range(10):
#     print(i+1)

# print("\n count total count of i")

# character = "artificial Intelligence"
# count = 0

# for var in character:
#     if( var == 'i'):
#         count += 1
    
# print("\n total count of i : ", count)


# -----------------------------------------------------------------------------
# Lec 11: vowel count
# -----------------------------------------------------------------------------
# print("\n Lec 11: vowel count") 

# print("\n Ques: count total vowel in to the given string ")
# word = "artificial"

# count = 0

# for ch in word:
#     if( ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
#         count += 1
    
# print("\n Total count of vowel in give string:",count)


# -----------------------------------------------------------------------------
# Lec 12: range function
# -----------------------------------------------------------------------------
# print("\n Lec 12: range function")


# print("range function : generate sequence.\n range function have 3 parameter = start, 'stop', step: start by default intitial from 0, stop - compalsary define and step = by default setp increase +1\n also if you want to start from 2 or 3 or -5 it's valid and also you can manipulate the step like +2, +3 , -5\n -5 must be your stopping condition below 0.  ")

# print("\n print 0 to 5")

# for i in range(5):
#     print(i)

# print("\n print 1 to 5")

# for i in range(1,6):
#     print(i)

# print("\n print 1 to 10 even number ")

# for i in range(2, 11, 2):
#     print(i)


# -----------------------------------------------------------------------------
# Lec 13: Sum of N numbers
# -----------------------------------------------------------------------------
# print("\n Lec 13: Sum of N numbers ")

# print("\n sum of first N natural numbers")

# num = int(input("Enter value of N: "))

# sum = 0

# for i in range(1, num + 1):
#     sum += i

# print("\n sum of first N natural's number's : ",sum)



# -----------------------------------------------------------------------------
# Lec 14: Function's in python
# -----------------------------------------------------------------------------
# print("\n Lec 14: Function's in python ")


# print("\n function is blocks of statements that perform a specific task.\n Also they are resuable block of component or block of code.\n Their two method in function =>\n 1. Function Defination\n 2. Function call")

# print("Functiono Defination")

# Function Defination:

# def hello():
#     print("Hello")
#     print("from python")

# Function Calling - 1 call means run function 1 time, 2 call means run function 2 times.
# hello()

# hello()

# print("\n Create a function for calculate sum of two number's.")

# function defination

# def sum(a,b):
#     ans = a + b
    
#     return ans

# sum_of_number = sum(3,4)
# print(sum_of_number)

# print("sum of two number's : ", sum(4,5))


# -----------------------------------------------------------------------------
# Lec 15: Practice Example (functios)
# -----------------------------------------------------------------------------
# print("\n Lec 15: Practice Example (functios) ")

# print("Ques: write a function, take a 3 number's and return average value of 3 number's ")


# Function defination

# def average(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg

# ans = average(3,4,3)
# print("average of 3 number",f"{ans:.2f}")


# print("\n In function you can set default value's when input value is not provide with function arguments")

# print("\n when we set default value of any parameter, that time we want pass first non-default values and then pass default parameter. \n by mistake you pass default parameter first that condition you will get error")
# def sum( a, b=1 ):
#     ans = a + b
#     return ans

# print("sum of two number's :",sum(4,3))
# print("sum of two number's :",sum(4))



# -----------------------------------------------------------------------------
# Lec 16: Types of functions
# -----------------------------------------------------------------------------
# print("\n Lec 16: Types of functios ")

# print("\n In python two types of function's\n\n 1st - Built In function\n\n 1. input()\n 2. range()\n 3. print()\n 4. type() \n\n 2nd - user defined functon \n\n In previous lecture I can write multiple typs of function like,\n 1. sum of tw number() \n 2. avarage of 3 numbers()\n etc")
# print("\n When we write a function, those part of logic we want to use multiple time in application those part of code write it into a function,\n whenever those part of logic use, that time I will call the function. ")


# -----------------------------------------------------------------------------
# Lec 17: Lambada functions
# -----------------------------------------------------------------------------
# print("\n Lec 17: Lambada functions \n when will use lambada function - for the simple task. ")

# print("\n uses of lambada function = high order function")

# print("""First things first: it looks like you are hitting two very common speed bumps when learning Python. Don't worry, they are easy fixes!

# Let's break down exactly what happened, why you saw that strange <function <lambda>...> message, and how to call the function correctly.

# 1. The Spelling: It's lambda, not lambada
# While the Lambada is a fun dance from the 1980s, Python only understands lambda (without the 'a' in the middle).

# 2. Why you got <function <lambda> at ...>
# When you saw sum of two number : <function <lambda> at 0x000001B54A4EBAB0>, Python wasn't actually giving you an error. It was just telling you:

# "Hey, I found a lambda function sitting in my memory at this specific address, but you didn't tell me to execute it."

# In Python, if you print a function's name without using parentheses (), Python prints the identity of the function rather than running the code inside it.

# 3. The Error: Calling it without arguments
# A lambda function expects you to pass data into its variables. If you define a lambda that requires two numbers but you don't provide them, Python will throw a TypeError.

# Here is how to write and call it correctly:

# The Correct Syntax
# Python

# # Syntax: lambda arguments : expression
# calc_sum = lambda x, y : x + y
# How to execute (call) it:
# To actually get the sum, you must pass the numbers inside parentheses right next to the function name, just like a regular function.

# Python

# # Define the lambda function
# calc_sum = lambda x, y : x + y
# # Call the function by passing two numbers (e.g., 5 and 10)
# result = calc_sum(5, 10)

# print("Sum of two numbers:", result)
# Output:

# Plaintext

# Sum of two numbers: 15
# Summary of what to change:
# * Make sure it is spelled lambda.
# * Always use () and pass the required numbers when you want to use it (e.g., my_function(5, 10)).

# What kind of application or script are you trying to build with this lambda function?""")

# print("\n syntax of lambada function : lambada variable : express")

# print("\n calcualte sum of two number ")

# sum = lambda a, b : a + b

# print("\n sum of two number : ",sum(5,2))


# print("\n calcualte average of two number ")

# avg = lambda a, b : (a + b)/2

# print("\n average of two number : ",avg(5,2))


# -----------------------------------------------------------------------------
# Lec 18: Factorial of N
# -----------------------------------------------------------------------------
# print("\n Lec 18: Factorial of N ")

# def factorial_of_num(n):
#     fact = 1

#     for i in range(1, n+1):
#         fact *= i
#     return fact

# n = int(input("Enter value of n "))

# print("factorial of ",n,":",factorial_of_num(n))








