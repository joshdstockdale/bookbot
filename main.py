def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    print_chars_report(chars_sorted_list)
    print("--- End report ---")


def get_num_words(str):
    words = str.split()
    return len(words)


def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(dict):
    list = []
    for key in dict:
        list.append({"char": key, "num": dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list


def print_chars_report(chars_list):
    for char in chars_list:
        c = char["char"]
        n = char["num"]
        print(f"The '{c}' character was found {n} times")


def get_chars_dict(str):
    chars = {}
    for s in str:
        lower = s.lower()
        if lower.isalpha():
            if lower not in chars:
                chars[lower] = 1
            else:
                chars[lower] += 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

