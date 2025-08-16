from stats import count_words, count_characters, dict_to_sorted_list
import sys

def get_book_text(file_path):
    return open(file_path)


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)
        
    with get_book_text(sys.argv[1]) as f:
        text=f.read()
        print(text)
        count_words(text)
        dict_to_sorted_list(count_characters(text))


main()
