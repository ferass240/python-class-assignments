from turtledemo.penrose import makeshapes
############ Exercise 1 ################
"""
Exercise 1: Basic Class Definition
Task:
Create a class Car with the following attributes:
make (string)
model (string)
year (integer)
Add a method display_info() that prints the car's details in a formatted string.
Create an instance of the Car class and call display_info().
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This Car is a {self.year} {self.model} which was manufactured in {self.make} ")



car1= Car("Italy", "Ferrari spider", "2005")
car2 = Car("Germany", "Porsche GTR", "2010")


car1.display_info()
############ Exercise 2 ################
"""
Exercise 2: Class with Constructor and Method
Task:
Create a class Rectangle with attributes width and height.
Add a method area() that returns the area of the rectangle.
Add a method perimeter() that returns the perimeter of the rectangle.
Create an instance of the Rectangle class and print its area and perimeter.
"""


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width


    def area(self):
        #print(f"The area of the rectangle is :\n {self.width * self.height}")
        return self.width * self.height

    def perimeter(self):
        #print(f"The perimeter of the rectangle is :\n {2* self.width+ 2* self.height}")
        return 2*self.width + 2*self.height

rect = Rectangle(10,5)
a = rect.area()
print(f"Area: {a}")

p = rect.perimeter()
print(f"Perimeter: {p}")


############ Exercise 3 ################
"""
Exercise 3: Class with Default Values
Task:
Create a class Book with attributes title, author, and pages (default value of 0).
Add a method display_info() that prints the book's details.
Create instances of Book with and without specifying the pages attribute.
"""
class Book:

    def __init__(self,title, author, pages = 0):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):

        print(f"Title: {self.title}, Author:{self.author}, Pages: {self.pages}")


book1 = Book("The Great Gatsby","F.Scott Fitzgerald",180)
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book1.display_info()
book2.display_info()


############ Exercise 4 ################
"""
Exercise 4: Class with Multiple Methods
Task:
Create a class BankAccount with attributes account_number, holder_name, and balance.
Add methods:
deposit(amount): Increases the balance by amount.
withdraw(amount): Decreases the balance by amount if sufficient funds are available.
display_balance(): Prints the current balance.
Create an instance of BankAccount and test all methods.
"""


class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print( f"\n Your current balance is: {self.balance}")
        pass

account = BankAccount("123456","Feras",500)
account.deposit(200)
account.display_balance()
account.withdraw(100)
account.display_balance()

############ Exercise 5 #################
"""
Exercise 5: Class with Inheritance
Task:
Create a base class Person with attributes name and age.
Add a method display_info() that prints the person's details.
Create a derived class Student that inherits from Person and adds an attribute student_id.
Override display_info() in Student to include the student_id.
Create an instance of Student and call display_info().
"""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        if self.gender == "male":
            print(f"This person's name is: {self.name} and he is {self.age} years old!")
        else:
            print(f"This person's name is {self.name} and she is {self.age} years old!")


per1 = Person("Feras", 29, "male")

per1.display_info()


class Student(Person):
    def __init__(self, student_id, name, age, gender):
        Person.__init__(self, name,age, gender)
        self.student_id = student_id

    def display_info(self):

        if self.gender == "male":
            print(f"The student with id number {self.student_id}  is {self.name} and he is {self.age} years old!")
        else:
            print(f"The student with id number {self.student_id} is {self.name} and she is {self.age} years old!")

stud1 = Student("1235", "Feras", "29", "male")
stud1.display_info()


############ Exercise 6 ################
"""
Exercise 6: Private Attributes and Methods
Task:
Create a class SecureAccount with attributes account_number and balance.
Make balance a private attribute.
Add methods:
deposit(amount): Increases the balance.
withdraw(amount): Decreases the balance if sufficient funds are available.
_display_balance(): Prints the current balance (private method).
Create an instance of SecureAccount and test the methods.
"""

class SecureAccount:

    def __init__(self, account_number, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def __display_balance(self):
        print(f"The Current balance is: {self.__balance}")

secure_account = SecureAccount("123", 1000)
secure_account.deposit(500)
secure_account.__display_balance()
secure_account.withdraw(200)
secure_account.__display_balance()
