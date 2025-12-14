#                                       Lec - 01 - File I/O
#                                       Lec - 02 - Operation on Files

# f = open("sample.txt","r")

# data = f.read()
# print(type(data))
# print(data)

# f.close()

# Read file line by line 

# f = open("sample.txt","r")

# # data = f.readline()
# # print(data)

# data = f.readline()
# # print(data)

# for x  in data:
#     print(x)

# f.close()


# Writting in existing data

# f = open("sample.txt","w")

# f.write("This is an overright file \n using write mode 'w' and write mode override the existing data")

# f.close()


#                                       Lec - 03 - Modes in File Operation

## r = reading [defalut]
## w = writting, truncates file first 
## x = creates new & open for writting
## a = writting, appends at end
## b = binary mode
## t = text mode [default]
## + = opens dist file for updater (r & w)

# f = open("sample.txt","w+")

# data = f.write("hello")

# print(f.read())

# new_file = open("sample2.txt","x")

# print(new_file.read())

# new_file = open("sample2.txt","r")
# print(new_file.read())



#                                       Lec - 04 - With Keyword

# with open("sample2.txt","r") as f:
#     data = f.read()
#     print(data)


#                                       Lec - 05 - Delete Files

# Remove files / Delete files from folder . if file is not present then throw the error.

# import os

# os.remove("sample2.txt")


#                                       Lec - 06 - Practice Problem
# Word search in file 

# search_word = "store"
# count = 1
# data = True

# with open("sample.txt", "r") as f:
#     while data:
#         data = f.readline()
#         if search_word in data:
#             print(f"{search_word} word found at line number = {count}")
#             break
#         count +=1


#                                       Lec - 07 - Exception Handling

# try:
#     x = int(input("Enter a number for divide"))
#     ans = 10 / x

# except ZeroDivisionError:
#     print(f"Divide by 0 is not allowed")
# except ValueError:
#     print(f"some error in your input value")
# else:
#     print(f"ans = {ans}")



#                                       Lec - 08 - finally Keyword

# try:
#     x = int(input("Enter a number for divide"))
#     ans = 10 / x

# except ZeroDivisionError:
#     print(f"Divide by 0 is not allowed")
# except ValueError:
#     print(f"some error in your input value")
# else:
#     print(f"ans = {ans}")

# finally:
#     print("End of Program")


#                                       Lec - 09 - List Comprehensions

# Normal Code / Logic for solving problem

# squares=[]

# for i in range(6):
#     squares.append(i*i)

# print(squares)


# Using List Comprehension

# sq = [i*i for i in range(6)]
# print(sq)


# There are multiple Way to write List comprehension 

# sq = [i*i for i in range(6) if i % 2 != 0]
# print(sq)


# -ve number  = 0

# nums = [-2,-3,3,4,-1,7]

# nums = [0 if val<0 else val for val in nums]
# print(nums)


# list lower to upper case

# lis = ["hello","python","apnacollege"]

# lis = [val.upper() for val in lis]
# print(lis)


#                                       Lec - 10 - Working with JSon Model

import json

# Json to Python Object 

# json_str = '{"name":"sourabh", "isTeacher":true}' 

# py_obj = json.loads(json_str)
# print(type(py_obj))
# print(py_obj)


# Python Object to the Json string

# py_obj = {
#     "name":"sourabh",
#     "age":25
# }

# json_str = json.dumps(py_obj)
# print(type(json_str))
# print(json_str)


# Let's try with files (Json - data.json)

# Improt Data Json to Pyton object

# with open("data.json","r") as f:
#     py_obj = json.load(f)
#     print(type(py_obj))
#     print(py_obj)


# Export Data Python to Json obj using write mode "w"
data = {
    "name" : "sourabh",
    "age" : 25,
    "isTeacher" : True
}
with open("data.json","w") as f:
    json.dump(data,f, indent =4, sort_keys= True)