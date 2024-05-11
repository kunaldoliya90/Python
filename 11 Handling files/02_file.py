# Write python program to find the most frequent words in a text read
# from a file

from collections import Counter
import re

def find_most_frequent_words(file_name, num_words):
    try:
        # Read text from the file
        with open(file_name, 'r') as file:
            text = file.read().lower()  # Convert text to lowercase for case-insensitive comparison

        # Tokenize the text into words
        words = re.findall(r'\b\w+\b', text)

        # Count the frequency of each word
        word_counts = Counter(words)

        # Find the most frequent words
        most_common_words = word_counts.most_common(num_words)

        # Display the most frequent words
        print(f"The {num_words} most frequent words in '{file_name}' are:")
        for word, count in most_common_words:
            print(f"{word}: {count} occurrences")

    except FileNotFoundError:
        print("File not found")

# Test the function
file_name = "11 Handling files\sample.txt"
num_words = 5
find_most_frequent_words(file_name, num_words)
