# 11.6 Write a python program to copy the contents of a file to another file.
def copy_file(source_file, destination_file):
    try:
        # Open the source file for reading
        with open(source_file, 'r') as source:
            # Read the content of the source file
            content = source.read()

        # Open the destination file for writing
        with open(destination_file, 'w') as destination:
            # Write the content to the destination file
            destination.write(content)

        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully")

    except FileNotFoundError:
        print("File not found")

# Test the function
source_file = "11 Handling files/sample.txt"  # Change to your source file name
destination_file = "11 Handling files\sample2.txt"  # Change to your destination file name
copy_file(source_file, destination_file)
