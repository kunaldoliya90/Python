# Write a python program to read first n lines of a file

def read_first_n_lines(file_name, n):
    try:
        # Open the file
        with open(file_name, 'r') as file:
            # Read the first n lines
            for i in range(n):
                line = file.readline().strip()  # Strip newline character
                if line:  # Check if line is not empty
                    print(line)
                else:  # Break if end of file is reached
                    break
    except FileNotFoundError:
        print("File not found")

# Test the function
file_name = "11 Handling files\sample.txt"  # Change to your file name
n = 5  # Number of lines to read
read_first_n_lines(file_name, n)
