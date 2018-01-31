# -*- coding: utf-8 -*-

"""Console script for pyrebrickable."""
from getpass import getpass

import click
import os

import rebrickable
from rebrickable import LegoApi, ApiClient, UsersApi


class UserApiAndToken(object):
    def __init__(self, api, token):
        self.api = api
        self.token = token


pass_client = click.make_pass_decorator(ApiClient)
pass_legoapi = click.make_pass_decorator(LegoApi)
pass_usersapi = click.make_pass_decorator(UserApiAndToken)

key_path = os.path.expanduser('~/.rebrickable')
usertoken_path = os.path.expanduser('~/.rebrickable.usertoken')


@click.group(help="Rebrickable CLI implemented in Python")
@click.pass_context
def main(ctx, args=None):
    """Console script for pyrebrickable."""
    configuration = rebrickable.Configuration()

    try:
        with open(key_path, 'r') as key_file:
            api_key = key_file.read()
            configuration.api_key['Authorization'] = api_key
            configuration.api_key_prefix['Authorization'] = 'key'
            ctx.obj = rebrickable.ApiClient(configuration)
    except FileNotFoundError:
        if ctx.invoked_subcommand != 'register':
            print('key file %s does not exist, please register your API key using: \n%s register' % (
                key_path, rebrickable.__name__))
            raise click.Abort()


@main.command(help='registers an API key with the CLI')
def register():
    key = getpass(prompt='Please enter your API key:')
    with open(key_path, 'w') as key_file:
        print(key)
        key_file.write(key)
        print('OK, saved into %s' % key_path)


@main.group()
@pass_client
@click.pass_context
def lego(ctx, client):
    ctx.obj = LegoApi(client)


@main.group()
@pass_client
@click.pass_context
def users(ctx, client):
    users_api = UsersApi(client)
    
    try:
        with open(usertoken_path, 'r') as usertoken_file:
            user_token = usertoken_file.read()
    except FileNotFoundError:
        if ctx.invoked_subcommand != 'register':
            print('User token %s does not exist, please login using: \n%s login' % (
                key_path, rebrickable.__name__))
            raise click.Abort()
    
    ctx.obj = UserApiAndToken(users_api, users_token)



@users.command(name='login')
@pass_usersapi
@click.argument('username', required=False)
def users_login(api, username):
    password = getpass()
    user_token = api_token.api.users_token_create(username=username, password=password)
    with open(usertoken_path, 'w') as usertoken_file:
        print(user_token)
        usertoken_file.write(user_token)
        print('OK, saved into %s' % usertoken_path)


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


@lego.group(name='colors')
def lego_colors():
    pass


@lego_colors.command(name='list')
@pass_legoapi
def lego_colors_list(api):
    print(api.lego_colors_list())


@lego_colors.command(name='read')
@pass_legoapi
@click.argument('id')
def lego_colors_read(api, id):
    print(api.lego_colors_read(id=id))


@lego.group(name='elements')
def lego_elements():
    pass


@lego_elements.command(name='read')
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


@lego.group(name='part_categories')
def lego_part_categories():
    pass


@lego_part_categories.command(name='list')
@pass_legoapi
def lego_part_categories_list(api):
    print(api.lego_part_categories_list())


@lego_part_categories.command(name='read')
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


@lego_parts.command(name='read')
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


@lego_sets.command(name='read')
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


@lego.group(name='themes')
def lego_themes():
    pass


@lego_themes.command(name='list')
@pass_legoapi
def lego_themes_list(api):
    print(api.lego_themes_list())


@lego_themes.command(name='read')
@pass_legoapi
@click.argument('id')
def lego_themes_read(api, id):
    print(api.lego_themes_read(id=id))


@users.group(name='allparts')
def users_allparts():
    pass


@users_allparts.command(name='list')
@pass_usersapi
@click.argument('user_token')
def users_allparts_list(api_token):
    print(api_token.api_token.api.users_allparts_list(user_token=api_token.token))


@users.group(name='badges')
def users_badges():
    pass


@users_badges.command(name='list')
@pass_usersapi
def users_badges_list(api_token):
    print(api_token.api.users_badges_list())


@users_badges.command(name='read')
@pass_usersapi
@click.argument('id')
def users_badges_read(api_token, id):
    print(api_token.api.users_badges_read(id=id))


@users.group(name='build')
def users_build():
    pass


@users_build.command(name='read')
@pass_usersapi
@click.argument('user_token')
@click.argument('set_num')
def users_build_read(api_token, set_num):
    print(api_token.api.users_build_read(user_token=api_token.token,
                               set_num=set_num))


@users.group(name='lost')
def users_lost():
    pass


@users_lost.group(name='parts')
def users_lost_parts():
    pass


