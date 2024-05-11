def count_word_occurrences(string):
    words = string.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

string = input("Enter a string: ")
word_occurrences = count_word_occurrences(string)

print("Occurrences of each word:")
for word, count in word_occurrences.items():
    print(f"'{word}': {count}")
