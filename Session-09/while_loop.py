# WHILE LOOP

# Printing numbers from 1 to 10
x = 1
while x <= 10:
    print(x)
    x += 1
 
# Printing odd numbers from 1 to 20     
x = 1
while x <= 20:
    if x % 2 == 1:
        print(x)
    x += 1

# Ticket booking simulation
seats = 8
while seats > 0:
    print("seats booked")
    seats -= 1
print("all seats are booked")   

# Countdown timer
x = 10
while x > 0:
    print(x)
    time.sleep(1)
    x -= 1
print("Happy new year!")    
