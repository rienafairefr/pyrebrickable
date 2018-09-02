# -*- coding: utf-8 -*-

"""Console script for pyrebrickable."""
from getpass import getpass

import click
from click import Abort, ClickException
from six.moves import input

from rebrickable_api import ApiClient, Configuration, Color, Element, Moc, PartCategory, Part, PartColorsElement, Set, \
    Theme, Badge, Build, PartListPart, PartList, Profile, SetList, SetListSet
from rebrickable_api import LegoApi, UsersApi
from rebrickable_api.rest import ApiException
from rebrickable_cli.utils import update_data, get_data, DATA_PATH


class UsersContext(object):
    def __init__(self, api, token):
        self.api = api
        self.token = token
        self.setlist = None


pass_client = click.make_pass_decorator(ApiClient)
pass_legoapi = click.make_pass_decorator(LegoApi)
pass_userscontext = click.make_pass_decorator(UsersContext)
pass_usersapi = click.make_pass_decorator(UsersApi)

def GET(ctx, fun):
    current_obj = fun()
    if ctx.invoked_subcommand is None:
        print(current_obj)
    else:
        ctx.obj = current_obj


class TypedResult(click.Group):
    def __init__(self, *args, **kwargs):
        self.type_ = kwargs.pop('type', None)
        super(TypedResult, self).__init__(*args, **kwargs)
        for attribute_name, attribute_type in self.type_.openapi_types.items():
            def get_type_cmd(this):
                @click.command()
                @click.make_pass_decorator(this.type_)
                def type_cmd(obj):
                    print(getattr(obj, attribute_name))

                return type_cmd

            self.add_command(get_type_cmd(self), name=attribute_name)


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


@lego.group(cls=TypedResult, type=Color, invoke_without_command=True, name='color')
@pass_legoapi
@click.pass_context
@click.argument('id')
def lego_colors_read(ctx, api, id):
    GET(ctx, lambda: api.lego_colors_read(id=id))


@lego.command(cls=TypedResult, type=Element, invoke_without_command=True, name='element')
@pass_legoapi
@click.pass_context
@click.argument('element_id')
def lego_elements_read(ctx, api, element_id):
    GET(ctx, lambda: api.lego_elements_read(element_id=element_id))


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


@lego_mocs.command(cls=TypedResult, type=Moc, invoke_without_command=True, name='read')
@pass_legoapi
@click.pass_context
@click.argument('set_num')
def lego_mocs_read(ctx, api, set_num):
    GET(ctx, lambda: api.lego_mocs_read(set_num=set_num))


@lego.command(name='part_categories')
@pass_legoapi
def lego_part_categories_list(api):
    print(api.lego_part_categories_list())


@lego.command(cls=TypedResult, type=PartCategory, invoke_without_command=True, name='part_category')
@pass_legoapi
@click.pass_context
@click.argument('id')
def lego_part_categories_read(ctx, api, id):
    GET(ctx, lambda: api.lego_part_categories_read(id=id))


@lego_parts_colors.command(name='list')
@pass_legoapi
@click.argument('part_num')
def lego_parts_colors_list(api, part_num):
    print(api.lego_parts_colors_list(part_num=part_num))


@lego_parts_colors.group(cls=TypedResult, type=PartColorsElement, invoke_without_command=True, name='read')
@pass_legoapi
@click.pass_context
@click.argument('color_id')
@click.argument('part_num')
def lego_parts_colors_read(ctx, api, color_id, part_num):
    GET(ctx, lambda: api.lego_parts_colors_read(color_id=color_id, part_num=part_num))


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


@lego.command(cls=TypedResult, type=Part, invoke_without_command=True, name='part')
@pass_legoapi
@click.pass_context
@click.argument('part_num')
def lego_parts_read(ctx, api, part_num):
    GET(ctx, lambda: api.lego_parts_read(part_num=part_num))


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


@lego.command(cls=TypedResult, type=Set, invoke_without_command=True, name='set')
@pass_legoapi
@click.pass_context
@click.argument('set_num')
def lego_sets_read(ctx, api, set_num):
    GET(ctx, lambda: api.lego_sets_read(set_num=set_num))


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


@lego.command(cls=TypedResult, type=Theme, invoke_without_command=True, name='theme')
@pass_legoapi
@click.pass_context
@click.argument('id')
def lego_themes_read(ctx, api, id):
    GET(ctx, lambda: api.lego_themes_read(id=id))


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


