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