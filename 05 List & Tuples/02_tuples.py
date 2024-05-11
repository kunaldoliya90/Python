# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Add items to a tuple by concatenating tuples
new_tuple = my_tuple + (6, 7)
print("Tuple after adding items:", new_tuple)

# Get the length of the tuple using len()
print("Length of the tuple:", len(new_tuple))

# Check if an item exists in the tuple
item_to_check = 3
if item_to_check in new_tuple:
    print(f"{item_to_check} exists in the tuple")
else:
    print(f"{item_to_check} does not exist in the tuple")

# Access items in the tuple using indexing
index_to_access = 2
print("Item at index", index_to_access, ":", new_tuple[index_to_access])
