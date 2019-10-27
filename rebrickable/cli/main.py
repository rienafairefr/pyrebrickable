# -*- coding: utf-8 -*-

"""Console script for pyrebrickable."""
from __future__ import print_function

import json
from collections import namedtuple

import click
import yaml
from click import prompt

from rebrickable.cli.data import data
from rebrickable.cli.common import State
from rebrickable.cli.lego import lego
from rebrickable.cli.login import login
from rebrickable.cli.user import user
from rebrickable.cli.users import users
from rebrickable.cli.utils import get_data, DATA_PATH, EnumType, write_data, get_api_client, Unregistered, Enum


class OutputFormat(Enum):
    json = 0  # json.dumps
    yaml = 1  # yaml.dump
    py = 2  # print


OutputFormatter = namedtuple('OutputFormatter', ['output'])


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

    def push_state(format, ctx):
        ctx.obj = State(format, client=get_api_client())

    try:
        push_state(format, click_context)
    except Unregistered:
        if click_context.invoked_subcommand != 'register':
            print('Calling \"rebrickable register\" to register your API key:')
            click_context.invoke(register)
            push_state(format, click_context)


@main.command(help='registers an API key with the CLI')
def register():
    key = prompt('API key')
    data = get_data()
    data['api_key'] = key
    write_data(data)
    print('OK, registered API key in %s' % DATA_PATH)


main.add_command(lego)
main.add_command(data)
main.add_command(users)
main.add_command(user)
main.add_command(login)

if __name__ == "__main__":
    main()
