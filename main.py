def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    from stats import words_in_book
    words_in_book(get_book_text("books/frankenstein.txt"))
    from stats import character_occ
    charcount = character_occ(get_book_text("books/frankenstein.txt"))
    print(charcount)



main()