#A Class is like an object constructor, or a "blueprint" for creating objects.
# class MyClass:
#   x = 5
  
  
  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)




class Person:
    # Constructor (called when object is created)
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    # Method to display info
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects
p1 = Person("Nirjala", 22)
p2 = Person("Ram", 25)

# Calling method using object
p1.greet()   
