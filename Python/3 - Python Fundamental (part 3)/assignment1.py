# Q1 - Ask the user for a stirng and check whether it is a palindrome or not. 
# A palindrome is a string which is same when we read it forward and backward. E.g. "madam", "racecar"

# [Hint] - A palindrome string is equal to the reversed version of the string. We can use a loop to reverse the string manually. 

# name = input("enter string ")

# name = "madam"

# reverse_str = name[::-1]

# if(name == reverse_str):
#     print("Palindrome")
# else:
#     print("not palindrome")

# Q-2 - Given a list of integers compute the average of all numbers in the list

# marks = [89,74,85,98,69,98]
# sum = 0

# for i in range(0,len(marks)):
#     sum += marks[i]

# ans = float(sum // len(marks))
# print(ans)


# Q-3 Input two lists of integers from the user. Merge them into one list and sort the result.
# E.g. - List1 = [1,2,7], list2= [2,4,5] result = [1,2,3,4,5,7]

# List1 = [1,2,7,3039,309843,44393]
# list2= [2,4,5,3,39039,84984,8397849]


# result = List1 + list2
# result.sort()
# ans = set(result)

# print(ans)

# # Method 2 
# unique_elemetns = set(List1 + list2)
# print(sorted(unique_elemetns))


# Q4 - Given a tuple of integers, create:
# A tuple of all even numbers
# A tuple of all odd numbers

# mix_tuple = (483,84,389,849,372,4882,4832,483,382,448,37,8947,8098)

# odd_list = []
# even_list = []

# for i in mix_tuple:
#     if(i % 2 == 0):
#         even_list.append(i)
#     else:
#         odd_list.append(i)

# even_tuple = tuple(even_list)
# odd_tuple = tuple(odd_list)

# print(even_tuple)
# print(odd_tuple)



# Q5 - Create a dictionary where keys - student names and value - marks(integer)
# Write a menu-based program where user press a key ('A','B','C','D') depending on the opeartion they want to perform on the dictionary:
# A - Add a studnet
# B - Update the marks
# C - Serach for a student
# D - Display all student and marks 



# students = {}  # <-- define dictionary OUTSIDE the loop

# while True:
#     print("\nPress A - Add a student")
#     print("Press B - Update marks")
#     print("Press C - Search for a student")
#     print("Press D - Display all students and marks")
#     print("Press E - Exit")

#     choice = input("Enter your choice: ").upper()


#     if choice == "A":
#         name = input("Enter student name")
#         marks = int(input("Enter marks out of 100"))

#         students[name] = marks
#         print("Student added successfully")
#     elif choice == "B":
#         name = input("Enter name of student for update marks of these student")

#         if name in students:
#             marks = int(input(f"Enter marks out of 100 of {name}"))

#             students[name] = marks
#             print("Marks updated succesfully")
#         else:
#             print("student not found in record")
    
#     elif choice == "C":
#         name = input("Enter student name for search")

#         if name in students:
#             print(f"{name} : {students[name]}")
#         else:
#             print("Student not found in record")
#     elif choice == "D":
#         if students:
#             print("\n All student and it's marks")

#             for name, marks in students.items():
#                 print(f"{name} : {marks}")
#         else:
#             print("No records available ")
#     elif choice == "E":
#         print("Thank you visit again \n")
#         break
#     else:
#         print("Wrong input \n ")

# Q6 - Given a list of words = ["apple", "banana", "kiwi", "cherry", "mangor"]
# create a dictionary that maps each word to its length. 
# Example : {"apple":5, "banana" : 6, "kiwi": 4, ...}

# words = ["apple", "banana", "kiwi", "cherry", "mangor"]
# new_words = {}

# for i in range(len(words)):
#     new_words.update({
#         words[i] : len(words[i])
#     })

# print(new_words)

# Q7 - Write a program that takes a string from the user and prints the number of spaces in the string

# inp_str = input("Enter a words to count spaces ")

# count=0

# for ch in inp_str:
#     if ch == " ":
#         count+=1
# print("Total space in string - ", count)

# Q8 - Write a program to check whether two lists share no common elements

# share no common elements list1 = [1,2,3,4] list2= [5,6,7,8]
# share common elements list1 = [1,2,3] list2 = [3,4]


# list1 = [1,2,3,4] 
# list2= [5,6,7,8]

# a = set(list1)
# b = set(list2)


# ans = a.intersection(b)
# print(ans)

# list_x = [1,2,3] 
# list_y = [3,4]

# c = set(list_x)
# d = set(list_y)

# ans1 = c.intersection(d)
# print(ans1)


# Q9 - Given a list, print all elements that apper more than once in the list. Hint[-use sets]


# def find_duplicates(input_list):
#     """
#     Finds and returns a list of all elements that appear more than once in the input list.
#     """
#     seen = set()
#     duplicates = set()

   
#     for element in input_list:
        
#         if element in seen:
#             duplicates.add(element)
#         else:
#             seen.add(element)

#     return list(duplicates)


# my_list = [1, 5, 3, 2, 5, 1, 4, 1, 9, 3, 7]
# result = find_duplicates(my_list)

# print(f"Original List: {my_list}")
# print(f"Elements appearing more than once: {result}")

# Q 10 - Ask the user for a string and print: Q 10• All unique characters• The count of unique characters

# user_input = input("Enter a string: ")

# unique_chars = sorted(set(user_input))

# print("Unique characters:", unique_chars)
# print("Count of unique characters:", len(unique_chars))
