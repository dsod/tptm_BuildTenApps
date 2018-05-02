import shutil
from pathlib import Path

import requests


def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw


def save_image(folder, name, data):
    suffix = '.jpg'
    filename = Path(folder / name).with_suffix(suffix)
    with open(filename, 'wb') as fout:
        shutil.copyfileobj(data, fout)
