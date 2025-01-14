from turtledemo.penrose import makeshapes


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

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width


    def area(self):
        print(f"The area is {self.width}*{self.height}")
