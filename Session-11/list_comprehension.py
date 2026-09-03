#List Comprehension, Dictionary Comprehension and Loops

# Convert each Kannada food name into uppercase
foods = ["bisi bele bath", "mysore pak", "neer dosa", "ragi mudde", "akki rotti"]
uppercase_foods = [food.upper() for food in foods]
print(uppercase_foods)

# Calculate the total price of all items using a for loop
items = {"rice": 50, "dal": 30, "sugar": 40, "salt": 20, "oil": 60}
total = 0
for price in items.values():
    total += price
print("Total price of items:", total)

# Create a list of squares from 1 to 10 using list comprehension
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [n**2 for n in num]
print("Squares of numbers:", squares)

#Student Data Task
students = [
    {
        "Name": "John",
        "Age": 20,
        "marks": 85
    },
    {
        "Name": "Alice",
        "Age": 22,
        "marks": 90
    },
    {
        "Name": "Bob",
        "Age": 21,
        "marks": 75
    }
]
for student in students:
    print(f"Name: {student['Name']}, Age: {student['Age']}, Marks: {student['marks']}")

#Dictionary Comprehension
#Filter cities whose population is 10 lakhs or more
cities = {
    "Bangalore": 130,
    "Mysore": 10,
    "Hubli": 9,
    "Belgaum": 6,
    "Mangalore":6
    }
large_cities = {city: population for city, population in cities.items() if population >= 10}
print(large_cities)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    print(row)
    print("Sum of row:", sum(row))
