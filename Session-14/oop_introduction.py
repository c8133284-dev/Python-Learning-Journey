# Create a Mobile class
class mobile:
    # Constructor to initialize brand and price
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
      
    # Method to display mobile details  
    def display_info(self):
        print(f"Brand: {self.brand}, Price: {self.price}")
# Create two objects      
mobile1 = mobile("Apple", 1000)
mobile2 = mobile("Samsung", 800)
# Display the details
mobile1.display_info()
mobile2.display_info()


#Create a Student class
class student:
    # Constructor to initialize name and marks 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
      
    # Method to display student information  
    def  display_info(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
      
# Create multiple student objects      
student1 = student("John", 85)
student2 = student("Alice", 92)
student3 = student("Bob", 78)

# Display information of each student
student1.display_info() 
student2.display_info()
student3.display_info()
