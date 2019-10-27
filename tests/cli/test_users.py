from __future__ import print_function

from rebrickable.cli.common import State
from rebrickable.cli.main import OutputFormatter
from rebrickable.cli.users import users_badges_list, users_badge
from tests.utils import parametrized, do_test

users_operations = [
    (users_badges_list, 'users_badges_list', [], {}),
    (users_badge, 'users_badges_read', ['12345'], {'id': 12345}),
]


@parametrized(['cli_func', 'method', 'cli_args', 'call_kwargs'], users_operations)
def test_users_operations(cli_func, method, cli_args, call_kwargs, runner, mocked_users_api):
    state = State(format=OutputFormatter(output=print), api=mocked_users_api)

    do_test(cli_func, method, cli_args, call_kwargs, runner, state)
