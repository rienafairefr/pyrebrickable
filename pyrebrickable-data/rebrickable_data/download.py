import os

import requests

from rebrickable_data.utils import data_dir, data_files

url_format = 'https://m.rebrickable.com/media/downloads/%s.csv'


def download_data_files():
    for data_file in data_files:
        csv_path = os.path.join(data_dir, data_file + '.csv')
        url = url_format % data_file
        if not os.path.exists(csv_path):
            response = requests.get(url)
            if response.ok:
                with open(csv_path, 'wb') as csv_file:
                    csv_file.write(response.content)
                print('OK, downloaded %s' % data_file)
            else:
                print('could not get remote data at %s' % url)


if __name__ == '__main__':
    download_data_files()
