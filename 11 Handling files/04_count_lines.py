def count_lines(file_name):
    try:
        # Open the file
        with open(file_name, 'r') as file:
            # Count the lines
            line_count = sum(1 for line in file)
        print(f"Number of lines in '{file_name}':", line_count)
    except FileNotFoundError:
        print("File not found")

# Test the function
file_name = "11 Handling files\sample2.txt"  # Change to your file name
count_lines(file_name)
