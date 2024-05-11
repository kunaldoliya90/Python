# 11.5 Write a python program to count the frequency of words in a file.
from collections import Counter
import re

def count_word_frequency(file_name):
    try:
        # Open the file and read its content
        with open(file_name, 'r') as file:
            text = file.read().lower()  # Convert text to lowercase for case-insensitive comparison

        # Tokenize the text into words
        words = re.findall(r'\b\w+\b', text)

        # Count the frequency of each word
        word_counts = Counter(words)

        # Print the word frequency
        print("Word frequency in", file_name, ":")
        for word, count in word_counts.items():
            print(f"{word}: {count} occurrences")

    except FileNotFoundError:
        print("File not found")

# Test the function
file_name = "11 Handling files\sample2.txt"  # Change to your file name
count_word_frequency(file_name)
