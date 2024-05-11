# 9.6 Write a python program to demonstrate inheritance
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

# Child class inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Child class inheriting from Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Child class inheriting from Animal
class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

# Create instances of different animals
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")

# Display information and make sounds
print(f"{dog.name} says: {dog.make_sound()}")
print(f"{cat.name} says: {cat.make_sound()}")
print(f"{bird.name} says: {bird.make_sound()}")
