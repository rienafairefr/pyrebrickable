# -*- coding: utf-8 -*-

"""Console script for pyrebrickable."""
from getpass import getpass

import click
import os

import rebrickable
from rebrickable import LegoApi, ApiClient

pass_client = click.make_pass_decorator(ApiClient)
pass_legoapi = click.make_pass_decorator(LegoApi)

key_path = os.path.expanduser('~/.rebrickable')

@click.group(help="Rebrickable CLI implemented in Python")
@click.pass_context
def main(ctx, args=None):
    """Console script for pyrebrickable."""
    configuration = rebrickable.Configuration()
    
    try:
        with open(key_path, 'r') as key_file:
            api_key = key_file.read()
            configuration.api_key['Authorization'] = api_key
            configuration.api_key_prefix['Authorization'] = 'key'
            ctx.obj = rebrickable.ApiClient(configuration)
    except FileNotFoundError:
        if ctx.invoked_subcommand != 'register':
            print('key file %s does not exist, please register your API key using: \n%s register' % (key_path, rebrickable.__name__))
            raise click.Abort()


@main.command(help='registers an API key with the CLI')
def register():
    key = getpass(prompt='Please enter your API key:')
    with open(key_path, 'w') as key_file:
        print(key)
        key_file.write(key)
        print('OK, saved into %s'%key_path)



@main.group()
@pass_client
@click.pass_context
def lego(ctx, client):
    ctx.obj = rebrickable.LegoApi(client)


@lego.group()
def colors():
    pass


@colors.command()
@pass_legoapi
def list(api):
    print(api.lego_colors_list())


@colors.command()
@pass_legoapi
@click.argument('id', type=str)
def read(api, id):
    print(api.lego_colors_read(id))


@lego.group()
def elements():
    pass


@lego.group()
def mocs():
    pass


@click.group()
def parts():
    pass


@parts.command
def parts(set_num):
    pass


@mocs.command()
def read(set_num):
    pass


@click.group()
def part():
    pass


@click.group()
def categories():
    pass


@categories.command
def list():
    pass


@categories.command
def read(id):
    pass

# lego_parts_colors_list
# lego_parts_colors_list_with_http_info
# lego_parts_colors_read
# lego_parts_colors_read_with_http_info
# lego_parts_colors_sets_list
# lego_parts_colors_sets_list_with_http_info
# lego_parts_list
# lego_parts_list_with_http_info
# lego_parts_read
# lego_parts_read_with_http_info
# lego_sets_alternates_list
# lego_sets_alternates_list_with_http_info
# lego_sets_list
# lego_sets_list_with_http_info
# lego_sets_parts_list
# lego_sets_parts_list_with_http_info
# lego_sets_read
# lego_sets_read_with_http_info
# lego_sets_sets_list
# lego_sets_sets_list_with_http_info
# lego_themes_list
# lego_themes_list_with_http_info
# lego_themes_read
# lego_themes_read_with_http_info


@click.command()
def users():
    pass


if __name__ == "__main__":
    main()