@users_lost_parts.command(name='create')
@pass_usersapi
@click.argument('user_token')
@click.argument('inv_part_id')
def users_lost_parts_create(api_token, inv_part_id):
    print(api_token.api.users_lost_parts_create(user_token=api_token.token, inv_part_id=inv_part_id))


@users_lost_parts.command(name='delete')
@pass_usersapi
@click.argument('user_token')
@click.argument('id')
def users_lost_parts_delete(api_token, id):
    print(api_token.api.users_lost_parts_delete(user_token=api_token.token, id=id))


@users_lost_parts.command(name='list')
@pass_usersapi
@click.argument('user_token')
def users_lost_parts_list(api_token):
    print(api_token.api.users_lost_parts_list(user_token=api_token.token))


@users.group(name='partlists')
def users_partlists():
    pass


@users_partlists.command(name='create')
@pass_usersapi
@click.argument('user_token')
@click.argument('name')
def users_partlists_create(api_token, name):
    print(api_token.api.users_partlists_create(user_token=api_token.token,
                                     name=name))


@users_partlists.command(name='delete')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
def users_partlists_delete(api_token, list_id):
    print(api_token.api.users_partlists_delete(user_token=api_token.token,
                                     list_id=list_id))


@users_partlists.command(name='list')
@pass_usersapi
@click.argument('user_token')
def users_partlists_list(api_token):
    print(api_token.api.users_partlists_list(user_token=api_token.token))


@users_partlists.group(name='partial')
def users_partlists_partial():
    pass


@users_partlists_partial.command(name='update')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
def users_partlists_partial_update(api_token, list_id):
    print(api_token.api.users_partlists_partial_update(user_token=api_token.token,
                                             list_id=list_id))


@users_partlists.group(name='parts')
def users_partlists_parts():
    pass


@users_partlists_parts.command(name='create')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
@click.argument('part_num')
@click.argument('quantity')
@click.argument('color_id')
def users_partlists_parts_create(api_token, list_id, part_num, quantity, color_id):
    print(api_token.api.users_partlists_parts_create(user_token=api_token.token,
                                           list_id=list_id,
                                           part_num=part_num,
                                           quantity=quantity,
                                           color_id=color_id))


@users_partlists_parts.command(name='delete')
@pass_usersapi
@click.argument('user_token')
@click.argument('color_id')
@click.argument('list_id')
@click.argument('part_num')
def users_partlists_parts_delete(api_token, color_id, list_id, part_num):
    print(api_token.api.users_partlists_parts_delete(user_token=api_token.token,
                                           color_id=color_id,
                                           list_id=list_id,
                                           part_num=part_num))


@users_partlists_parts.command(name='list')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
def users_partlists_parts_list(api_token, list_id):
    print(api_token.api.users_partlists_parts_list(user_token=api_token.token, list_id=list_id))


@users_partlists_parts.command(name='read')
@pass_usersapi
@click.argument('user_token')
@click.argument('color_id')
@click.argument('list_id')
@click.argument('part_num')
def users_partlists_parts_read(api_token, color_id, list_id, part_num):
    print(api_token.api.users_partlists_parts_read(user_token=api_token.token, color_id=color_id, list_id=list_id, part_num=part_num))


@users_partlists_parts.command(name='update')
@pass_usersapi
@click.argument('user_token')
@click.argument('color_id')
@click.argument('list_id')
@click.argument('part_num')
@click.argument('quantity')
def users_partlists_parts_update(api_token, color_id, list_id, part_num, quantity):
    print(api_token.api.users_partlists_parts_update(user_token=api_token.token, color_id=color_id, list_id=list_id, part_num=part_num,
                                           quantity=quantity))


@users_partlists.command(name='read')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
def users_partlists_read(api_token, list_id):
    print(api_token.api.users_partlists_read(user_token, list_id=list_id))


@users_partlists.command(name='update')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
@click.argument('name')
def users_partlists_update(api_token, list_id, name):
    print(api_token.api.users_partlists_update(user_token, list_id=list_id, name=name))


@users.group(name='parts')
def users_parts():
    pass


@users_parts.command(name='list')
@pass_usersapi
@click.argument('user_token')
def users_parts_list(api_token):
    print(api_token.api.users_parts_list(user_token=api_token.token))


@users.group(name='profile')
def users_profile():
    pass


@users_profile.command(name='list')
@pass_usersapi
@click.argument('user_token')
def users_profile_list(api_token):
    print(api_token.api.users_profile_list(user_token=api_token.token))


@users.group('setlists')
def users_setlists():
    pass


@users_setlists.command(name='create')
@pass_usersapi
@click.argument('user_token')
@click.argument('name')
def users_setlists_create(api_token, name):
    print(api_token.api.users_setlists_create(user_token=api_token.token, name=name))


