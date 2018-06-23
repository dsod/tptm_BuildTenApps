import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')

def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry, can't search the path.")
        return

    word = get_search_word_from_user()
    if not word:
        print("Can't search for nothing.")
        return

    matches = search_folder(folder, word)
    for v in matches:
        print('----------- MATCH ------------')
        print('file:  {}'.format(v.file))
        print('line:  {}'.format(v.line))
        print('match:  {}'.format(v.text.strip()))
        print()



def print_header():
    print('---------------------------------')
    print('       File Searcher App')
    print('---------------------------------')


def get_folder_from_user():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None
    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_word_from_user():
    word = input("What word do you want to search for? ")
    return word.lower()


def search_folder(folder, word):
    items = os.listdir(folder)
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folder(full_item, word)
        elif not item.startswith('.'):
            yield from search_file(full_item, word)


def search_file(filename, search_text):
    try:
        #print('Trying to search in {}'.format(filename))
        with open(filename, 'r', encoding='utf-8') as fin:
            line_num = 0
            for line in fin:
                line_num += 1
                if line.lower().find(search_text) >= 0:
                    m = SearchResult(line=line_num, file=filename, text=line)
                    yield m
    except (PermissionError, UnicodeDecodeError):
        pass


if __name__ == '__main__':
    main()
