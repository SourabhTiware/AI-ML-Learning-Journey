# Q1- Create a BankAccount class with attributes account_number,owner_name, and balance. 
# Add methods to deposit, withdraw and check balance

# class BankAccount:

#     def __init__(self,account_number, owner_name, balance=0):

#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance
    
#     def deposit(self,add_amount):

#         if add_amount <=0:
#             raise ValueError("Deposite amount should be 1 or greater")
        
#         self.balance += add_amount
#         print(f"{self.owner_name} in your acount no {self.account_number} creadit amount {self.balance} and total balance {self.balance}")
    
#     def withdraw(self,with_amount):
        
#         if with_amount <= 0: 
#             raise ValueError("Withdrawal amount should be 1 or greater")
#         elif with_amount>self.balance:
#             raise ValueError("Insufficient account balance")
        
#         self.balance -= with_amount
#         print(f"{self.owner_name} in your account no {self.account_number} debit total amount {with_amount} and balance {self.balance}")
    
#     def check_balance(self):
#         return self.balance
    
# b = BankAccount(111, "sourabh", 500)

# b.deposit(200)
# b.withdraw(100)
# print(b.check_balance())
# b.deposit(3000)



# Q2 - Create a class Book with the following attributes:
# title, author, list of reviews
# and add methods to:
# add a new review, count reviews, display all reviews


# class Book:

#     review = []
#     def __init__(self, title, author, reviews):
#         self.title = title
#         self.author = author
#         self.reviews = reviews
    
#     def add_review(self,new_reviews):
#         self.review.append(self.reviews)
#         self.review.append(new_reviews)
#         print("review added successfully")

    
#     def count_review(self):
#         self.count = len(self.review)
#         print(f"total count of review {self.count}")
    
#     def display_review(self):
#         print(f"Total reviews = {self.review}")

# b = Book("Life", "sourabh","Best life lesson")

# print(b.title)
# print(b.author)
# print(b.reviews)

# b.add_review("new one")
# b.count_review()
# b.display_review()

# Q3 - Create a class Student with private attributes __name, __roll_no and __marks.
# Provide getter and setter methods with validation (e.g. marks cannot be negative, roll number has to be between 1 & 100 and name cannot be empty)

# class Student:
    
#     def __init__(self,name,roll_no,marks):
#         self.__name = name
#         self.__roll_no = roll_no
#         self.__marks = marks
        
    
#     def get_info(self):
#         print(self.__name,self.__roll_no,self.__marks)
    
#     def set_info(self,stu_mark, stu_roll, stu_name):
#         if(stu_mark>0):
#             self.__marks = stu_mark
#             print("marks updated successfully")
#         else:
#             print("marks should be greater than 0")

#         if(stu_roll>0 and stu_roll <= 100):
#             self.__roll_no = stu_roll
#             print("roll number updated successfully")
#         else:
#             print("marks should be between 0 to 100")
        
#         if(len(stu_name)>0):
#             self.__name = stu_name
#             print("name updated successfully")
#         else:
#             print("name should not be empty")

    
# s = Student("",2,33)
# s.set_info(89,3,"sourabh")
# s.get_info()

# Q4 - Create a class Shape with a method area()
# Create subclass Circle, Rectangle and Triangle that override the area() method

# class Shape():

#     def area():
#         pass

# class Circle(Shape):
#     def __init__(self,r):
#         self.r = r
    
#     def area_circle(self):
#         area = 3.14 *(self.r**2)
#         return area

# class Rectangle(Shape):
#     def __init__(self,l,w):
#         self.l = l
#         self.w = w
    
#     def area_rectangle(self):
#         area = self.l * self.w
#         return area

# class Triangle(Shape):
#     def __init__(self,b,h):
#         self.b = b
#         self.h = h
    
#     def area_triangle(self):
#         area = 1/2 * (self.b * self.h)
#         return area

# c = Circle(3)
# print(c.area_circle())

# r = Rectangle(4,3)
# print(r.area_rectangle())

# t = Triangle(3,2)
# print(t.area_triangle())

# Q5- Create a base class vehical with attributes like brand and model. create two subclass Car and Bike that add
# extra attributes - seates (in car) & engine_cc (in Bike)

