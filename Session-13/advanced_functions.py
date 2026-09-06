#Lambda, Recursion and Variable-Length Arguments

#Lambda Function
multiply = lambda a, b: a * b
result = multiply(4, 5)
print("Multiplication Result:", result)

#Recursive Function
def sum_numbers(n):
    if n == 0:
        return 0
    else:   
        return n + sum_numbers(n - 1)
result = sum_numbers(5)
print("Sum=", result)  

#Variable-Length Arguments
def average(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
result = average(10, 20, 30, 40, 50)
print("Average:", result)
