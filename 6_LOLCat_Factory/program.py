import pathlib
import platform
import subprocess

import cat_service


def main():
    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)


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
    print('Contacting server to download the cats...')
    cat_count = 8
    for i in range(1, cat_count+1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)


def display_cats(folder):
    print('Displaying cars in OS Window.')
    if platform.system() == 'Dwarwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder.name])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't recognize which OS you are running.")


if __name__ == '__main__':
    main()
