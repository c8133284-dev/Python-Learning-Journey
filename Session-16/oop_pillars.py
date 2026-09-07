#OOP - Four Pillars

# 1. ENCAPSULATION
# Protecting data inside a class
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def check_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

account = BankAccount("12345", 5000)

account.check_balance()
account.deposit(1000)
account.withdraw(2000)
account.check_balance()


# 2. ABSTRACTION
# Hiding complicated internal details
class phone:
    def call_contact(self, name):
        print("calling", name)
    def take_picture(self):
        print("taking picture")
phone = phone()
phone.call_contact("John")
phone.take_picture()   


# 3. INHERITANCE
# Child class gets features from parent class
class vehicle:
    def start(self):
        print("Vehicle started")
class bike(vehicle):
    def ride(self):
        print("Bike is riding")
bike = bike()
bike.start()
bike.ride()                


# 4. POLYMORPHISM
# Same method name with different behavior
class shape:
    def calculate_area(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
shapes = [circle(5), rectangle(4, 6)]
for shape in shapes:
    print("Area:", shape.calculate_area())
