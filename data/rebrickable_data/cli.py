import click

from rebrickable_data.download import download_main
from rebrickable_data.importing import import_main


@click.group()
def main():
    pass


main.add_command(download_main)
main.add_command(import_main)

if __name__ == '__main__':
    main()
