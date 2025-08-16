import os
from stats import count_words, count_characters, dict_to_sorted_list
import sys

def get_book_text(file_path):
    return open(file_path)


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return

    with get_book_text(file_path) as f:
        text=f.read()
        count_words(text)
        dict_to_sorted_list(count_characters(text))


main()
