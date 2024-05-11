# 9.7 Write a python program for method overriding. 
# Parent class
class Animal:
    def sound(self):
        return "Generic sound"

# Child class inheriting from Animal
class Dog(Animal):
    def sound(self):
        return "Woof!"

# Child class inheriting from Animal
class Cat(Animal):
    def sound(self):
        return "Meow!"

# Child class inheriting from Animal
class Bird(Animal):
    def sound(self):
        return "Chirp!"

# Create instances of different animals
dog = Dog()
cat = Cat()
bird = Bird()

# Display the sounds made by each animal
print("Dog says:", dog.sound())
print("Cat says:", cat.sound())
print("Bird says:", bird.sound())
