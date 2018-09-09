import json

import click

from rebrickable_api import PartList, Profile, SetList, SetListSet, Build, UsersApi
from rebrickable_api.rest import ApiException
from rebrickable_cli.cli.common import add_typed_subcommands, pass_state, \
    get_or_push_context_obj, object_print, get_user_token


@click.group(help='user data (sets, parts lists, set lists, etc.)')
@click.option('--username', '-u', required=False, default='%%default%%')
@pass_state
def user(ctx, username):
    try:
        ctx.api = UsersApi(ctx.client)
        ctx.user_token = get_user_token(username)
    except (IOError, KeyError, ValueError):
        print('Please login using: \nrebrickable users login [-u username]')
        raise click.Abort()


@add_typed_subcommands(PartList)
@user.group('partlist')
@pass_state
@get_or_push_context_obj(click.argument('list_id', type=int))
def user_partlist(ctx, list_id):
    return ctx.api.users_partlists_read(user_token=ctx.user_token, list_id=list_id)


@user_partlist.command('delete')
@pass_state
@object_print
def user_partlist_delete(ctx):
    return ctx.api.users_partlists_delete(user_token=ctx.user_token,
                                          list_id=ctx.list_id)


@user_partlist.command('partial_update')
@pass_state
@click.option('--name', expose_value=False)
@click.option('--is_buildable', expose_value=False, type=bool)
@click.option('--num_parts', expose_value=False, type=int)
@object_print
def user_partlist_partial_update(ctx, *args, **kwargs):
    return ctx.api.users_partlists_partial_update(user_token=ctx.user_token,
                                                  list_id=ctx.list_id, *args, **kwargs)


@user_partlist.group('parts')
def user_partlist_parts():
    pass


@user_partlist_parts.command('create')
@pass_state
@click.argument('part_num')
@click.argument('quantity', type=int)
@click.argument('color_id', type=int)
@object_print
def user_partlist_parts_create(ctx, part_num, quantity, color_id):
    return ctx.api.users_partlists_parts_create(user_token=ctx.user_token,
                                                list_id=ctx.list_id,
                                                part_num=part_num,
                                                quantity=quantity,
                                                color_id=color_id)


@user_partlist_parts.command('delete')
@pass_state
@click.argument('color_id', type=int)
@click.argument('part_num')
@object_print
def user_partlist_parts_delete(ctx, color_id, part_num):
    return ctx.api.users_partlists_parts_delete(user_token=ctx.user_token,
                                                color_id=color_id,
                                                list_id=ctx.list_id,
                                                part_num=part_num)


@user_partlist_parts.command('list')
@pass_state
@object_print
def user_partlist_parts_list(ctx):
    return ctx.api.users_partlists_parts_list(user_token=ctx.user_token, list_id=ctx.list_id)


@add_typed_subcommands(PartList)
@user_partlist.group('part')
@pass_state
@get_or_push_context_obj(click.argument('part_num'), click.argument('color_id', type=int))
def user_partlist_part(ctx, color_id, part_num):
    return ctx.api.users_partlists_parts_read(user_token=ctx.user_token, color_id=color_id,
                                              list_id=ctx.list_id,
                                              part_num=part_num)


@user_partlist_part.command('update')
@pass_state
@click.argument('quantity', type=int)
@object_print
def user_partlist_part_update(ctx, quantity):
    return ctx.api.users_partlists_parts_update(user_token=ctx.user_token, color_id=ctx.color_id,
                                                list_id=ctx.list_id, part_num=ctx.part_num,
                                                quantity=quantity)


@user_partlist.command('update')
@pass_state
@click.argument('name')
@object_print
def user_partlist_update(ctx, name):
    return ctx.api.users_partlists_update(user_token=ctx.user_token, list_id=ctx.list_id, name=name)


@user.command('parts')
@pass_state
@object_print
def user_parts(ctx):
    return ctx.api.users_parts_list(user_token=ctx.user_token)


@add_typed_subcommands(Profile)
@user.group('profile', invoke_without_command=True)
@pass_state
@object_print
def user_profile(ctx):
    return ctx.api.users_profile_list(user_token=ctx.user_token)


@user.group('setlists')
def user_setlists():
    pass


@user_setlists.command('list')
@pass_state
@object_print
def user_setlists_list(ctx):
    return ctx.api.users_setlists_list(user_token=ctx.user_token)


@add_typed_subcommands(SetList)
@user.group('setlist')
@pass_state
@get_or_push_context_obj(click.argument('list_id', type=int))
def user_setlist(ctx, list_id):
    return ctx.api.users_setlists_read(user_token=ctx.user_token, list_id=list_id)


@user_setlists.command('create')
@pass_state
@click.argument('name')
@object_print
def user_setlists_create(ctx, name):
    return ctx.api.users_setlists_create(user_token=ctx.user_token, name=name)


@user_setlist.command('delete')
@pass_state
@object_print
def user_setlist_delete(ctx):
    return ctx.api.users_setlists_delete(user_token=ctx.user_token, list_id=ctx.list_id)


@user_setlist.group('partial')
def user_setlists_partial():
    pass


@user_setlist.command('update')
@pass_state
@object_print
def user_setlist_partial_update(ctx):
    return ctx.api.users_setlists_partial_update(user_token=ctx.user_token, list_id=ctx.list_id)


@user_setlist.group('sets')
def user_setlist_sets():
    pass


@user_setlist_sets.command('list')
@pass_state
@object_print
def user_setlist_sets_list(ctx):
    return ctx.api.users_setlists_sets_list(user_token=ctx.user_token, list_id=ctx.list_id)


