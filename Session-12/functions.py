#Functions, Parameters and Return

#Greet Function
def greet():
    print("Hello, welcome to our program!")

greet()
greet()

#Parameterized Greet
def greet(name):
    print(f"Hello, {name}! Welcome to our program!")

greet("John")
greet("Alice")

#Sum Function
def add_numbers(a, b):
    return a + b

result1 = add_numbers(5, 10)
result2 = add_numbers(3, 7)
print("Result 1:", result1)
print("Result 2:", result2)
