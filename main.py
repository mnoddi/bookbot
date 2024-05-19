import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main() -> int:
    book_path = "./books/frankenstein.txt"
    book_content = get_book_text(book_path)
    print(book_content)
    return 0

if __name__ == '__main__':
    sys.exit(main())