# -*- coding: utf-8 -*-

"""Console script for pyrebrickable."""
from getpass import getpass

import click
from six.moves import input

from rebrickable_api import ApiClient, Configuration
from rebrickable_api import LegoApi, UsersApi
from rebrickable_api.rest import ApiException
from rebrickable_cli.utils import update_data, get_data, DATA_PATH


class UsersContext(object):
    def __init__(self, api, token):
        self.api = api
        self.token = token


pass_client = click.make_pass_decorator(ApiClient)
pass_legoapi = click.make_pass_decorator(LegoApi)
pass_userscontext = click.make_pass_decorator(UsersContext)
pass_usersapi = click.make_pass_decorator(UsersApi)


def get_api_client():
    configuration = Configuration()
    data = get_data()
    api_key = data['api_key']
    configuration.api_key['Authorization'] = api_key
    configuration.api_key_prefix['Authorization'] = 'key'
    return ApiClient(configuration)


@click.group(help="Rebrickable CLI implemented in Python")
@click.pass_context
def main(ctx, args=None):
    """Console script for pyrebrickable."""

    try:
        ctx.obj = get_api_client()
    except (IOError, KeyError, ValueError):
        if ctx.invoked_subcommand != 'register':
            print('please register your API key using: \nrebrickable register')
            raise click.Abort()


@main.command(help='registers an API key with the CLI')
def register():
    key = getpass(prompt='Please enter your API key:')
    update_data('api_key', key)
    print('OK, registered API key in %s' % DATA_PATH)


@main.group()
@pass_client
@click.pass_context
def lego(ctx, client):
    ctx.obj = LegoApi(client)


def get_users_context(client):
    users_api = UsersApi(client)
    data = get_data()
    users_token = data['users_token']
    return UsersContext(users_api, users_token)


@main.group()
@pass_client
@click.pass_context
def users(ctx, client):
    users_api = UsersApi(client)
    ctx.obj = users_api
    try:
        ctx.obj = get_users_context(client)
    except (IOError, KeyError, ValueError):
        if ctx.invoked_subcommand != 'login':
            print('Please login using: \nrebrickable users login')
            raise click.Abort()


@users.command(name='login')
@pass_usersapi
@click.argument('username', required=False)
def users_login(users_api, username=None):
    if username is None:
        username = input('Username: ')
    password = getpass()
    try:
        users_token = users_api.users_token_create(username, password)
        update_data('users_token', users_token.user_token)

        print('OK, saved users token into %s' % DATA_PATH)
    except ApiException as e:
        print('Login failed, response was %s' % e.body)
        raise click.Abort()


@lego.group(name='parts')
def lego_parts():
    pass


@lego_parts.group(name='colors')
def lego_parts_colors():
    pass


@lego_parts_colors.group(name='sets')
def lego_parts_colors_sets():
    pass


@lego_parts_colors_sets.command(name='list')
@pass_legoapi
@click.argument('color_id')
@click.argument('set_num')
def lego_parts_colors_sets_list(api, color_id, set_num):
    print(api.lego_parts_colors_sets_list(color_id=color_id, set_num=set_num))


@lego.command(name='colors')
@pass_legoapi
def lego_colors_list(api):
    print(api.lego_colors_list())


@lego.command(name='color')
@pass_legoapi
@click.argument('id')
def lego_colors_read(api, id):
    print(api.lego_colors_read(id=id))


@lego.command(name='element')
@pass_legoapi
@click.argument('element_id')
def lego_elements_read(api, element_id):
    print(api.lego_elements_read(element_id=element_id))


@lego.group(name='mocs')
def lego_mocs():
    pass


@lego_mocs.group(name='parts')
def lego_mocs_parts():
    pass


@lego_mocs_parts.command(name='list')
@pass_legoapi
@click.argument('set_num')
def lego_mocs_parts_list(api, set_num):
    print(api.lego_mocs_parts_list(set_num=set_num))


@lego_mocs.command(name='read')
@pass_legoapi
@click.argument('set_num')
def lego_mocs_read(api, set_num):
    print(api.lego_mocs_read(set_num=set_num))


@lego.command(name='part_categories')
@pass_legoapi
def lego_part_categories_list(api):
    print(api.lego_part_categories_list())


@lego.command(name='part_category')
@pass_legoapi
@click.argument('id')
def lego_part_categories_read(api, id):
    print(api.lego_part_categories_read(id=id))


