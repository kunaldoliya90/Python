# Create an empty list
my_list = []

# Insert elements into the list using insert()
my_list.insert(0, 'apple')  # Insert 'apple' at index 0
my_list.insert(1, 'banana') # Insert 'banana' at index 1
my_list.insert(2, 'orange') # Insert 'orange' at index 2
print("List after insertions:", my_list)

# Remove an element from the list using remove()
my_list.remove('banana') # Remove 'banana' from the list
print("List after removal:", my_list)

# Append elements to the list using append()
my_list.append('grape')  # Append 'grape' to the end of the list
my_list.append('kiwi')   # Append 'kiwi' to the end of the list
print("List after append:", my_list)

# Get the length of the list using len()
print("Length of the list:", len(my_list))

# Remove and return the last element from the list using pop()
last_element = my_list.pop()
print("Popped element:", last_element)
print("List after pop:", my_list)

# Clear the list using clear()
my_list.clear()
print("List after clear:", my_list)
