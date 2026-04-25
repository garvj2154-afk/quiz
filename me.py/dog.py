# # # class bank:
# # #     def createaccount(self,account_number,name,balance):
# # #         self.account_number=account_number
# # #         self.name=name
# # #         self.balance=balance
# # #         print("account created succesfully!!!!!!!!!!!")
# # #     def show_details(self):
# # #         print("account_number:",self.account_number)
# # #         print("Account holder:",self.name)
# # #         print("Balance:",self.balance)
# # #     def deposit(self,amount):
# # #         self.balance+=amount
# # #         print("amount deposit succesfully")
# # #         print("Updated Balance:",self.balance)
# # #     def withdraw(self,amount):
# # #         if amount<=self.balance:
# # #             self.balance-=amount
# # #             print("Amount withdraw succesfully")
# # #             print("Updated Balance:",self.balance)
# # #         else:
# # #             print("insufficient balance")
# # #     def show_balance(self):
# # #         print("current balance:",self.balance)




# # class Student:
# #     def define_student(self):
# #         print("Name:", self.name)
# #         print("Roll No:", self.roll_no)
# #         print("-------------------")


# # # Create first object
# # student1 = Student()
# # student1.name = "Rahul"
# # student1.roll_no = 101

# # # Create second object
# # student2 = Student()
# # student2.name = "Priya"
# # student2.roll_no = 102

# # # Print details
# # student1.define_student()
# # student2.define_student()
# # class Student:
# #     def student1(self, name, roll_number):
# #         self.name = name
# #         self.roll_number = roll_number

# #     def student2(self, name1, roll_number1):
# #         self.name1 = name1
# #         self.roll_number1 = roll_number1

# #         print("student1 details:")
# #         print("Name:", self.name)
# #         print("Roll no.:", self.roll_number)

# #         print("student2 details:")
# #         print("Name:", self.name1)
# #         print("Roll no.:", self.roll_number1)
# # s = Student()
 
# # class dog:
# #     def dog1(self,name,breed):
# #         self.name=name
# #         self.breed=breed
# #     def dog2(self,name1,breed1):
# #         self.name1=name1
# #         self.breed1=breed1
# #         print("Dog details")
# #         print("Name:",self.name)
# #         print("Breed:",self.breed)
# #         print("Dog2 details")
# #         print("Name:",self.name1)
# #         print("Breed:",self.breed1)
# # d=dog()
# # d.dog1("khyati_mam/didi","cutie")
# # d.dog2("Anshika_mam/didi","pookie🎀")
# # class book:
# #     def book1(self,title,author):
# #         self.title=title
# #         self.author=author
# #     def book2(self,title2,author2):
# #         self.author2=author2
# #         self.title2=title2
# #         print("Intoduction to Book1")
# #         print("Title:",self.title)
# #         print("Author:",self.author)
    
# #         print("Intoduction to Book2")
# #         print("Title:",self.title2)
# #         print("Author:",self.author2)
# # b=book()
# # b.book1("How to make people fool","Fool")
# # b.book2("How to get pro at any game","Garv pani puri wala")


