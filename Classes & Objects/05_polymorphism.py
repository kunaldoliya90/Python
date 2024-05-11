# 9.5 Write a python program to apply polymorphism.

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Bird(Animal):
    def sound(self):
        return "Chirp!"

# Function to make animal sounds
def make_sound(animal):
    print(animal.sound())

# Create instances of different animals
dog = Dog()
cat = Cat()
bird = Bird()

# Make animal sounds
make_sound(dog)
make_sound(cat)
make_sound(bird)
