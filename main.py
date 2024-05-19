import sys, os

def get_book_content(path):
    with open(path) as f:
        return f.read(), os.path.basename(f.name)

def get_word_count(text) -> int:
    words = text.split()
    word_count = len(words)
    return word_count

def count_letters(text):
    counts_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in counts_dict:
                counts_dict[char] += 1
            else:
                counts_dict[char] = 1
    return counts_dict

def print_letter_count(letters):
    for letter in letters:
        print(f" * The letter '{letter}' appears {letters[letter]} times.")

def main() -> int:
    book_path = "./books/frankenstein.txt"
    book_text, file_name = get_book_content(book_path)
    word_count = get_word_count(book_text)
    letter_counts = count_letters(book_text)
    
    sorted_letters = dict(sorted(letter_counts.items(), key=lambda letter: letter[1], reverse=True))
    
    print(f"=== Report for {file_name} ===")
    print()
    print(f"Words: {word_count}")
    print()
    print_letter_count(sorted_letters)
    print()
    print("=== Report end ===")

    return 0

if __name__ == '__main__':
    sys.exit(main())