@users.command(cls=TypedResult, type=Badge, invoke_without_command=True, name='badge')
@pass_userscontext
@click.pass_context
@click.argument('id')
def users_badges_read(ctx, users_context, id):
    GET(ctx, lambda: users_context.api.users_badges_read(id=id))


@users.command(cls=TypedResult, type=Build, invoke_without_command=True, name='build')
@pass_userscontext
@click.pass_context
@click.argument('set_num')
def users_build_read(ctx, users_context, set_num):
    GET(ctx, lambda: users_context.api.users_build_read(user_token=users_context.token,
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


@users_partlists_parts.command(cls=TypedResult, type=PartListPart, invoke_without_command=True, name='read')
@pass_userscontext
@click.pass_context
@click.argument('color_id')
@click.argument('list_id')
@click.argument('part_num')
def users_partlists_parts_read(ctx, users_context, color_id, list_id, part_num):
    GET(ctx, lambda: users_context.api.users_partlists_parts_read(user_token=users_context.token, color_id=color_id,
                                                                  list_id=list_id,
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


@users_partlists.command(cls=TypedResult, type=PartList, invoke_without_command=True, name='read')
@pass_userscontext
@click.pass_context
@click.argument('list_id')
def users_partlists_read(ctx, users_context, list_id):
    GET(ctx, lambda: users_context.api.users_partlists_read(users_context.token, list_id=list_id))


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


@users.group(cls=TypedResult, type=Profile, invoke_without_command=True, name='profile')
@pass_userscontext
@click.pass_context
def users_profile_get(ctx, users_context):
    GET(ctx, lambda: users_context.api.users_profile_list(user_token=users_context.token))


@users.group('setlists', invoke_without_command=True)
@pass_userscontext
@click.pass_context
def users_setlists(ctx, users_context):
    if ctx.invoked_subcommand is None:
        print(users_context.api.users_setlists_list(user_token=users_context.token))


@users.group('setlist', cls=TypedResult, type=SetList, invoke_without_command=True)
@click.argument('list_id')
@pass_userscontext
@click.pass_context
def users_setlist(ctx, users_context, list_id):
    setlist = users_context.api.users_setlists_read(user_token=users_context.token, list_id=list_id)
    ctx.obj = setlist
    if ctx.invoked_subcommand is None:
        GET(ctx, lambda: users_context.api.users_setlists_read(user_token=users_context.token, list_id=setlist.id))


@users_setlists.command(name='create')
@pass_userscontext
@click.argument('name')
def users_setlists_create(users_context, name):
    print(users_context.api.users_setlists_create(user_token=users_context.token, name=name))


def setlist_command(fun):
    @pass_userscontext
    def new_fun(users_context, *args, **kwargs):
        setlist = users_context.setlist
        if setlist is not None:
            fun(*args, **kwargs)
        else:
            raise ClickException('need a list_id !')
    return new_fun


@users_setlist.command(name='delete')
@pass_userscontext
@click.pass_context
def users_setlists_delete(ctx, users_context):
    setlist = ctx.find_object(SetList)
    print(users_context.api.users_setlists_delete(user_token=users_context.token, list_id=setlist.id))


@users_setlist.group(name='partial')
def users_setlists_partial():
    pass


@users_setlist.command(name='update')
@pass_userscontext
@click.pass_context
def users_setlists_partial_update(ctx, users_context):
    setlist = ctx.find_object(SetList)
    print(users_context.api.users_setlists_partial_update(user_token=users_context.token, list_id=setlist.id))


@users_setlist.group(name='sets', invoke_without_command=True)
@pass_userscontext
@click.pass_context
def users_setlists_sets(ctx, users_context):
    setlist = ctx.find_object(SetList)
    if ctx.invoked_subcommand is None:
        print(users_context.api.users_setlists_sets_list(user_token=users_context.token, list_id=setlist.id))


@users_setlist.group(name='set', cls=TypedResult, type=SetListSet, invoke_without_command=True)
@pass_userscontext
@click.pass_context
@click.argument('set_num')
def users_setlists_sets(ctx, users_context, set_num):
    setlist = ctx.find_object(SetList)
    if ctx.invoked_subcommand is None:
        setlistset = users_context.api.users_setlists_sets_read(user_token=users_context.token, list_id=setlist.id, set_num=set_num)
        ctx.obj = setlistset
        GET(ctx, lambda: setlistset)


@users_setlists_sets.command(name='create')
@pass_userscontext
@click.pass_context
@click.argument('set_num')
def users_setlists_sets_create(ctx, users_context, set_num):
    setlist = ctx.find_object(SetList)
    print(users_context.api.users_setlists_sets_create(user_token=users_context.token,
                                                       list_id=setlist.id,
                                                       set_num=set_num))


@users_setlists_sets.command(name='delete')
@pass_userscontext
@click.pass_context

def users_setlists_sets_delete(ctx, users_context, set_num):
    setlist = ctx.find_object(SetList)
    print(users_context.api.users_setlists_sets_delete(user_token=users_context.token,
                                                       list_id=setlist.id,
                                                       set_num=set_num))


@users_setlists_sets.group()
def users_setlists_sets_partial():
    pass


@users_setlists_sets_partial.command(name='update')
@pass_userscontext
@click.pass_context
@click.argument('set_num')
def users_setlists_sets_partial_update(ctx, users_context, set_num):
    setlist = ctx.find_object(SetList)
    print(users_context.api.users_setlists_sets_partial_update(user_token=users_context.token,
                                                               list_id=setlist.id,
                                                               set_num=set_num))


@users_setlists_sets.command(cls=TypedResult, type=SetListSet, invoke_without_command=True, name='read')
@pass_userscontext
@click.pass_context
@click.argument('set_num')
def users_setlists_sets_read(ctx, users_context, set_num):
    setlist = ctx.find_object(SetList)
    GET(ctx, lambda: users_context.api.users_setlists_sets_read(user_token=users_context.token,
                                                                list_id=setlist.id,
                                                                set_num=set_num))


@users_setlists_sets.command(name='update')
@pass_userscontext
@click.pass_context
@click.argument('set_num')
def users_setlists_sets_update(ctx, users_context, set_num):
    setlist = ctx.find_object(SetList)
    print(users_context.api.users_setlists_sets_update(user_token=users_context.token,
                                                       list_id=setlist.id,
                                                       set_num=set_num))


@users_setlists.command(name='update')
@pass_userscontext
@click.pass_context
@click.argument('name')
def users_setlists_update(ctx, users_context, name):
    setlist = ctx.find_object(SetList)
    print(users_context.api.users_setlists_update(user_token=users_context.token,
                                                  list_id=setlist.id,
                                                  name=name))


@users.group(name='sets', invoke_without_command=True)
@pass_userscontext
@click.pass_context
@click.option('--set_num', expose_value=False)
@click.option('--theme_id', expose_value=False)
@click.option('--min_year', expose_value=False)
@click.option('--max_year', expose_value=False)
@click.option('--min_parts', expose_value=False)
@click.option('--max_parts', expose_value=False)
@click.option('--search', expose_value=False)
def users_sets(ctx, users_context, *args, **kwargs):
    if ctx.invoked_subcommand is None:
        print(users_context.api.users_sets_list(users_context.token, *args, **kwargs))


@users.group(name='set', cls=TypedResult, type=SetListSet, invoke_without_command=True)
@pass_userscontext
@click.pass_context
@click.argument('set_num')
def users_set(ctx, users_context, set_num):
    set = users_context.api.users_sets_read(user_token=users_context.token, set_num=set_num)
    ctx.obj = set
    if ctx.invoked_subcommand is None:
        GET(ctx, lambda: set)


@users_sets.command(name='create')
@pass_userscontext
@click.argument('set_num')
def users_sets_create(users_context, set_num):
    try:
        print(users_context.api.users_sets_create(user_token=users_context.token,
                                              set_num=set_num))
    except ApiException, e:
        print('an error occured: %s, %s, %s' % (e.status, e.body, e.message))


@users_set.command(name='delete')
@pass_userscontext
@click.pass_context
def users_sets_delete(ctx, users_context):
    setlistset = ctx.find_object(SetList)
    print(users_context.api.users_sets_delete(user_token=users_context.token, set_num=set_num))


@users_sets.command(name='list')
@pass_userscontext
def users_sets_list(users_context):
    print(users_context.api.users_sets_list(user_token=users_context.token))


@users_sets.command(cls=TypedResult, type=SetListSet, invoke_without_command=True, name='read')
@pass_userscontext
@click.pass_context
@click.argument('set_num')
def users_sets_read(ctx, users_context, set_num):
    GET(ctx, lambda: users_context.api.users_sets_read(user_token=users_context.token, set_num=set_num))


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
