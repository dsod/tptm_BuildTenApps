import os


def load(name):
    '''
    This method created and loads a new journal.

    :param name:  This is the base name of the hournal to load.
    :return:  A new journal data structure populated with the file data.
    '''
    data = []
    filename = get_full_patchname(name)
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            print('... loading journal from {} ...'.format(name))
            for entry in f.readlines():
                data.append(entry.rstrip())
            print('... loaded {} entries ...'.format(len(data)))
            return data
    else:
        print('... loaded journal file found ...')
        return data


def save(name, journal_data):
    filename = get_full_patchname(name)
    with open(filename, 'w', encoding='utf-8') as f:
        print('... saving to {} ...'.format(filename))
        for item in journal_data:
            f.write(item + '\n')
        print('... save complete...')


def add_entry(text, journal_data):
    journal_data.append(text)
    return journal_data


def get_full_patchname(name):
    filename = os.path.join('.', 'data', name + '.jrl')
    return filename