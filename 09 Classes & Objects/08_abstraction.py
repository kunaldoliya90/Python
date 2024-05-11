# 9.8 Write a python program to define abstraction.

from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

# Concrete subclass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Concrete subclass
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances of different animals
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Display information and make sounds
print(f"{dog.name} says: {dog.make_sound()}")
print(f"{cat.name} says: {cat.make_sound()}")
