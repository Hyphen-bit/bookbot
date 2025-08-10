import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def display_alph_chars(LISTODIC):
    for entry in LISTODIC:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")


def main():
    #get filepath from sys.argv list and feed into filepath if no argument supplied, report error message.
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        from stats import words_in_book
        num_words = words_in_book(get_book_text(filepath))
        from stats import character_occ
        charcount = character_occ(get_book_text(filepath))
        from stats import dict_lists
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        display_alph_chars(dict_lists(charcount))
        print("============= END ===============")
    


main()