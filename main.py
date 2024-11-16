def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    letters_sorted = get_letters_sorted(num_letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in letters_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def sort_on(d):
    return d["num"]


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_letters(text):
    lowered_string = text.lower()
    letter_count = {}
    for letter in lowered_string:
        if letter.isalpha():
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
    return letter_count


def get_letters_sorted(num_chars_dict):
    sorted_list = []
    for i in num_chars_dict:
        sorted_list.append({"char": i, "num": num_chars_dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list  

main()
