# Create a Movie class
class movie:

    # Constructor to initialize movie details
    def __init__(self,title, rating):
        self.title = title
        self.rating = rating

    # Method to display movie details  
    def display_info(self):
        print("movie title:", self.title)
        print("movie rating:", self.rating)

# Create movie objects
movie1 = movie("Inception", 8.8)
movie2 = movie("The Dark Knight", 9.0)

# Display movie details
movie1.display_info()
movie2.display_info()


# Create an Employee class
class employee:
    
    # Constructor with default salary
    def __init__(slf, name, designation, salary=30000):
        slf.name = name
        slf.designation = designation
        slf.salary = salary
    
    # Method to display employee details  
    def display_info(slf):
        print("Employee Name:", slf.name)
        print("Designation:", slf.designation)
        print("Salary:", slf.salary)
        print()
      
# Create employee objects      
employee1 = employee("John", "Manager", 5000)
employee2 = employee("Alice", "Developer")
employee3 = employee("Bob", "Designer", 3500)


# Display employee details
employee1.display_info()
employee2.display_info()
employee3.display_info() 
