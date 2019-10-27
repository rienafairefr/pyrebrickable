# -*- coding: utf-8 -*-

"""Console script for pyrebrickable."""
from __future__ import print_function
import json
from collections import namedtuple
from getpass import getpass

import click
import yaml

from rebrickable.api import ApiClient, Configuration
from rebrickable.cli.data import data
from rebrickable.data.database import reset_db_main
from rebrickable.data.download import download_main
from rebrickable.data.download_extra import download_extra_main
from rebrickable.data.importing import import_main
from .common import State

from .lego import lego
from .user import user
from .users import users

try:
    from enum import Enum, EnumMeta  # pragma: no cover
except ImportError:  # pragma: no cover
    from enum34 import Enum, EnumMeta  # pragma: no cover

from rebrickable.cli.utils import get_data, DATA_PATH, EnumType, write_data


class OutputFormat(Enum):
    json = 0  # json.dumps
    yaml = 1  # yaml.dump
    py = 2  # print


OutputFormatter = namedtuple('OutputFormatter', ['output'])


def get_api_client():
    configuration = Configuration()
    data = get_data()
    api_key = data['api_key']
    configuration.api_key['Authorization'] = api_key
    configuration.api_key_prefix['Authorization'] = 'key'
    return ApiClient(configuration)


@click.group(help="Rebrickable CLI implemented in Python")
@click.pass_context
@click.option('--output', '-o', help='output printer (json, yaml, py --regular print Python function--)',type=EnumType(OutputFormat, casesensitive=False), default="py")
def main(click_context, output):
    """Console script for pyrebrickable."""

    format = None
    if output == OutputFormat.json:
        format = OutputFormatter(output=lambda o: print(json.dumps(o.to_dict(), default=str)))
    elif output == OutputFormat.yaml:
        format = OutputFormatter(output=lambda o: print(yaml.dump(o.to_dict(), default_flow_style=False)))
    elif output == OutputFormat.py:
        format = OutputFormatter(output=lambda o: print(o))

    try:
        click_context.obj = State(format=format, client=get_api_client())
    except (IOError, KeyError, ValueError):
        if click_context.invoked_subcommand != 'register':
            print('please register your API key using: \nrebrickable register')
            raise click.Abort()


def get_api_key():
    return getpass(prompt='Please enter your API key:')


@main.command(help='registers an API key with the CLI')
def register():
    key = get_api_key()
    data = get_data()
    data['api_key'] = key
    write_data(data)
    print('OK, registered API key in %s' % DATA_PATH)


main.add_command(lego)
main.add_command(data)
main.add_command(users)
main.add_command(user)

if __name__ == "__main__":
    main()
