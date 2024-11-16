def main():
    word_count = 0

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    
    words = file_contents.split()

    for word in words:
        word_count += 1

    print(word_count)

main()