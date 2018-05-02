import pathlib

import cat_service


def main():
    print_header()
    folder = get_or_create_output_folder()
    print('Found or created {}: '.format(folder))
    download_cats(folder)
    # display cats
    print('Hello from main')


def print_header():
    print('------------------------------------------')
    print('             CAT FACTORY')
    print('------------------------------------------')


def get_or_create_output_folder():
    base_folder = pathlib.Path(__file__)

    folder = 'cat_pictures'
    full_path = base_folder.parent / folder
    if not full_path.exists() or not full_path.is_dir():
        print('Creating new directory at {}'.format(full_path))
        pathlib.Path.mkdir(full_path)

    return full_path


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count+1):
        name = 'lolcat_{}'.format(i)
        cat_service.get_cat(folder, name)


if __name__ == '__main__':
    main()
