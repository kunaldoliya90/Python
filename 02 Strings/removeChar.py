def remove_odd_index_chars(s):
    return ''.join([s[i] for i in range(len(s)) if i % 2 == 0])

# Input string from the user
string = input("Enter a string: ")

# Removing characters with odd index values
result = remove_odd_index_chars(string)

# Printing the result
print("String with characters at odd index removed:", result)