@users_setlists.command(name='delete')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
def users_setlists_delete(api_token, list_id):
    print(api_token.api.users_setlists_delete(user_token=api_token.token, list_id=list_id))


@users_setlists.command(name='list')
@pass_usersapi
@click.argument('user_token')
def users_setlists_list(api_token):
    print(api_token.api.users_setlists_list(user_token=api_token.token))


@users_setlists.group(name='partial')
def users_setlists_partial():
    pass


@users_setlists_partial.command(name='update')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
def users_setlists_partial_update(api_token, list_id):
    print(api_token.api.users_setlists_partial_update(user_token=api_token.token, list_id=list_id))


@users_setlists.command(name='read')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
def users_setlists_read(api_token, list_id):
    print(api_token.api.users_setlists_read(user_token=api_token.token, list_id=list_id))


@users_setlists.group(name='sets')
def users_setlists_sets():
    pass


@users_setlists_sets.command(name='create')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
@click.argument('set_num')
def users_setlists_sets_create(api_token, list_id, set_num):
    print(api_token.api.users_setlists_sets_create(user_token=api_token.token,
                                         list_id=list_id,
                                         set_num=set_num))


@users_setlists_sets.command(name='delete')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
@click.argument('set_num')
def users_setlists_sets_delete(api_token, list_id, set_num):
    print(api_token.api.users_setlists_sets_delete(user_token=api_token.token,
                                         list_id=list_id,
                                         set_num=set_num))


@users_setlists_sets.command(name='list')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
def users_setlists_sets_list(api_token, list_id):
    print(api_token.api.users_setlists_sets_list(user_token=api_token.token,
                                       list_id=list_id))


@users_setlists_sets.group()
def users_setlists_sets_partial():
    pass


@users_setlists_sets_partial.command(name='update')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
@click.argument('set_num')
def users_setlists_sets_partial_update(api_token, list_id, set_num):
    print(api_token.api.users_setlists_sets_partial_update(user_token=api_token.token,
                                                 list_id=list_id,
                                                 set_num=set_num))


@users_setlists_sets.command(name='read')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
@click.argument('set_num')
def users_setlists_sets_read(api_token, list_id, set_num):
    print(api_token.api.users_setlists_sets_read(user_token=api_token.token,
                                       list_id=list_id,
                                       set_num=set_num))


@users_setlists_sets.command(name='update')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
@click.argument('set_num')
def users_setlists_sets_update(api_token, list_id, set_num):
    print(api_token.api.users_setlists_sets_update(user_token=api_token.token,
                                         list_id=list_id,
                                         set_num=set_num))


@users_setlists.command(name='update')
@pass_usersapi
@click.argument('user_token')
@click.argument('list_id')
@click.argument('name')
def users_setlists_update(api_token, list_id, name):
    print(api_token.api.users_setlists_update(user_token=api_token.token,
                                    list_id=list_id,
                                    name=name))


@users.group(name='sets')
def users_sets():
    pass


@users_sets.command(name='create')
@pass_usersapi
@click.argument('user_token')
@click.argument('set_num')
def users_sets_create(api_token, set_num):
    print(api_token.api.users_sets_create(user_token=api_token.token,
                                set_num=set_num))


@users_sets.command(name='delete')
@pass_usersapi
@click.argument('user_token')
@click.argument('set_num')
def users_sets_delete(api_token, set_num):
    print(api_token.api.users_sets_delete(user_token=api_token.token, set_num=set_num))


@users_sets.command(name='list')
@pass_usersapi
@click.argument('user_token')
def users_sets_list(api_token):
    print(api_token.api.users_sets_list(user_token=api_token.token))


@users_sets.command(name='read')
@pass_usersapi
@click.argument('user_token')
@click.argument('set_num')
def users_sets_read(api_token, set_num):
    print(api_token.api.users_sets_read(user_token=api_token.token, set_num=set_num))


@users_sets.group(name='sync')
def users_sets_sync():
    pass


@users_sets_sync.command(name='create')
@pass_usersapi
@click.argument('user_token')
@click.argument('set_num')
def users_sets_sync_create(api_token, set_num):
    print(api_token.api.users_sets_sync_create(user_token=api_token.token, set_num=set_num))


@users_sets_sync.command(name='update')
@pass_usersapi
@pass_usertoken
@click.argument('user_token')
@click.argument('set_num')
def users_sets_update(api_token, set_num):
    print(api_token.api.users_sets_update(user_token=api_token.token, set_num=set_num))


@users.group(name='token')
def users_token():
    pass


@users_token.command(name='create')
@pass_usersapi
@click.argument('username')
@click.argument('password')
def users_token_create(api, username, password):
    print(api_token.api.users_token_create(username=username, password=password))


if __name__ == "__main__":
    main()
