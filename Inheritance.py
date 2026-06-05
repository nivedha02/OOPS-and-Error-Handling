"""Problem 8 — Inheritance (medium)
Create a base class Animal with name and a method speak() that prints "...". 
Create two child classes Dog and Cat that override speak() — Dog prints "Woof!", Cat prints "Meow!".
"""
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print("Woof!")
class Cat(Animal):
    def speak(self):
        print("Meow!")

# Test cases
dog = Dog("Buddy")
cat = Cat("Whiskers")
deer=Animal("Bambi")
dog.speak()  # Should print "Woof!"
cat.speak()  # Should print "Meow!" 
deer.speak() # Should print "..."