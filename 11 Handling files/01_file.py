# Write a python code to perform following operations with a text file:
# i) create ii) open iii) read iv) write v) append vi) close vii) delete


# Create a text file
def create_file(file_name):
    try:
        with open(file_name, 'x'):
            print("File created successfully")
    except FileExistsError:
        print("File already exists")

# Open a text file for reading
def open_file_for_reading(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError:
        print("File not found")

# Read a text file
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError:
        print("File not found")

# Write to a text file
def write_to_file(file_name, text):
    try:
        with open(file_name, 'w') as file:
            file.write(text)
            print("Data written to file successfully")
    except FileNotFoundError:
        print("File not found")

# Append to a text file
def append_to_file(file_name, text):
    try:
        with open(file_name, 'a') as file:
            file.write(text)
            print("Data appended to file successfully")
    except FileNotFoundError:
        print("File not found")

# Close a text file
def close_file(file_name):
    try:
        file = open(file_name, 'r')
        file.close()
        print("File closed successfully")
    except FileNotFoundError:
        print("File not found")

# Delete a text file
def delete_file(file_name):
    import os
    try:
        os.remove(file_name)
        print("File deleted successfully")
    except FileNotFoundError:
        print("File not found")

# Test the functions
file_name = "sample.txt"
create_file(file_name)
write_to_file(file_name, "Hello, World!\n")
append_to_file(file_name, "This is a new line.")
open_file_for_reading(file_name)
delete_file(file_name)