@lego_parts_colors.command(name='list')
@pass_legoapi
@click.argument('part_num')
def lego_parts_colors_list(api, part_num):
    print(api.lego_parts_colors_list(part_num=part_num))


@lego_parts_colors.command(name='read')
@pass_legoapi
@click.argument('color_id')
@click.argument('part_num')
def lego_parts_colors_read(api, color_id, part_num):
    print(api.lego_parts_colors_read(color_id=color_id, part_num=part_num))


@lego_parts_colors_sets.command(name='list')
@pass_legoapi
@click.argument('color_id')
@click.argument('part_num')
def lego_parts_colors_sets_list(api, color_id, part_num):
    print(api.lego_parts_colors_sets_list(color_id=color_id, part_num=part_num))


@lego_parts.command(name='list')
@pass_legoapi
def lego_parts_list(api):
    print(api.lego_parts_list())


@lego.command(name='part')
@pass_legoapi
@click.argument('part_num')
def lego_parts_read(api, part_num):
    print(api.lego_parts_read(part_num=part_num))


@lego.group(name='sets')
def lego_sets():
    pass


@lego_sets.group(name='alternates')
def lego_sets_alternates():
    pass


@lego_sets_alternates.command(name='list')
@pass_legoapi
@click.argument('set_num')
def lego_sets_alternates_list(api, set_num):
    print(api.lego_sets_alternates_list(set_num=set_num))


@lego_sets.command(name='list')
@pass_legoapi
def lego_sets_list(api):
    print(api.lego_sets_list())


@lego_sets.group(name='parts')
def lego_sets_parts():
    pass


@lego_sets_parts.command(name='list')
@pass_legoapi
@click.argument('set_num')
def lego_sets_parts_list(api, set_num):
    print(api.lego_sets_parts_list(set_num=set_num))


@lego.command(name='set')
@pass_legoapi
@click.argument('set_num')
def lego_sets_read(api, set_num):
    print(api.lego_sets_read(set_num=set_num))


@lego_sets.group(name='sets')
def lego_sets_sets():
    pass


@lego_sets_sets.command(name='list')
@pass_legoapi
@click.argument('set_num')
def lego_sets_sets_list(api, set_num):
    print(api.lego_sets_sets_list(set_num=set_num))


@lego.command(name='themes')
@pass_legoapi
def lego_themes_list(api):
    print(api.lego_themes_list())


@lego.command(name='theme')
@pass_legoapi
@click.argument('id')
def lego_themes_read(api, id):
    print(api.lego_themes_read(id=id))


@users.group(name='allparts')
def users_allparts():
    pass


@users_allparts.command(name='list')
@pass_userscontext
def users_allparts_list(users_context):
    print(users_context.api.users_allparts_list(user_token=users_context.token))


@users.command(name='badges')
@pass_userscontext
def users_badges_list(users_context):
    print(users_context.api.users_badges_list())


@users.command(name='badge')
@pass_userscontext
@click.argument('id')
def users_badges_read(users_context, id):
    print(users_context.api.users_badges_read(id=id))


@users.command(name='build')
@pass_userscontext
@click.argument('set_num')
def users_build_read(users_context, set_num):
    print(users_context.api.users_build_read(user_token=users_context.token,
                                             set_num=set_num))


@users.group(name='lost_parts')
def users_lost_parts():
    pass


@users_lost_parts.command(name='create')
@pass_userscontext
@click.argument('inv_part_id')
def users_lost_parts_create(users_context, inv_part_id):
    print(users_context.api.users_lost_parts_create(user_token=users_context.token, inv_part_id=inv_part_id))


@users_lost_parts.command(name='delete')
@pass_userscontext
@click.argument('id')
def users_lost_parts_delete(users_context, id):
    print(users_context.api.users_lost_parts_delete(user_token=users_context.token, id=id))


@users_lost_parts.command(name='list')
@pass_userscontext
def users_lost_parts_list(users_context):
    print(users_context.api.users_lost_parts_list(user_token=users_context.token))


@users.group(name='partlists')
def users_partlists():
    pass


@users_partlists.command(name='create')
@pass_userscontext
@click.argument('name')
def users_partlists_create(users_context, name):
    print(users_context.api.users_partlists_create(user_token=users_context.token,
                                                   name=name))


