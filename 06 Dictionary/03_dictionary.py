def sort_dict_ascending(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: str(item[1])))

def sort_dict_descending(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: str(item[1]), reverse=True))

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "salary": 50000
}

sorted_dict_ascending = sort_dict_ascending(my_dict)
print("Dictionary sorted by values in ascending order:", sorted_dict_ascending)

sorted_dict_descending = sort_dict_descending(my_dict)
print("Dictionary sorted by values in descending order:", sorted_dict_descending)
