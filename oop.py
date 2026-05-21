class Car:
    def start(self):
        print("Car started")

my_car = Car()
my_car.start()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")


s1 = Student("Ali", 20)
s1.info()