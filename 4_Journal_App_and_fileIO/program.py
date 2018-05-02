import journal


def main():
    print_app_header()
    run_event_loop(journal)


def print_app_header():
    print('----------------------------')
    print('  PERSONAL JOURNAL APP')
    print('-----------------------------')


def list_entries(journal_data):
    if journal_data is not None:
        print('Your {} journal entries:'.format(len(journal_data)))
        entries = reversed(journal_data)
        for i, item in enumerate(entries):
            print('[{}]. {}'.format(i + 1, item))
    else:
        print('Journal is empty.')


def run_event_loop(file):
    action = 'Empty'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while action != 'x':
        action = input('What do you want to do? [L]ist, [A]dd, or E[x]it? ')
        action = action.lower().strip()

        if action == 'l':
            list_entries(journal_data)

        elif action == 'a':
            entry = input('Enter your journal entry: ')
            journal_data = journal.add_entry(entry, journal_data)

        elif action == 'x':
            journal.save(journal_name, journal_data)

        else:
            print()
            print('Invalid input...')
            print()

    print('Exiting loop.')


if __name__ == '__main__':
    main()