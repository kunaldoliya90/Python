# 12.1 Write a python code to read a csv file using pandas’ module and print
# the first and last five lines of a file.

import pandas as pd

def read_csv_file(file_name):
    try:
        # Read the CSV file
        df = pd.read_csv(file_name)

        # Print the first five lines
        print("First five lines of the file:")
        print(df.head())

        # Print the last five lines
        print("\nLast five lines of the file:")
        print(df.tail())

    except FileNotFoundError:
        print("File not found")

# Test the function
file_name = "12 Handling CSV Files\\test.csv"  # Change to your file name
read_csv_file(file_name)
