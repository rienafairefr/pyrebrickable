import click

from rebrickable.data.database import reset_db_main
from rebrickable.data.download import download_main
from rebrickable.data.download_extra import download_extra_main
from rebrickable.data.importing import import_main


@click.group(help='data commands')
def data():
    pass


data.add_command(download_main)
data.add_command(import_main)
data.add_command(reset_db_main)
data.add_command(download_extra_main)
