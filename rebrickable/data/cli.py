import click

from .database import reset_db_main
from .download import download_main
from .importing import import_main
from .download_extra import download_extra_main


@click.group()
def main():
    pass


main.add_command(download_main)
main.add_command(import_main)
main.add_command(reset_db_main)
main.add_command(download_extra_main)

if __name__ == '__main__':
    main()
