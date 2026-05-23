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

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(1000)
account.deposit(500)
account.show_balance()

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    pass


dog = Dog()
dog.sound()

class Bird:
    def fly(self):
        print("Bird can fly")


class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")


p = Penguin()
p.fly()

class Cat:
    def sound(self):
        print("Meow")


class Cow:
    def sound(self):
        print("Moo")


animals = [Cat(), Cow()]

for animal in animals:
    animal.sound()
    
    from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


sq = Square(4)
print("Area:", sq.area())

class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name


e1 = Employee("Ahmed")

print(e1.name)
print(Employee.company)


class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b


print(MathUtils.add(5, 3))

class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def total_people(cls):
        return cls.count


p1 = Person()
p2 = Person()

print(Person.total_people())

class Father:
    def skills(self):
        print("Gardening")


class Mother:
    def talents(self):
        print("Cooking")


class Child(Father, Mother):
    pass


c = Child()
c.skills()
c.talents()