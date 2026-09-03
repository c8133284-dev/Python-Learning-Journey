# For Loops

# Multiples of 3 between 1 and 30
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

# Sum of first 10 numbers
total = 0
for i in range(1, 11):
    total = total + i
    print("sum=", total) 

# Print name letter by letter
name = input("Enter your name: ")
for letter in name:
    print(letter)
    
# Count vowels in a string
text = input("Enter your string: ")
count = 0
for letter in text:
    if letter.lower() in 'aeiou':
        count += 1
print("Number of vowels:", count)
