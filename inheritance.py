"""Inheritance allows a class (child class) to inherit properties and methods from another class (parent class).
This helps in code reuse and building hierarchies."""
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):  # Inheriting from Animal
    def speak(self):
        print(f"{self.name} barks.")

# Another child class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  
cat.speak()  