# # class employee():
# #     def __init__(self,name,salary):
# #         self.name=name
# #         self.salary=salary
# #     def employee2(self,name2,salary2):
# #         self.name2=name2
# #         self.salary2=salary2
# #         print("Employee details")
# #         print("Name:",self.name)
# #         print("Salary:",self.salary)
# #         print("Name:",self.name2)
# #         print("Salary:",self.salary2)
# # e=employee()
# # e.employee1("Garv","10")
# # e.employee2("Jay","50")
# # if e.salary> e.salary2:
# #     print("Salary is Higher")
# # else:
# #     print("Salary is lower")
# # class person:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# # p1=person("Garv",0)
# # print("Name:",p1.name)
# # print("Age:",p1.age)
# # class rectangle():
# #     def __init__(self,length,breadth):
# #         self.length=length
# #         self.breadth=breadth
# #     def area(self):
# #         print("area:",self.length*self.breadth)
# #     def perimeter(self):
# #         print("perimeter:",2*(self.length+self.breadth))
# # r1=rectangle(20,35)
# # r1.area()
# # r1.perimeter()  
# # class Person():
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# #     def check_age(self):
# #         if self.age>=18:
# #             print(self.name,"You can vote")
# #         else:
# #             print(self.name,"You can't vote")
# # p1=Person("Garv",17)
# # p1.check_age()
# # class student():
# #     def __init__(self,name,m1,m2,m3):
# #         self.name=name
# #         self.m1=m1
# #         self.m2=m2
# #         self.m3=m3
# #     def result(self):
# #         total=self.m1+self.m2+self.m3
# #         average=total/3
# #         print("Name:",self.name)
# #         print("Total:",total)
# #         print("average:",average)
# # s1=student("Khyati",12,13,14)
# # s1.result(   )
# # class movie():
# #     def __init__(self,movie_name,movie_rating):
# #         self.movie_name=movie_name
# #         self.movie_rating=movie_rating
# #     def check_movie(self):
# #         if self.movie_rating>=4:
# #             print(self.movie_name,"hit")
# #         else:
# #             print(self.movie_name,"Flop")
# # m1=movie("Marvel's_spider brand new day",4)
# # m1.check_movie()
# class employee():
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def check_bonus(self):
#         if self.salary>=5000:
#             bonus=self.salary*0.10
#         else:
#             bonus=self.salary*0.05
#         final_salary=self.salary+bonus
#         print("Name:",self.name)
#         print("final_salary:",final_salary) 
# e1=employee("Garv",3000)
# e1.check_bonus()      
# class vehicle():
#     def __init__(self,brand):
#         self.brand=brand
#     def start(self):
#         print("Vehicle started")
# class car(vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model=model
#     def show_result(self):
#         print("brand:",self.brand)
#         print("model:",self.model)
# c1=car("PORSCHE",911)
# # c1.start()
# # c1.show_result()
# class person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class employee(person):
#     def __init__(self, name, age,salary):
#         super().__init__(name, age)
#         self.salary=salary
#     def show_result(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Salary:",self.salary)
# e=employee("Garv",17,20000000)
# e.show_result()
# class teacher():
#     def teach(self):
#         print("Teaching subject:")
# class maths_teacher(teacher):
#     def solve(self):
#         print("Solve maths problem")
# t=maths_teacher()
# t.teach()
# t.solve()
# class appliance():
#     def power_on(self):
#         print("Appliance on")
# class washing_machine(appliance):
#     def wash(self):
#         print("washing clothes")
# w=washing_machine()
# w.power_on()
# w.wash()
# class bus():
#     def __init__(self,bus_number,total_seat,book_seat):
#         self.bus_number=bus_number
#         self.total_seat=total_seat
#         self.book_seat=book_seat
#     def available_seats(self):
#         available=self.total_seat-self.book_seat
#         print("Bus number:",self.bus_number)
#         print("available seats:",available)
# b=bus(40040,20,10)
# # b.available_seats()
# salary=1000
# experience=10 
# if experience>=10: 
#     bonus=salary*0.20
#     total_salary=salary+bonus
#     print(total_salary)
# elif experience>=5:
#     bonus1=salary*0.10
#     total_salary1=salary+bonus1
#     print(total_salary1)
# else:
#     print("No bonus")
# weight=47
# height=5.8
# bmi=weight/height**2
# if bmi<=18.5:
#     print("Under weight")
# elif bmi<=25:
#     print("Normal weight")
# elif bmi<=30:
#     print("Overweight")
# else:
#     print("obese")
# for i in range(1,51):
#     if i%5==0:
#         continue
#     print(i)
# num=1
# for i in range(1,5):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()
# class bank_account():
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance
#     def deposit(self,amount):
#         self.amount=amount
#         self.balance+=amount
#         print("deposited:",amount)
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print("withdraw:",amount)
#         else:
#             print("Insufficient balance.")
#     def check_balance(self):
#         print("Current balance:",self.balance)
# b=bank_account("Khyati",400)
# b.withdraw(399)
# b.deposit(1)
# b.check_balance()
# from abc import ABC, abstractmethod

