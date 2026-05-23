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

class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving")


car = Car()
car.drive()

class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price


p = Product(500)
print(p.price)

class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Point(self.x + other.x)


p1 = Point(5)
p2 = Point(10)

result = p1 + p2
print(result.x)

class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher


t1 = Teacher("Mr. Khan")
s1 = Student("Ali", t1)

print(f"{s1.name} is taught by {s1.teacher.name}")

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"


book = Book("Python Basics")
print(book)

class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, amount):
        self.__salary = amount

    def get_salary(self):
        return self.__salary


emp = Employee()
emp.set_salary(50000)

print(emp.get_salary())

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


u1 = User("Ali", 22)

print(u1.name, u1.age)

class Lion:
    def sound(self):
        return "Roar"


class Goat:
    def sound(self):
        return "Mehh"


animals = [Lion(), Goat()]

for animal in animals:
    print(animal.sound())
    
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class CreditCard(Payment):

    def pay(self):
        print("Payment via Credit Card")


c = CreditCard()
c.pay()

class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

s = Student("Ahmed")
s.show()

# vehicle porject
class Vehicle:
    def start(self):
        print("Vehicle started")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


b = Bike()
b.start()
b.ride()

class GrandParent:
    pass


class Parent(GrandParent):
    pass


class Child(Parent):
    pass


print(issubclass(Child, GrandParent))

class Logger:
    instances = 0

    def __init__(self):
        Logger.instances += 1


l1 = Logger()
l2 = Logger()

print(Logger.instances)

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()

print(s1 == s2)

class Bank:
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            print("Deposited:", amount)


b = Bank()
b.deposit(-100)

class CPU:
    def process(self):
        print("Processing...")


class Computer:
    def __init__(self):
        self.cpu = CPU()


pc = Computer()
pc.cpu.process()

class Number:
    def __init__(self, value):
        self.value = value

    def __len__(self):
        return self.value


n = Number(10)

print(len(n))

