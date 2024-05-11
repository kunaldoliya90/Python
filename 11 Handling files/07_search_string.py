# 11.7 Write a python program to search for a string in text file
def search_string_in_file(file_name, search_string):
    try:
        # Open the file for reading
        with open(file_name, 'r') as file:
            # Read each line in the file
            for line_number, line in enumerate(file, start=1):
                # Check if the search string is found in the line
                if search_string in line:
                    print(f"Found '{search_string}' in '{file_name}' at line {line_number}:")
                    print(line)

    except FileNotFoundError:
        print("File not found")

# Test the function
file_name = "11 Handling files\sample.txt"  # Change to your file name
search_string = "Kunal"   # Change to the string you want to search for
search_string_in_file(file_name, search_string)
