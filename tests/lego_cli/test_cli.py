from __future__ import print_function
from rebrickable_api import Set, Part, Color, Moc
from rebrickable_cli.cli.common import GlobalContext, LegoContext
from rebrickable_cli.cli.lego import lego_colors, lego_color, lego_element, lego_part_categories, lego_part_category, \
    lego_parts, lego_sets, lego_themes, lego_theme, lego_set, lego_set_alternates, lego_set_parts, lego_set_sets, \
    lego_part_colors, lego_part, lego_part_color, lego_part_color_sets, lego_moc_parts, lego_moc
from rebrickable_cli.cli.main import OutputFormatter

from tests.test_cli_integration import parametrized, context_stack, do_test

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
        LegoContext(api=mocked_lego_api)
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
        LegoContext(api=mocked_lego_api, set_num='75192-1')
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
        LegoContext(api=mocked_lego_api, part_num='3004')
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
        LegoContext(api=mocked_lego_api, part_num='3020', color_id=45)
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
        LegoContext(api=mocked_lego_api, set_num='MOC-5634')
    )
    call_kwargs['set_num'] = 'MOC-5634'

    do_test(cli_func, method, cli_args, call_kwargs, runner, mocked_lego_api, context)