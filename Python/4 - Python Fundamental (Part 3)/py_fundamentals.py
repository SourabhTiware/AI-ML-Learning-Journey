#                                       Lec -01 - What is object oriented Programming
#                                       Lec -02 - Class and Object

# class Student:
#     subject = "python"
#     college = "apna college"
#     year = 2025-26

# stu1 = Student()
# stu2 = Student()

# print(stu1.subject, stu1.college, stu1.year)
# print(stu2.subject, stu2.college, stu2.year)


#                                       Lec -03 - Attributes and Methods
#                                       Lec -04 - Constructor - init() method
#                                       Lec -05 - Types of Constructors

# # Default Constructor 


# class Student:
#     def __init__(self):       # automatic called when object is created.
#         print("Constructor are called")

# stu1 = Student()


# Parameterized constructor 

# class Student:
#     def __init__(self,name):
#         self.name = name

# stu1 = Student("sourabh")
# stu2 = Student("Roshani")

# print(stu1.name)
# print(stu2.name)


#                                       Lec -06 - Attributes - Class & instance

# class Student:
#     college = "ABC college"        # class attribute
#     def __init__(self, name, gpa): # instance attributes
#         self.name = name
#         self.gpa = gpa

# stu1 = Student("Rahul", 8.7)
# stu2 = Student("Harshita", 9.4)

# print(f"{stu1.name} studying in {stu1.college} has {stu1.gpa} cgpa.")

# # class attributes can also be accessed with class name
# print(f"{stu2.name} studying in {Student.college} has {stu2.gpa} cgpa.") 



#                                       Lec -07 - Instance Method
#                                       Lec -08 - class Method
#                                       Lec -09 - static Method

# class laptop:
#     storage_type = "ssd"    # Class attribute

#     def __init__(self,RAM,graphic_card): # Instance attribute (constructor)
#         self.RAM = RAM
#         self.graphic_card = graphic_card

#     def get_info(self):     # Instance method
#         print(f"Laptop has {self.RAM} RAM and Storage type is {self.storage_type} with {self.graphic_card} graphic card")
    
#     @classmethod            # class method
#     def get_storage_type(cls):
#         print(f"Storage type is {cls.storage_type}")
    
#     @staticmethod           # static method
#     def cal_discount(price,discount):
#         final_answer = price - (price * discount / 100)
#         print(f"final price is {final_answer}")

# l1 = laptop("16 GB","NVIDIA")

# l1.get_info()
# laptop.get_storage_type()

# # When multipel digit number pass as parameter to class. if number should divide by _ (underscore) Python automatic convert it 40_000 => 40000
# l1.cal_discount(40_000, 5)



#                                       Lec -10 - Practice Problem

# Q- Design & create an online store for products(name,price). 
# Track total products being created
# Create a static method to calculate discount on each product based on a % parameter

# class Products:
#     count = 0

#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         Products.count += 1     # To access class attribut in instance attribute or constructor to use ClassName.classObject

#     def get_info(self):         # Instance method
#         print(f"price of {self.name} is {self.price} rupepee")
    
#     @classmethod
#     def get_count(cls):
#         print(f"total products in store = {cls.count}")
    
#     @staticmethod
#     def cal_discount(price,discount):
#         dis = price - (price * discount / 100)
#         print(f"final price after discount {dis}")

# p1 = Products("phone", 10_000)
# p2 = Products("laptop", 50_000)
# p3 = Products("pen", 10)

# p1.get_info()
# Products.get_count()
# p1.cal_discount(p1.price, 12)



#                                       Lec -11 - Encapsulation in OOP's


# class BankAccount:
#     def __init__(self, name, balance, acc_num):
#         self.name = name                    # Public Attribute
#         self._balance = balance             # Protected Attribute
#         self.__acc_num = acc_num            # Private Attribute
    
#     def get_acc_num(self):                  # getter
#         return self.__acc_num
    
#     def set_acc_num(self,new_acc_num):      # setter
#         self.__acc_num = new_acc_num


# acc1 = BankAccount("Rahul",100_000,111)

# print(f"{acc1.name} in your account total balance {acc1._balance}") # by convention protected attribute not access outside the class

# acc1.set_acc_num(121)

# print(f"{acc1.name} is your new account number is {acc1._BankAccount__acc_num}")    # by convention private attribute not access outside the class




#                                       Lec -12 - Inheritance In OOP's

# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

# class Teacher(Employee):
#     def __init__(self,subject):
#         self.subject = subject

# class AdminStaff(Employee):
#     def __init__(self,role):
#         self.role = role

# t1 = Teacher("Python")
# ads = AdminStaff("mananger")

