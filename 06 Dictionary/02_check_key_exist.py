def key_exists(dictionary, key):
    return key in dictionary

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

key_to_check = "age"

if key_exists(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
