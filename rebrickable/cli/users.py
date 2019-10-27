import click

from rebrickable.api import UsersApi, Badge
from .common import object_print, add_typed_subcommands, \
    pass_state, get_or_push


@click.group(help='users-related data (global badge information)')
@pass_state
def users(state):
    state.api = UsersApi(state.client)


@users.command(name='badges')
@pass_state
@object_print
def users_badges_list(state):
    return state.api.users_badges_list()


@add_typed_subcommands(Badge)
@users.group('badge')
@pass_state
@get_or_push
@click.argument('badge_id', type=int)
def users_badge(state, badge_id):
    return state.api.users_badges_read(id=badge_id)