# print(f"subject is {t1.subject} and start time '{t1.start_time}' and end time '{t1.end_time}' ")
# print(f"your role is {ads.role} and start time '{t1.start_time}' and end time '{t1.end_time}'")


#                                       Lec -13 - Types of Inheritance

#                                       Single Inheritance                  Employee -> Teacher
#                                       Multilevel Inheritance              Employee -> AdminStaff -> Account

# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

# class AdminStaff(Employee):
#     def __init__(self,role):
#         self.role = role

# class Account(AdminStaff):
#     def __init__(self,salary, role):
#         super().__init__(role)
#         self.salary = salary


# acc1 = Account(46_000,"Software Developer")

# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)


#                                       Multiple Inheritance              

#                                           Teacher     Student
#                                            \               /
#                                             \             /
#                                              \           /
#                                               \         /
#                                                \       /
#                                                 \     /
#                                                  \   /
#                                                   \ /
#                                                    |
#                                                   TA

# class Teacher:
#     def __init__(self, salary):
#         self.salary = salary

# class Student:
#     def __init__(self,gpa):
#         self.gpa = gpa

# class TA(Teacher,Student):
#     def __init__(self,salary,gpa,name):
#         super().__init__(salary)
#         Student.__init__(self,gpa)
#         self.name = name

# ta1 = TA(45000, 8.2, "Sourabh")

# print(ta1.name, ta1.salary, ta1.gpa)



#                                       Lec -14 - Absctraction

# from abc import ABC, abstractmethod

# class Animal(ABC):      # Absctractoin based class
#     def make_sound(self):
#         pass

# class Lion(Animal):
#     def make_sound(self):
#         print("Roar")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")

# lion = Lion()
# cat = Cat()

# lion.make_sound()
# cat.make_sound()


                                    # ✅ Why Abstract Classes Are Needed — Benefits
                                    # 1. Enforces required methods

                                    # Forces every subclass to implement specific methods.

                                    # Prevents “oh shit, I forgot to define that method” bugs.

                                    # 2. Catches errors early (before runtime)

                                    # Without abstraction, missing methods crash your program only when executed.

                                    # With abstraction, Python blocks class creation itself if required methods aren’t implemented.

                                    # 3. Defines a clear contract

                                    # Abstract class = rulebook

                                    # Subclasses = must follow the rulebook

                                    # Everyone knows what methods must exist.

                                    # 4. Supports clean polymorphism

                                    # You can treat different subclasses the same way.

                                    # Example: loop through animals and call .make_sound() without checking their type.

                                    # 5. Improves code structure in large projects

                                    # When you have dozens of subclasses, abstraction prevents inconsistent method names.

                                    # Keeps architecture predictable and readable.

                                    # 6. Prevents direct instantiation of “base” class

                                    # You don’t want objects of a generic class like Animal, Shape, PaymentMethod.

                                    # Abstract class blocks accidental creation of incomplete objects.

                                    # ❌ Drawbacks of Abstract Classes
                                    # 1. More boilerplate

                                    # Requires decorators (@abstractmethod) and ABC imports.

                                    # Slightly more code than normal classes.

                                    # 2. Reduces flexibility

                                    # Forces every subclass to implement the method, even when some subclasses don’t need it.

                                    # If you design the abstraction wrong, subclasses feel forced.

                                    # 3. Overengineering risk

                                    # Beginners use abstract classes where they DON'T make sense.

                                    # Example: using ABC for Teacher–Student–TA (your earlier example) is pointless.

                                    # 4. Harder to refactor later

                                    # If you modify an abstract method’s signature,

                                    # every subclass must be updated → ripple effect.

                                    # 5. Can lead to deep inheritance chains

                                    # Too many abstract base classes → messy hierarchy → harder to understand.

                                    # 6. Python already allows duck typing

                                    # Python doesn’t require abstract classes unlike Java, C#.

                                    # Sometimes ABC adds unnecessary rigidity to a language designed to be flexible.

                                    # 🎯 Simple Mental Model

                                    # Abstract class = rules you must follow.
                                    # Normal class = do whatever you want.

                                    # Use ABC only when you want enforcement, not just organization.


#                                       Lec -15 - Polymorphism (Function Overridding)

# class Animal():
#     def sound(self):
#         print("some generic sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark sound")

# d = Dog()
# d.sound()

# a = Animal()
# a.sound()



#                                       Lec -15 - Polymorphism ( Duck Typing)

class Dog:
    def speak(self):
        print("Dog")

class Cat:
    def speak(self):
        print("Cat")

class Robot:
    def speak(self):
        print("Robot")

def make_it_speak(entity):
    entity.speak()          # Doesn't care about type


d = Dog()
# d.speak()

c = Cat()
# c.speak()

r = Robot()
# r.speak()

for i in (d,c,r):
    make_it_speak(i)