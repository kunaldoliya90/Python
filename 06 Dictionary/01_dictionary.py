# Create a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 1. Print the dictionary items
print("Dictionary items:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 2. Access items in the dictionary
print("\nAccessing items:")
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

# 3. Use get() method
print("\nUsing get() method:")
print("Age:", my_dict.get("age"))
print("Gender:", my_dict.get("gender", "Not specified"))  # Providing a default value

# 4. Change values in the dictionary
print("\nChanging values:")
my_dict["age"] = 35
my_dict["city"] = "Los Angeles"
print("Updated dictionary:", my_dict)

# 5. Use len() to get the length of the dictionary
print("\nLength of the dictionary:", len(my_dict))