@users_partlists.command(name='delete')
@pass_userscontext
@click.argument('list_id')
def users_partlists_delete(users_context, list_id):
    print(users_context.api.users_partlists_delete(user_token=users_context.token,
                                                   list_id=list_id))


@users_partlists.command(name='list')
@pass_userscontext
def users_partlists_list(users_context):
    print(users_context.api.users_partlists_list(user_token=users_context.token))


@users_partlists.group(name='partial')
def users_partlists_partial():
    pass


@users_partlists_partial.command(name='update')
@pass_userscontext
@click.argument('list_id')
def users_partlists_partial_update(users_context, list_id):
    print(users_context.api.users_partlists_partial_update(user_token=users_context.token,
                                                           list_id=list_id))


@users_partlists.group(name='parts')
def users_partlists_parts():
    pass


@users_partlists_parts.command(name='create')
@pass_userscontext
@click.argument('list_id')
@click.argument('part_num')
@click.argument('quantity')
@click.argument('color_id')
def users_partlists_parts_create(users_context, list_id, part_num, quantity, color_id):
    print(users_context.api.users_partlists_parts_create(user_token=users_context.token,
                                                         list_id=list_id,
                                                         part_num=part_num,
                                                         quantity=quantity,
                                                         color_id=color_id))


@users_partlists_parts.command(name='delete')
@pass_userscontext
@click.argument('color_id')
@click.argument('list_id')
@click.argument('part_num')
def users_partlists_parts_delete(users_context, color_id, list_id, part_num):
    print(users_context.api.users_partlists_parts_delete(user_token=users_context.token,
                                                         color_id=color_id,
                                                         list_id=list_id,
                                                         part_num=part_num))


@users_partlists_parts.command(name='list')
@pass_userscontext
@click.argument('list_id')
def users_partlists_parts_list(users_context, list_id):
    print(users_context.api.users_partlists_parts_list(user_token=users_context.token, list_id=list_id))


@users_partlists_parts.command(name='read')
@pass_userscontext
@click.argument('color_id')
@click.argument('list_id')
@click.argument('part_num')
def users_partlists_parts_read(users_context, color_id, list_id, part_num):
    print(
        users_context.api.users_partlists_parts_read(user_token=users_context.token, color_id=color_id, list_id=list_id,
                                                     part_num=part_num))


@users_partlists_parts.command(name='update')
@pass_userscontext
@click.argument('color_id')
@click.argument('list_id')
@click.argument('part_num')
@click.argument('quantity')
def users_partlists_parts_update(users_context, color_id, list_id, part_num, quantity):
    print(users_context.api.users_partlists_parts_update(user_token=users_context.token, color_id=color_id,
                                                         list_id=list_id, part_num=part_num,
                                                         quantity=quantity))


@users_partlists.command(name='read')
@pass_userscontext
@click.argument('list_id')
def users_partlists_read(users_context, list_id):
    print(users_context.api.users_partlists_read(users_context.token, list_id=list_id))


@users_partlists.command(name='update')
@pass_userscontext
@click.argument('list_id')
@click.argument('name')
def users_partlists_update(users_context, list_id, name):
    print(users_context.api.users_partlists_update(users_context.token, list_id=list_id, name=name))


@users.command(name='parts')
@pass_userscontext
def users_parts_list(users_context):
    print(users_context.api.users_parts_list(user_token=users_context.token))


@users.command(name='profile')
@pass_userscontext
def users_profile_list(users_context):
    print(users_context.api.users_profile_list(user_token=users_context.token))


@users.group('setlists')
def users_setlists():
    pass


@users_setlists.command(name='create')
@pass_userscontext
@click.argument('name')
def users_setlists_create(users_context, name):
    print(users_context.api.users_setlists_create(user_token=users_context.token, name=name))


@users_setlists.command(name='delete')
@pass_userscontext
@click.argument('list_id')
def users_setlists_delete(users_context, list_id):
    print(users_context.api.users_setlists_delete(user_token=users_context.token, list_id=list_id))


@users_setlists.command(name='list')
@pass_userscontext
def users_setlists_list(users_context):
    print(users_context.api.users_setlists_list(user_token=users_context.token))


@users_setlists.group(name='partial')
def users_setlists_partial():
    pass


@users_setlists_partial.command(name='update')
@pass_userscontext
@click.argument('list_id')
def users_setlists_partial_update(users_context, list_id):
    print(users_context.api.users_setlists_partial_update(user_token=users_context.token, list_id=list_id))


