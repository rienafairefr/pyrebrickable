import os

import click
import requests

from .utils import data_mapping, data_dir


url_format = 'https://m.rebrickable.com/media/downloads/%s.csv'


@click.command(name='download')
@click.option('--force', is_flag=True, help='force to overwrite existing file(s)')
def download_main(force=False):
    print('data directory %s' % data_dir)
    not_overwriting = False
    for data_file in data_mapping:
        csv_path = os.path.join(data_dir, data_file + '.csv')
        url = url_format % data_file
        if os.path.exists(csv_path) and not force:
            not_overwriting = True
            continue

        response = requests.get(url)
        if response.ok:
            with open(csv_path, 'wb') as csv_file:
                csv_file.write(response.content)
            print('OK, downloaded %s.csv' % data_file)
        else:
            print('could not get remote data at %s' % url)
    if not_overwriting:
        print('Not overwriting csv files, add --force if that''s what you want')
