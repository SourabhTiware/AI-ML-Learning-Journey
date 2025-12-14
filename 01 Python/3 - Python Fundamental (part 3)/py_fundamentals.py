#                                           Lec-01 - String

# word = "python "

# print("total character in string = ",len(word))

# Acces the string character by manually 

# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])

# Accessing the string character using loop

# print("\n \n ")
# for i in word:
#     print(i)


# Concatenate String using " + " operator

# w1 = "I love"
# w2 = "python"

# sentence = w1 + " " + w2
# print(sentence)


#                                           Lec-02 - Slicing in String

# word = "Hello, I'm Sourabh"

# # 0 to end of the sting
# print(word[:])

# # 0 to end of the string in another way
# print(word[0:]) # by default it's going to the end of the stirng 

# # 0 to end of the string in another way
# print(word[:len(word)])

# # 2nd position to the 6 th position ( Last index is not including in final output. )
# print(word[2:7])

# # 11 th position to the end of the string
# print(word[11:])

# # 7th position to the 10 th position ( last index is not included in final output)
# print(word[7:11])


#                                           Lec-03 - String formatting f-string & format()

# 1. format function - python version 3. 

# a = 5
# b = 10

# sum = a+b

# print("sum is {}".format(sum)) # normal formatting
# print("language is {}".format("python"))  # In format string also include string format. 
# print("sum of {} & {} is {} ".format(a,b,sum))


# 1.2 Index formatting. Not mostly use

# print("sum of {0} & {1} is {2}".format(a,b,sum))
# print("sum of {1} & {0} is {2}".format(a,b,sum))

# 1.3 Value based formatting

# print("value of variable {a} & {b}".format(a=4,b=3))

# 2. f-string formatting (Literal string interpolation). mostly used in python code 

# print(f"sum of {a} & {b} is = {a+b}")



#                                           Lec-04 - List in python

# marks = [98, 87, 78, 87,"sourabh", 96.43, "python"]
# print(marks)
# print(marks[0])
# print(marks[-2])

# Slicing on list 

# print(marks[:])
# print(marks[2:6])
# print(marks[4:])
# print(marks[-5:-1])


#                                           Lec-05 - List methods (function)

nums=[1,2,3]

# # append(value) - it's add and element to the end of the list
# nums.append(4)
# print(nums)

# inset(idx, value) - it's add an element in list, according to the index.
nums.insert(2,10)
print(nums)

# The insert(10, 39) uses index 10, exceeding the list's length of 4, so Python appends 39 to the end instead of 
# raising an error. The final list becomes [1, 2, 10, 3, 39]

# nums.insert(10,39)
# print(nums)

# # sort() - it is sort the list in ascending order
# nums.sort()
# print(nums)

# # sort(reverse=True - it is sort in desending order
# nums.sort(reverse=True)
# print(nums)

# # reverse() - it is an reverse the list
# nums.reverse()
# print(nums)


#                                           Lec-06 - using loops with lists

# list_num = [19,23,48,23,3,42,4]
# num=3
# idx = 0

# for val in list_num:
#     if(val == num):
#         print(f"{num} is found at index {idx}")
#         break
#     idx += 1


#                                           Lec-07 Tuple in python

tup = (1,2,3,4,5)

# Accessing the tuple element.
# print(tup[3])

# Can't assign new value of tuple index. it can casue error
# tup[3] = 3
# print(tup)

# but over write the tuple value. assign new value to the tuple. 

# tup = (88,78,97, 34,5,4)
# print(tup)

# for val in tup:
#     print(val)


#                                           Lec-08 - Tuple Method

# t.index(val) - index method, print the index of value

# t = (2,3,4,2,4,5,2,4,5,6,2)

# print(t.index(2))

# t.count(val) - count the total value appeared in tuple

# print(t.count(2))


#                                           Lec-09 - Dictionary in python

# info = {
#     "name" : "sourabh",
#     "cgpa" : 9.2,
#     "subject" : ["math", "science"],
#     3.14: "PI"
# }

# # print the dict 

# print(info)

# # Accessing the value using key

# print(info["name"])

# # Dict is mutable

# info["cgpa"] = 9.6
# print(info)


#                                           Lec-10 - Dictionary methods

# print the all keys of dictionary 

# dict_key = info.keys()
# print(dict_key)

# # print the all values of dictionary 

# dict_val = info.values()
# print(dict_val)

# # pirnt all items of the dictionary (key:value) 

# dict_item = info.items()
# print(dict_item)

# # print the value through the key

# print(info.get("name"))
# print("end of get method")

# # update the dictionary. 

# info.update({
#     "city" : "kolhapur"
# })

# print(info)


#                                           Lec-11 - sets in python


# s = {1,2,3,4,5}
# print(s)

# # empty set is always consider as dictionary
# t = {}
# print(type(t))

# # do declare empty set consider following syntax

# x = set()
# print(type(x))


#                                           Lec-12 - Set Method

# p = {1,2,3,4,5}

# # p.add(val)        Add a value

# p.add(6)
# print(p)

# # p.remove(val)     Remove a value

# p.remove(2)
# print(p)

# # p.pop()           Remove a randome value from set

# p.pop()
# print(p)

# # a.union(b)     Return union of 2 sets 

# a = {33,22,55,44}
# b = {88,33,22,77}

# print(a.union(b))


# # p.intersion(set2) Return the inserseciton of two sets

# print("intersection")
# print(a.intersection(b))







