# 9.2 Write a python Program to call data member and function using classes
# and objects

class MyClass:
    def __init__(self, message):
        self.message = message
    
    def print_message(self):
        print("Message:", self.message)

# Create an object of MyClass
my_object = MyClass("Hello World")

# Access the data member and call the function using the object
print("Data member value:", my_object.message)
my_object.print_message()
