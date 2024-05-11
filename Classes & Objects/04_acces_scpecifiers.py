# 9.4 Write a python program to demonstrate access specifiers. 

class MyClass:
    def __init__(self):
        self.public_attribute = "I am a public attribute"
        self._protected_attribute = "I am a protected attribute"
        self.__private_attribute = "I am a private attribute"

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")


# Create an object of MyClass
obj = MyClass()

# Access public attribute and call public method
print(obj.public_attribute)
obj.public_method()
print()

# Access protected attribute and call protected method (not recommended)
print(obj._protected_attribute)
obj._protected_method()
print()

# Accessing private attributes and methods will raise AttributeError
# print(obj.__private_attribute)
# obj.__private_method()
