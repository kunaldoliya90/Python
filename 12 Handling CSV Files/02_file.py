# 12.2 Write a python program to create, write and read CSV files Into a
# Dictionary.

import csv

def write_csv_file(file_name, data):
    try:
        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in data:
                writer.writerow(row)

        print(f"CSV file '{file_name}' created successfully")

    except IOError:
        print("Error writing to CSV file")

def read_csv_file(file_name):
    try:
        with open(file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)

    except IOError:
        print("Error reading CSV file")

# Test the functions
file_name = "12 Handling CSV Files\\test2.csv"
data = [
    {"Name": "Kunal", "Age": 20, "City": "Indore"},
    {"Name": "Aditya Thakur", "Age": 22, "City": "New Delhi"},
    {"Name": "Atisha", "Age": 21, "City": "Bhopal"}
]

# Write data to CSV file
write_csv_file(file_name, data)

# Read data from CSV file
read_csv_file(file_name)
