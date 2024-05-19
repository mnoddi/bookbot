import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text) -> int:
    words = text.split()
    word_count = len(words)
    return word_count

def main() -> int:
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(f"Words: {word_count}")
    return 0

if __name__ == '__main__':
    sys.exit(main())