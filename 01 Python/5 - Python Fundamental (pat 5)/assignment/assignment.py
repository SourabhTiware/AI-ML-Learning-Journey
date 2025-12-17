# Q1 - Create a program that:
#      1. Opens a file "names.txt" in write mode
#      2. Writes 5 names (one per line) entered by the user
#      3. Then opens the same file in read mode and prints all names

# with open("name.txt","r") as f:
#     # data = f.write("Sourabh")
#     print(f.read())

# with open("name.txt","a") as f:
#     data = f.write("\nakahsy\nram\nBob")

# with open("name.txt","r") as f:
#     # data = f.write("Sourabh")
#     print(f.read())


# Q2 - Create a program that:
#   1. Opens a file "log.txt" in append mode
#   2. Adds a new log entry (like "program run successfully")
#   3. Opens the file read mode and prints all logs

with open("log.txt","a+") as f:
    f = f.write("Program run successfully")
    print(f.readline)