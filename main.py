def main():
    path_to_file = 'books/frankenstein.txt'
    with open(path_to_file) as f:
        book_text = f.read()
        print('----- Begin report of ' + path_to_file + ' -----')
        words_in_book(book_text)
        count_characters(book_text)
        print('----- End Report -----')

def words_in_book(text):
    words = text.split()
    print('There are ' + str(len(words)) + ' words in this document')

def count_characters(text):
    character_dict = {}
    for x in text.lower():
        if x in character_dict.keys():
            character_dict.update({x:character_dict[x] + 1})
        else:
            character_dict.update({x:1})
    for x in character_dict:
        if x.isalpha():
            print('The ' + x + ' character was found ' + str(character_dict[x]) + ' times')

if __name__ == '__main__':
    main()