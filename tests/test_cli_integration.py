from __future__ import print_function

from six import StringIO

import pytest
from click import Context, Command

from rebrickable_cli.cli.common import UserContext
from rebrickable_cli.cli.lego import *
from rebrickable_cli.cli.main import *
from rebrickable_cli.cli.user import *
from rebrickable_cli.cli.users import *


def parametrized(*args, **kwargs):
    def decorator(fun):
        if 'ids' not in kwargs:
            def get_id(param):
                if isinstance(param, Command):
                    return param.callback.__name__
                return str(param)

            kwargs['ids'] = get_id
        return pytest.mark.parametrize(*args, **kwargs)(fun)

    return decorator


def do_test(cli_func, method, cli_args, call_kwargs, runner, api, context):
    mocked_method = getattr(api, method)
    mocked_method.return_value = 'stuff'
    result = runner.invoke(cli_func, cli_args, obj=context)
    if result.exit_code != 0:
        print(result.output)
        pass
    mocked_method.assert_called_with(**call_kwargs)
    assert 'stuff\n' == result.output


users_operations = [
    (user_partlists_create, 'users_partlists_create', ['test'], {'name': 'test'}),
    (user_partlists_list, 'users_partlists_list', [], {}),
    (user_allparts, 'users_allparts_list', [], {}),

    (user_build, 'users_build_read', ['75192-1'], {'set_num': '75192-1'}),
    (user_lost_parts_create, 'users_lost_parts_create', ['14523'], {'inv_part_id': 14523}),
    (user_lost_parts_delete, 'users_lost_parts_delete', ['47859'], {'id': 47859}),
    (user_lost_parts_list, 'users_lost_parts_list', [], {}),
    (user_parts, 'users_parts_list', [], {}),

    (user_setlists_create, 'users_setlists_create', ['test'], {'name': 'test'}),
    (user_setlists_list, 'users_setlists_list', [], {}),

    (user_sets_create, 'users_sets_create', ['1234-4'], {'set_num': '1234-4'}),
    (user_sets_list, 'users_sets_list', [], {}),
    (user_sets_sync, 'users_sets_sync_create', ["-f", StringIO("{\"test\": \"foo\"}")],
     {'array_of_set_list_sets': {'test': 'foo'}}),
    (user_profile, 'users_profile_list', [], {}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_operations)
def test_users_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    state = State(format=OutputFormatter(output=print), api=mocked_users_api, user_token='abcdef')

    call_kwargs['user_token'] = 'abcdef'
    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, state)


users_no_token_operations = [
    (users_badges_list, 'users_badges_list', [], {}),
    (users_badge, 'users_badges_read', ['12345'], {'id': 12345}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_no_token_operations)
def test_users_no_token_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    state = State(format=OutputFormatter(output=print), api=mocked_users_api, user_token='abcdef')

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, state)


users_partlist_operations = [
    (user_partlist_partial_update, 'users_partlists_partial_update', [], {}),
    (user_partlist_delete, 'users_partlists_delete', [], {}),
    (user_partlist_parts_create, 'users_partlists_parts_create', ['3004', '4', '45'],
     {'part_num': '3004', 'color_id': 45, 'quantity': 4}),
    (user_partlist_parts_delete, 'users_partlists_parts_delete', ['35', '3002'], {'part_num': '3002', 'color_id': 35}),
    (user_partlist_parts_list, 'users_partlists_parts_list', [], {}),
    (user_partlist, 'users_partlists_read', ['987654321'], {}),
    (user_partlist_update, 'users_partlists_update', ['test'], {'name': 'test'}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_partlist_operations)
def test_users_partlist_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    state = State(format=OutputFormatter(output=print), api=mocked_users_api, user_token='abcdef', list_id=987654321)

    call_kwargs['list_id'] = 987654321
    call_kwargs['user_token'] = 'abcdef'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, state)


users_partlist_part_operations = [
    (user_partlist_part, 'users_partlists_parts_read', ['45', '3004'],
     {'color_id': 45}),
    (user_partlist_part_update, 'users_partlists_parts_update', ['475'],
     {'quantity': 475}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_partlist_part_operations)
def test_users_partlist_part_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    state = State(format=OutputFormatter(output=print), api=mocked_users_api, user_token='abcdef', list_id=987654321, color_id=45, part_num='3004')

    call_kwargs['color_id'] = 45
    call_kwargs['part_num'] = '3004'
    call_kwargs['list_id'] = 987654321
    call_kwargs['user_token'] = 'abcdef'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, state)


users_setlist_operations = [
    (user_setlist, 'users_setlists_read', ['987654321'], {}),
    (user_setlist_delete, 'users_setlists_delete', [], {}),
    (user_setlist_sets_create, 'users_setlists_sets_create', ['1234-1'], {'set_num': '1234-1'}),
    (user_setlist_sets_list, 'users_setlists_sets_list', [], {}),
    (user_setlist_update, 'users_setlists_update', ['test'], {'name': 'test'}),
    (user_setlist_partial_update, 'users_setlists_partial_update', [], {}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_setlist_operations)
def test_users_setlist_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    state = State(format=OutputFormatter(output=print),  api=mocked_users_api, user_token='abcdef', list_id=987654321)

    call_kwargs['list_id'] = 987654321
    call_kwargs['user_token'] = 'abcdef'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, state)


users_setlist_set_operations = [
    (user_setlist_set_delete, 'users_setlists_sets_delete', [], {}),
    (user_setlist_set_partial_update, 'users_setlists_sets_partial_update', ['1357-1'], {}),
    (user_setlist_set, 'users_setlists_sets_read', ['1357-1'], {}),
    (user_setlist_set_update, 'users_setlists_sets_update', [], {}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_setlist_set_operations)
def test_users_setlist_set_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    state = State(format=OutputFormatter(output=print), api=mocked_users_api, user_token='abcdef', list_id=987654321, set_num='1357-1')

    call_kwargs['list_id'] = 987654321
    call_kwargs['user_token'] = 'abcdef'
    call_kwargs['set_num'] = '1357-1'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, state)


users_set_operations = [
    (user_set_delete, 'users_sets_delete', [], {}),
    (user_set, 'users_sets_read', ['75192-1'], {}),
    (user_set_update, 'users_sets_update', [], {}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_set_operations)
def test_users_set_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    state = State(format=OutputFormatter(output=print), api=mocked_users_api, user_token='abcdef', set_num='75192-1')

    call_kwargs['set_num'] = '75192-1'
    call_kwargs['user_token'] = 'abcdef'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, state)