# class Course(ABC):

#     def _init_(self, course_name):
#         self.course_name = course_name

#     @abstractmethod
#     def get_duration(self):
#         pass

#     @abstractmethod
#     def get_fee(self):
#         pass


# class PythonCourse(Course):

#     def get_duration(self):
#         return "3 Months"

#     def get_fee(self):
#         return 15000


# class DataScienceCourse(Course):

#     def get_duration(self):
#         return "6 Months"

#     def get_fee(self):
#         return 40000


# p = PythonCourse("Python")
# d = DataScienceCourse("Data Science")

# print(p.course_name, "-", p.get_duration(), "-", p.get_fee())
# print(d.course_name, "-", d.get_duration(), "-", d.get_fee())
# class bank:
#     def interest(self):
#         print("bank interest")
# class sbi():
#     def interest(self):
#         print("SBI interest rate 6%")
# class HDFC():
#     def interest(self):
#         print("HDFC interest rate 7%")
# banks=[sbi(),HDFC()]
# for bank in banks:
#     bank.interest()
# import math
# class shape():
#     def area(self):
#           self=self
# class circle(shape):
#     def __init__(self,r):
#                 self.r=r
#     def area(self):
#                 print("Area of circle:",math.pi*self.r*self.r)
# class rectangle(shape):
#     def __init__(self,l,b):
#                 self.l=l
#                 self.b=b
#     def area(self):
#         print("Area of rectangle:",self.l*self.b)
# c=circle(56)
# r=rectangle(56,40)
# shapes=[c,r]
# for shape in shapes:
# #     shape.area()
# class employee():
#     def work(self):
#         print("Employee creates Taj mahal")
# class developer(employee):
#     def work(self):
#         print("Developer write code")
# class designer(employee):
#     def work(self):
#         print("Designer create design")
# emp=employee()
# dv=developer()
# ds=designer()
# emp.work()
# dv.work()
# ds.work()
# class book():
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         return self.pages+other.pages
# b1=book(400)
# b2=book(69)
# print("total pages:",b1+b2)
# class payment():
#     def pay(self):
#         print("Processing payment")
# class cashpayment(payment):
#     def pay(self):
#         print("Payment done by cash")
# class onlinepayment(payment):
#     def pay(self):
#         print("Payment done by online method")
# payments=[cashpayment(),onlinepayment()]
# for p in payments:
#     p.pay()
# class student():
#     def student(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("Student details")
#         print("Name:",self.name)
#         print("Marks:",self.marks)
# s1=student()
# s2=student()
# s1.student("Harsh  ita",800)
# s2.student("AUNTY G",800)
# if s1.marks>s2.marks:
#     s1.display()
# else:
#     s2.display()
#     print("SIKANDER")
# class person():
#     def person(self,name,age):
#         self.name=name
#         self.age=age
# class teacher(person):
#     def teacher(self,subject):
#         self.subject=subject
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Subject:",self.subject)
# t=teacher()
# t.person("ANSHIKa",889)
# t.teacher("PYTHON")
# t.display()
# class vehicle():
#     def start(self):
#         print("Vehicle started")
# class car(vehicle):
#     def start(self):
#         print("Car is started")
# v=vehicle()
# c=car()
# c.start()
# v.start()
# class student():
#     def __init__(self):
#         self.__marks=500
#     def set_marks(self,marks):
#         self.__marks=marks
#     def get_marks(self):
#         return self.__marks
# s=student()
# s.set_marks(50)
# print("marks:",s.get_marks())
# class bank_account():
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#         print("Deposited:",amount)
#     def withdraw(self,amount):
#         if amount<self.__balance:
#             self.__balance-=amount
#             print("Withdraw:",self.__balance)
#         else:
#             print("Insufficient balance")
#     def get_balance(self):
#         return self.__balance
# b=bank_account(5000)
# b.withdraw(0)
# b.deposit(9)
# print("Apke account mein 9 ruppes prapt hue:",b.get_balance())
# class Employee():
#     def __init__(self, salary):
#         self.__salary = salary

