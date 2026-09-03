# IF, ELIF AND ELSE

# Checking whether a number is positive, negative or zero
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# Checking voting eligibility based on age
age = 18
if age < 18:
    print("not eligible to vote")
elif age == 18:
    print("eligible to vote") 
else :
    print("eligible to vote") 
  
# Checking whether a number is even or odd
x = 10
if x%2 == 0:
    print("x is even")
else:
    print("x is odd")
  
# GRADE CALCULATOR
grade = int(input("Enter your grade: "))
if grade >= 90:
    print("A grade")
elif grade >= 75:
    print("B grade")
elif grade >= 60:
    print("C grade")    
elif grade >= 50:
    print("D grade")
elif grade < 40:
    print("F grade")
else:
    print("Invalid grade")  
  
# Checking bus pass price based on age
age = int(input("Enter your age: "))
if age < 5:
    print("bus pass is free")
elif age > 60:
    print("senior citizen discount ")
else:
    print("full price")         

# Checking meal time based on the given hour
Time = int(input("enter the time:"))
if Time == 8:
    print("time to breakfast")
elif Time == 13:
    print("time to lunch")
elif Time == 20:
    print("time to dinner")
else:
    print("not time to eat")  
