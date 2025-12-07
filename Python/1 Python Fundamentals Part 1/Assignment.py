# Q1 - WAP that asks the user for their name and age, then prints a sentence like:
# Hello Sourabh, You are 25 years old!

# name = input("Enter your name ")
# age = int(input("Enter your age "))

# print("Hello",name,"You are", age, "years old!")

# Q2 - Take two numbers as input from the user and print their sum, difference, product and quotient

# a = int(input("Enter number 1st "))
# b = int(input("Enter number 2nd "))

# print("Addication = ",a+b)
# print("Substraction = ",a-b)
# print("Multiplication = ",a*b)
# print("Division = ",a/b)

# Q3 - Ask the user to enter two integers and one float. Convert them all to floats and print their average.

# a = int(input("Enter 1st number "))
# b = int(input("Enter 2nd number "))
# c = float(input("Enter 3rd number "))

# avg = (a+b+c)/3

# print(avg)

# Q4 - The user enters a string containing a number (e.g. "45"). Convert it to:

# an integer
# an float
# a string again

# print all three values with their types. 

# random_num = 45

# print(int(random_num), type(random_num))

# # float
# int_to_float = float(random_num)
# print(float(int_to_float), type(int_to_float))

# # String
# int_to_str = str(random_num)
# print(int_to_str, type(int_to_str))

# # float to String
# float_to_str = str(int_to_float)
# print(float_to_str, type(float_to_str))

# Q5. Evaluate and print the result of the following expression:
# Based on what you learnt in the lecture explain why the output is what it is.


# x = 10 + 3 * 2 ** 2
# print(x)


# Q6 - WAP to Swap values of two numbers entered by the user

# num1 = int(input("enter 1st number "))
# num2 = int(input("Enter 2nd number "))

# temp = num1
# num1 = num2
# num2 = temp

# print("after swap num1 = ", num1)
# print("after swap num2 =", num2)


# Q7 Ask the user for a temperature in celsius (string input). convert it to float,then calculate and print temperature in fahrenheit.
# Conversion forumula: FahrenheitTemp = (CelsiusTemp * (9/5)) + 32


# temperature = float(input("Enter a Temperature"))

# fahrenheit_temp = (temperature * (9/5) + 32)
# print(fahrenheit_temp)

# Q8 - Take the radius (r) as user input and print the area. 
# use the formula: Area = Pia * r**2 ( value of Pia = 3.14)

# radius = float(input("Enter radius "))
# pia = 3.14

# area = pia * (radius**2)

# print(area)


# Q9 Ask the user for: Principal(P), Rate(R), Time(T). Convert all to float and compute Simple interest:
# SI = (P * R * T) / 100


# principal = float(input("Enter pricipal amount "))
# Rate = float(input("Enter rate of intrest "))
# Time = float(input("Enter total time period for loan repayment "))

# si = (principal * Rate * Time) / 100
# print(si)

# Q-10 Take a decimal number as input (like 45.78) and output its:
# integer part - 45
# fractional part - 78

num = input("Enter a decimal number: ")

# Split into integer and fractional parts
if '.' in num:
    integer_part, fractional_part = num.split('.')
    fractional_part = '.' + fractional_part
else:
    integer_part = num
    fractional_part = "No fractional part"

print("integer part -", integer_part)
print("fractional part -", fractional_part)
