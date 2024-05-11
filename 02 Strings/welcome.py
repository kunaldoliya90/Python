def is_valid_name(name):
    # Check if the name contains only alphabetic characters and spaces
    return name.replace(' ', '').isalpha()

data = input("Enter your name: ")

if is_valid_name(data):
    print("Welcome,", data + "!")
else:
    print("Invalid input. Please enter a valid name.")
