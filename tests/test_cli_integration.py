from __future__ import print_function

from rebrickable_api import Set, Part, Color, Moc, PartList, PartListPart, SetList, SetListSet
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


def context_stack(*objs):
    ctx = None
    for obj in objs:
        if ctx is None:
            ctx = Context(main, obj=obj)
        else:
            ctx = Context(main, obj=obj, parent=ctx)
    return ctx


def do_test(cli_func, method, cli_args, call_kwargs, runner, api, context):
    mocked_method = getattr(api, method)
    mocked_method.return_value = 'stuff'
    result = runner.invoke(cli_func, cli_args, obj=api, parent=context)
    if result.exit_code != 0:
        print(result.output)
        pass
    mocked_method.assert_called_with(**call_kwargs)
    assert 'stuff\n' == result.output


# legoapi
lego_operations = [
    (lego_colors, 'lego_colors_list', [], {}),
    (lego_color, 'lego_colors_read', ['6'], {'id': 6}),
    (lego_element, 'lego_elements_read', ['1234'], {'element_id': '1234'}),
    (lego_part_categories, 'lego_part_categories_list', [], {}),
    (lego_part_category, 'lego_part_categories_read', ['17859'], {'id': 17859}),
    (lego_parts, 'lego_parts_list', [], {}),
    (lego_sets, 'lego_sets_list', [], {}),
    (lego_themes, 'lego_themes_list', [], {}),
    (lego_theme, 'lego_themes_read', ['1485'], {'id': '1485'}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], lego_operations)
def test_lego_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_lego_api):
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
    )

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_lego_api, context)


lego_set_operations = [
    (lego_set, 'lego_sets_read', ['75192-1'], {}),
    (lego_set_alternates, 'lego_sets_alternates_list', [], {}),
    (lego_set_parts, 'lego_sets_parts_list', [], {}),
    (lego_set_sets, 'lego_sets_sets_list', [], {}),
]

@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], lego_set_operations)
def test_lego_set_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_lego_api):
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
        Set(set_num='75192-1')
    )

    call_kwargs['set_num'] = '75192-1'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_lego_api, context)


lego_part_operations = [
    (lego_part_colors, 'lego_parts_colors_list', [], {}),
    (lego_part, 'lego_parts_read', ['3004'], {}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], lego_part_operations)
def test_lego_part_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_lego_api):
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
        Part(part_num='3004')
    )

    call_kwargs['part_num'] = '3004'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_lego_api, context)


lego_part_color_operations = [
    (lego_part_color, 'lego_parts_colors_read', ['45'], {}),
    (lego_part_color_sets, 'lego_parts_colors_sets_list', [], {}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], lego_part_color_operations)
def test_lego_part_color_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_lego_api):
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
        Part(part_num='3020'),
        Color(id=45),
    )

    call_kwargs['part_num'] = '3020'
    call_kwargs['color_id'] = 45

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_lego_api, context)


lego_moc_operations = [
    (lego_moc_parts, 'lego_mocs_parts_list', [], {}),
    (lego_moc, 'lego_mocs_read', ['MOC-5634'], {}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], lego_moc_operations)
def test_lego_moc_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_lego_api):
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
        Moc(set_num='MOC-5634')
    )
    call_kwargs['set_num'] = 'MOC-5634'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_lego_api, context)


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
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
        UserContext(api=mocked_users_api, token='abcdef')
    )
    call_kwargs['user_token'] = 'abcdef'
    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, context)


users_no_token_operations = [
    (users_badges_list, 'users_badges_list', [], {}),
    (users_badge, 'users_badges_read', ['12345'], {'id': 12345}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_no_token_operations)
def test_users_no_token_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
        UserContext(api=mocked_users_api, token='abcdef')
    )
    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, context)


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
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
        UserContext(api=mocked_users_api, token='abcdef'),
        PartList(id=987654321)
    )

    call_kwargs['list_id'] = 987654321
    call_kwargs['user_token'] = 'abcdef'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, context)


users_partlist_part_operations = [
    (user_partlist_part, 'users_partlists_parts_read', ['45', '3004'],
     {'color_id': 45}),
    (user_partlist_part_update, 'users_partlists_parts_update', ['475'],
     {'quantity': 475}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_partlist_part_operations)
def test_users_partlist_part_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
        UserContext(api=mocked_users_api, token='abcdef'),
        PartList(id=987654321),
        PartListPart(color=Color(id=45), part=Part(part_num='3004'))
    )
    call_kwargs['color_id'] = 45
    call_kwargs['part_num'] = '3004'
    call_kwargs['list_id'] = 987654321
    call_kwargs['user_token'] = 'abcdef'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, context)


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
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
        UserContext(api=mocked_users_api, token='abcdef'),
        SetList(id=987654321)
    )

    call_kwargs['list_id'] = 987654321
    call_kwargs['user_token'] = 'abcdef'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, context)


users_setlist_set_operations = [
    (user_setlist_set_delete, 'users_setlists_sets_delete', [], {}),
    (user_setlist_set_partial_update, 'users_setlists_sets_partial_update', ['1357-1'], {}),
    (user_setlist_set, 'users_setlists_sets_read', ['1357-1'], {}),
    (user_setlist_set_update, 'users_setlists_sets_update', [], {}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_setlist_set_operations)
def test_users_setlist_set_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
        UserContext(api=mocked_users_api, token='abcdef'),
        SetList(id=987654321),
        SetListSet(set_num='1357-1')
    )

    call_kwargs['list_id'] = 987654321
    call_kwargs['user_token'] = 'abcdef'
    call_kwargs['set_num'] = '1357-1'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, context)


users_set_operations = [
    (user_set_delete, 'users_sets_delete', [], {}),
    (user_set, 'users_sets_read', ['75192-1'], {}),
    (user_set_update, 'users_sets_update', [], {}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_set_operations)
def test_users_set_entrypoints(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    context = context_stack(
        GlobalContext(OutputFormatter(output=print), None),
        UserContext(api=mocked_users_api, token='abcdef'),
        Set(set_num='75192-1')
    )

    call_kwargs['set_num'] = '75192-1'
    call_kwargs['user_token'] = 'abcdef'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api, context)

"""

lego
  - colors:
    - list
  - color: 
    - read
  - element:
    - read
  - moc:
    - read 
    - parts  
  - part_categories:
    - list
  - part_category:
    - read
  - parts:
    - list
  - part:
    - read 
    - colors
    - color :
      - sets
  - sets:
    - list
  - set:
    - read 
    - alternates
    - parts
    - sets
  - themes:
    - list
  - theme:
    - read

users:
  - _token
  - badges
  - badge
  
user
  - allparts
  - build
  - lost_parts:
    - list
  - lost_part:
    - read
  - partlists:
    - list
  - partlist:
    - read
    - parts:
      - list
    - part:
      - read
    
  - parts:
    - list
  - profile:
    - read
  - setlists:
    - list
  - setlist:
    - read
    - sets:
      - list
    - set:
      - read
  - sets:
    - list
    - sync
  - set:
    - read

"""