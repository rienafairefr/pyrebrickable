'lego_colors'
from inspect import getmembers
import random
import click
from click.testing import CliRunner

from rebrickable import cli, LegoApi
from rebrickable.cli import get_api_client, get_users_context

alldefs = getmembers(cli)
random.shuffle(alldefs)
client = get_api_client()
users_context = get_users_context(client)
lego_api = LegoApi(client)
runner = CliRunner()

test_args = {
    'lego_mocs_read': ['MOC-4528'],
    'users_partlists_parts_list': ['66871'],
    'users_partlists_parts_read': ['8', '40480', '6587'],
    'users_partlists_read': ['40476'],
    'users_setlists_read': ['161396'],
    'users_setlists_sets_list': ['161396'],
    'users_setlists_sets_read': ['161396', '41116-1'],
    'users_sets_read': ['5866-1'],
    'users_build_read': ['75192-1'],
    'lego_sets_read': ['75192-1'],
    'lego_elements_read': ['4297717']
}

failing = [
    'users_partlists_delete',
    'users_setlists_partial_update',
    'users_setlists_delete',
    'users_setlists_sets_delete',
    'users_setlists_sets_create',
    'users_token_create',
    'users_setlists_sets_update',
    'users_sets_sync_create',
    'users_lost_parts_delete',
    'users_partlists_partial_update',
    'users_sets_create',
    'users_setlists_update',
    'users_setlists_sets_partial_update',
    'users_partlists_update',
    'users_partlists_parts_update',
    'users_partlists_parts_create',
    'users_sets_delete',
    'users_partlists_parts_delete',
    'users_sets_update',
]

print('[')
for (name, fun) in alldefs:
    if name == 'register':
        continue
    if name == 'users_login':
        continue
    if name not in failing:
        continue

    if isinstance(fun, click.Command) and not isinstance(fun, click.Group):
        if name.startswith('users'):
            obj = users_context
        elif name.startswith('lego'):
            obj = lego_api

        if name in test_args:
            args = test_args[name]
        else:
            args = ['1' for param in fun.params]
        result = runner.invoke(fun, obj=obj, args=args)
        if result.exit_code != 0:
            print('\'' + name + '\',')
print(']')