# class Vehical():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

# class Car(Vehical):
#     def __init__(self,brand,model,total_seats):
#         super().__init__(brand, model)
#         self.total_seats = total_seats
    
#     def get_info(self):
#         return f"The car brand is {self.brand} and model is {self.model} with total {self.total_seats} seats"

# class Bike(Vehical):
#     def __init__(self,brand,model,engine_power):
#         super().__init__(brand,model)
#         self.engine_power = engine_power
    
#     def get_info(self):
#         return f"The Vehical brand is {self.brand} and model is {self.brand} with engine power {self.engine_power}"

# c = Car("Tata Motor","BS-IV", 23)
# print(c.get_info())

# b = Bike("Hero Motar", "splendor", "125 CC")
# print(b.get_info())
    



# Q-6 Create an abstract class Employee with an Abstract method. calculate_salary().
# Create subclass Intern, FullTimeEmployee and ContractEmployee that implement the method differently

# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary():
#         pass
# class Intern(Employee):
#     def __init__(self,name,basic_pay,tax,pf):
#         self.name = name
#         self.basic_pay=  basic_pay
#         self.tax = tax
#         self.pf = pf
    
#     def calculate_salary(self):
#         salary = self.basic_pay + self.tax + self.pf
#         return salary

# class FullTimeEmployee(Employee):
#     def __init__(self,name,basic_pay,tax,pf,bonus):
#         self.name = name
#         self.basic_pay=  basic_pay
#         self.tax = tax
#         self.pf = pf
#         self.bonus = bonus
    
#     def calculate_salary(self):
#         salary = self.basic_pay + self.tax + self.pf+self.bonus
#         return salary

# class ContractEmployee(Employee):
#     def __init__(self,name,basic_pay,tax,small_bonus):
#         self.name = name
#         self.basic_pay = basic_pay
#         self.tax = tax
#         self.small_bonus = small_bonus

#     def calculate_salary(self):
#         salary = self.basic_pay + self.tax + self.small_bonus
#         return salary

# i = Intern("Sourabh",10_000,200,500)
# print(i.calculate_salary())

# e = FullTimeEmployee("Rahul",40_000,400,300,1000)
# print(e.calculate_salary())

# c = ContractEmployee("Sakshi",4000,200,700)
# print(c.calculate_salary())


# Q7 - Create a class Person that allows the constructor to work with:
# name only
# name + age
# name + age + address
# As direct constrctor overloading (multiple constructor) are not allowed but we have to use default parameters to simulate constructor overloading

# class Person():
#     def __init__(self,name,age = None, address = None):
#         self.name = name
#         self.age = age 
#         self.address = address
    
#     @classmethod
#     def from_name(cls,name):
#         return cls(name)
    
#     @classmethod
#     def from_name_age(cls,name,age):
#         return cls(name,age)
    
#     @classmethod
#     def from_name_age_address(cls,name,age,address):
#         return cls(name,age,address)
    
#     def get_info(self):
#         print("Name: ",self.name)
#         print("Age: ", self.age)
#         print("Address: ",self.address)

# p1 = Person.from_name("sourabh")
# p2 = Person.from_name_age("Sourabh",25)
# p3 = Person.from_name_age_address("Sourabh",25,"Pune")

# p3.get_info()
# print("\n")
# p2.get_info()
# print("\n")
# p1.get_info()


# Q8 Create a class Player with:
#       a class variable player_count
#       instance variable name and level
# Track how man players were created


# class Player():
#     player_count = 0
#     name_level = []

#     def __init__(self,name,level):
#         self.name = name
#         self.level = level
#         self.player_count += 1

    
#     def get_info(self, new_name, new_level):
#         self.name = new_name
#         self.level = new_level
#         print(f"name = {self.name} and level is {self.level}")

#     def get_total_player(self):
#         return f"total player = {self.player_count}"
    
# p = Player("Sourabh","L3")
# p2 = Player("Rahul","L1")
# p.get_info("Rahul","L2")

# print(p.get_total_player())
    

# Q9 - Create the follwing classes: Herbivor, Carnivore, Ownivore with some attributes and methods. Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance works.
