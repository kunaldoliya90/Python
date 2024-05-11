import sys

def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program.py <text>")
        sys.exit(1)

    text = sys.argv[1]
    word_count = count_words(text)
    print("Number of words:", word_count)