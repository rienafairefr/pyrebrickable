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
}

failing = [
    'lego_elements_read',
    'lego_sets_read',
    'users_allparts_list',
    'users_build_read',
    'users_lost_parts_delete',
    'users_partlists_delete',
    'users_partlists_partial_update',
    'users_partlists_parts_create',
    'users_partlists_parts_delete',
    'users_partlists_parts_list',
    'users_partlists_parts_read',
    'users_partlists_parts_update',
    'users_partlists_read',
    'users_partlists_update',
    'users_setlists_delete',
    'users_setlists_partial_update',
    'users_setlists_read',
    'users_setlists_sets_create',
    'users_setlists_sets_delete',
    'users_setlists_sets_list',
    'users_setlists_sets_partial_update',
    'users_setlists_sets_read',
    'users_setlists_sets_update',
    'users_setlists_update',
    'users_sets_create',
    'users_sets_delete',
    'users_sets_read',
    'users_sets_sync_create',
    'users_sets_update',
    'users_token_create',
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