@users_setlists.command(name='read')
@pass_userscontext
@click.argument('list_id')
def users_setlists_read(users_context, list_id):
    print(users_context.api.users_setlists_read(user_token=users_context.token, list_id=list_id))


@users_setlists.group(name='sets')
def users_setlists_sets():
    pass


@users_setlists_sets.command(name='create')
@pass_userscontext
@click.argument('list_id')
@click.argument('set_num')
def users_setlists_sets_create(users_context, list_id, set_num):
    print(users_context.api.users_setlists_sets_create(user_token=users_context.token,
                                                       list_id=list_id,
                                                       set_num=set_num))


@users_setlists_sets.command(name='delete')
@pass_userscontext
@click.argument('list_id')
@click.argument('set_num')
def users_setlists_sets_delete(users_context, list_id, set_num):
    print(users_context.api.users_setlists_sets_delete(user_token=users_context.token,
                                                       list_id=list_id,
                                                       set_num=set_num))


@users_setlists_sets.command(name='list')
@pass_userscontext
@click.argument('list_id')
def users_setlists_sets_list(users_context, list_id):
    print(users_context.api.users_setlists_sets_list(user_token=users_context.token,
                                                     list_id=list_id))


@users_setlists_sets.group()
def users_setlists_sets_partial():
    pass


@users_setlists_sets_partial.command(name='update')
@pass_userscontext
@click.argument('list_id')
@click.argument('set_num')
def users_setlists_sets_partial_update(users_context, list_id, set_num):
    print(users_context.api.users_setlists_sets_partial_update(user_token=users_context.token,
                                                               list_id=list_id,
                                                               set_num=set_num))


@users_setlists_sets.command(name='read')
@pass_userscontext
@click.argument('list_id')
@click.argument('set_num')
def users_setlists_sets_read(users_context, list_id, set_num):
    print(users_context.api.users_setlists_sets_read(user_token=users_context.token,
                                                     list_id=list_id,
                                                     set_num=set_num))


@users_setlists_sets.command(name='update')
@pass_userscontext
@click.argument('list_id')
@click.argument('set_num')
def users_setlists_sets_update(users_context, list_id, set_num):
    print(users_context.api.users_setlists_sets_update(user_token=users_context.token,
                                                       list_id=list_id,
                                                       set_num=set_num))


@users_setlists.command(name='update')
@pass_userscontext
@click.argument('list_id')
@click.argument('name')
def users_setlists_update(users_context, list_id, name):
    print(users_context.api.users_setlists_update(user_token=users_context.token,
                                                  list_id=list_id,
                                                  name=name))


@users.group(name='sets')
def users_sets():
    pass


@users_sets.command(name='create')
@pass_userscontext
@click.argument('set_num')
def users_sets_create(users_context, set_num):
    print(users_context.api.users_sets_create(user_token=users_context.token,
                                              set_num=set_num))


@users_sets.command(name='delete')
@pass_userscontext
@click.argument('set_num')
def users_sets_delete(users_context, set_num):
    print(users_context.api.users_sets_delete(user_token=users_context.token, set_num=set_num))


@users_sets.command(name='list')
@pass_userscontext
def users_sets_list(users_context):
    print(users_context.api.users_sets_list(user_token=users_context.token))


@users_sets.command(name='read')
@pass_userscontext
@click.argument('set_num')
def users_sets_read(users_context, set_num):
    print(users_context.api.users_sets_read(user_token=users_context.token, set_num=set_num))


@users_sets.group(name='sync')
def users_sets_sync():
    pass


@users_sets_sync.command(name='create')
@pass_userscontext
@click.argument('set_num')
def users_sets_sync_create(users_context, set_num):
    print(users_context.api.users_sets_sync_create(user_token=users_context.token, set_num=set_num))


@users_sets_sync.command(name='update')
@pass_userscontext
@click.argument('set_num')
def users_sets_update(users_context, set_num):
    print(users_context.api.users_sets_update(user_token=users_context.token, set_num=set_num))


@users.group(name='token')
def users_token():
    pass


@users_token.command(name='create')
@pass_userscontext
@click.argument('username')
@click.argument('password')
def users_token_create(users_context, username, password):
    print(users_context.api.users_token_create(username=username, password=password))


if __name__ == "__main__":
    main()