@add_typed_subcommands(SetListSet)
@user_setlist.group('set')
@pass_state
@get_or_push_context_obj(click.argument('set_num'))
def user_setlist_set(ctx, set_num):
    return ctx.api.users_setlists_sets_read(user_token=ctx.user_token, list_id=ctx.list_id, set_num=set_num)


@user_setlist_sets.command('create')
@pass_state
@click.argument('set_num')
@object_print
def user_setlist_sets_create(ctx, set_num):
    return ctx.api.users_setlists_sets_create(user_token=ctx.user_token,
                                              list_id=ctx.list_id,
                                              set_num=set_num)


@user_setlist_sets.command('delete')
@pass_state
@object_print
def user_setlist_set_delete(ctx):
    return ctx.api.users_setlists_sets_delete(user_token=ctx.user_token,
                                              list_id=ctx.list_id,
                                              set_num=ctx.set_num)


@user_setlist_sets.group()
def user_setlists_sets_partial():
    pass


@user_setlists_sets_partial.command('update')
@pass_state
@click.argument('set_num')
@object_print
def user_setlist_set_partial_update(ctx, set_num):
    return ctx.api.users_setlists_sets_partial_update(user_token=ctx.user_token,
                                                      list_id=ctx.list_id,
                                                      set_num=set_num)


@user_setlist_sets.command('update')
@pass_state
@object_print
def user_setlist_set_update(ctx):
    return ctx.api.users_setlists_sets_update(user_token=ctx.user_token,
                                              list_id=ctx.list_id,
                                              set_num=ctx.set_num)


@user_setlist.command('update')
@pass_state
@click.argument('name')
@object_print
def user_setlist_update(ctx, name):
    return ctx.api.users_setlists_update(user_token=ctx.user_token,
                                         list_id=ctx.list_id,
                                         name=name)


@user.group('sets')
def user_sets():
    pass


@user_sets.command('list')
@pass_state
@click.option('--set_num', expose_value=False)
@click.option('--theme_id', expose_value=False)
@click.option('--min_year', expose_value=False)
@click.option('--max_year', expose_value=False)
@click.option('--min_parts', expose_value=False)
@click.option('--max_parts', expose_value=False)
@click.option('--search', expose_value=False)
@object_print
def user_sets_list(ctx, *args, **kwargs):
    return ctx.api.users_sets_list(user_token=ctx.user_token, *args, **kwargs)


@add_typed_subcommands(SetListSet)
@user.group('set')
@pass_state
@get_or_push_context_obj(click.argument('set_num'))
def user_set(ctx, set_num):
    return ctx.api.users_sets_read(user_token=ctx.user_token, set_num=set_num)


@user_sets.command('create')
@pass_state
@click.argument('set_num')
@object_print
def user_sets_create(ctx, set_num):
    try:
        return ctx.api.users_sets_create(user_token=ctx.user_token,
                                         set_num=set_num)
    except ApiException as e:
        print('an error occured: %s, %s, %s' % (e.status, e.body, e.message))


@user_set.command('delete')
@pass_state
@object_print
def user_set_delete(ctx):
    try:
        return ctx.api.users_sets_delete(user_token=ctx.user_token, set_num=ctx.set_num)
    except ApiException as e:
        print('an error occured: %s, %s, %s' % (e.status, e.body, e.message))


@user_sets.command('sync')
@pass_state
@click.option('--file', '-f', type=click.File('r'), default='-')
@object_print
def user_sets_sync(ctx, file):
    # Assume the file contains a json list of SetListSet
    file_content = file.read()
    array_of_set_list_sets = json.loads(file_content)
    return ctx.api.users_sets_sync_create(
        user_token=ctx.user_token, array_of_set_list_sets=array_of_set_list_sets)


@user_set.command('sync')
@pass_state
@object_print
def user_set_update(ctx):
    return ctx.api.users_sets_update(
        user_token=ctx.user_token, set_num=ctx.set_num)


@user.command('allparts')
@pass_state
@object_print
def user_allparts(ctx):
    return ctx.api.users_allparts_list(user_token=ctx.user_token)


@add_typed_subcommands(Build)
@user.group('build')
@pass_state
@get_or_push_context_obj(click.argument('set_num'))
def user_build(ctx, set_num):
    return ctx.api.users_build_read(user_token=ctx.user_token,
                                    set_num=set_num)


@user.group('lost_parts')
def user_lost_parts():
    pass


@user_lost_parts.command('create')
@pass_state
@click.argument('inv_part_id', type=int)
@object_print
def user_lost_parts_create(ctx, inv_part_id):
    return ctx.api.users_lost_parts_create(user_token=ctx.user_token, inv_part_id=inv_part_id)


@user_lost_parts.command('delete')
@pass_state
@click.argument('lost_part_id', type=int)
@object_print
def user_lost_parts_delete(ctx, lost_part_id):
    return ctx.api.users_lost_parts_delete(user_token=ctx.user_token, id=lost_part_id)


@user_lost_parts.command('list')
@pass_state
@object_print
def user_lost_parts_list(ctx):
    return ctx.api.users_lost_parts_list(user_token=ctx.user_token)


@user.group('partlists')
def user_partlists():
    pass


@user_partlists.command('create')
@pass_state
@click.argument('name')
@object_print
def user_partlists_create(ctx, name):
    return ctx.api.users_partlists_create(user_token=ctx.user_token,
                                          name=name)


@user_partlists.command('list')
@pass_state
@object_print
def user_partlists_list(ctx):
    return ctx.api.users_partlists_list(user_token=ctx.user_token)