#     @property
#     def salary(self):
#         return self.__salary

#     @salary.setter
#     def salary(self, value):
#         if value > 0:
#             self.__salary = value
#         else:
#             print("Salary must be positive")


# emp = Employee(200)
# print( emp.salary)

# emp.salary = 30000
# print("Updated Salary:", emp.salary)

# emp.salary = -5000
# class product():
#     def __init__(self):
#         self.__price=0
#     def set_price(self,price):
#             if price>0:
#                 self.__price=price
#             else:
#                 print("Invalid Price")
#     def calculate(self):
#             return self.__price*0.18
#     def get_price(self):
#             return self.__price
#     def total(self):
#           gst=self.calculate()
#           return self.__price+gst
# p=product()
# p.set_price(700)
# p.total()
# print("Price:",p.get_price())
# print("GST:",p.calculate())
# print("Total price:",p.total())
# class mobile():
#     def __init__(self):
#         self.__battery=100
#     def charge(self,amount):
#         self.__battery+=amount
#         if self.__battery>100:
#             self.__battery=100
#     def use(self,amount):
#         if amount<self.__battery:
#             self.__battery-=amount
#         else:
#             print("NOT ENOUGH BATTERY")
#     def get_battery(self):
#         return self.__battery
# m=mobile()
# m.charge(90)
# m.use(45)
# print("Battery:",m.get_battery())
# class temeprature():
#     def __init__(self):
#         self.__celsius=0
#     def set_temperature(self,value):
#         if value>=-273:
#             self.__celsius=value
#         else:
#             print("Temperature below 0 degrees")
#     def fahrenheit(self):
#         return(self.__celsius*9/5)+32 
#     def get_temperature(self):
#         return self.__celsius
# t=temeprature()
# t.set_temperature(90)
# print("Celsius:",t.get_temperature())
# print("Faherneit:",t.fahrenheit())
n=5
# for i in range(1,n+1):
#     for j in range(1,6):
#         print(j,"*",end=" ")
#         n+=1
#     print()
# n=5
# for i in range(1,6):
#     for j in range(5-i):
#         print("*",end=(" "))
#     print()
# for i in range(1,10000):
#     name=("GARV PGL","SARE PGL")
#     print(name)
# f=open("hlo.txt",'w')
# for i in range(1,19):
#     f.write(str(i)+"\n")
# f.close()
# for i in range(1,21):
#     if i%2==0:
#         print(i,"  EVEN NUMBERS")
#     else:
#         print(i,"  ODD NUMBERS")
# total=0
# while True:
#     num=int(input("ENTER NUMBER"))
#     if num<=0:
#         break
    
#     else:
#         total+=num
# print("Total number:",total)
# num=[1,2,3,4,5]
# try:
#     index=int(input("ENTER INDEX:"))
#     print("element:",num[index])
# except IndexError:
#     print("ERROR: INVALID INDEX")
# except ValueError:
#     print("ERROR: Enter valid number please")
# try:
#     num1=int(input("ENTER A NUMBER1"))
#     num2=int(input("ENTER A NUMBER2"))
#     result=num1/num2
#     print(result)
# except ZeroDivisionError:
#     print("Not divisble by zero")
# except ValueError:
#     print("ENTER A VALID NUMBER")
# try:
#     num=int(input("ENTER A NUMBER:"))
#     print("square:",num**2)
# except ValueError:
#     print("Wrong input stupid take a number")
# finally:
#     print("Khel khatam")
class InvalidAgeError(Exception):
    pass
try:
    age=int(input("ENTER YOUR AGE:"))
    if age<18:
        raise InvalidAgeError("YOU MUST BE 18 TO VOTE")
    print("Guarranted")
except InvalidAgeError as e:
    print("error:",e)
except ValueError:
    print("ENTER YOUR TRUE AGE")
    
 



    
