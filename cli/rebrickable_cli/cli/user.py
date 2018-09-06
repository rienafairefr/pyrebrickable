import json

import click

from rebrickable_api import PartList, PartListPart, Profile, SetList, SetListSet, Set, Build
from rebrickable_api.rest import ApiException
from rebrickable_cli.cli.common import pass_global, get_user_context, add_typed_subcommands, pass_usercontext, \
    get_or_push_context_obj, object_print


@click.group(help='user data (sets, parts lists, set lists, etc.)')
@click.option('--username', '-u', required=False, default='%%default%%')
@pass_global
@click.pass_context
def user(ctx, global_context, username):
    try:
        ctx.obj = get_user_context(global_context.client, username)
    except (IOError, KeyError, ValueError):
        print('Please login using: \nrebrickable users login [-u username]')
        raise click.Abort()


@add_typed_subcommands(PartList)
@user.group('partlist')
@click.argument('list_id', type=int)
@pass_usercontext
@get_or_push_context_obj
def user_partlist(user_context, list_id):
    return user_context.api.users_partlists_read(user_token=user_context.token, list_id=list_id)


@user_partlist.command('delete')
@pass_usercontext
@click.pass_context
@object_print
def user_partlist_delete(ctx, user_context):
    partlist = ctx.find_object(PartList)
    return user_context.api.users_partlists_delete(user_token=user_context.token,
                                                   list_id=partlist.id)


@user_partlist.command('partial_update')
@pass_usercontext
@click.pass_context
@click.option('--name', expose_value=False)
@click.option('--is_buildable', expose_value=False, type=bool)
@click.option('--num_parts', expose_value=False, type=int)
@object_print
def user_partlist_partial_update(ctx, user_context, *args, **kwargs):
    partlist = ctx.find_object(PartList)
    return user_context.api.users_partlists_partial_update(user_token=user_context.token,
                                                           list_id=partlist.id, *args, **kwargs)


@user_partlist.group('parts')
def user_partlist_parts():
    pass


@user_partlist_parts.command('create')
@pass_usercontext
@click.pass_context
@click.argument('part_num')
@click.argument('quantity', type=int)
@click.argument('color_id', type=int)
@object_print
def user_partlist_parts_create(ctx, user_context, part_num, quantity, color_id):
    partlist = ctx.find_object(PartList)
    return user_context.api.users_partlists_parts_create(user_token=user_context.token,
                                                         list_id=partlist.id,
                                                         part_num=part_num,
                                                         quantity=quantity,
                                                         color_id=color_id)


@user_partlist_parts.command('delete')
@pass_usercontext
@click.pass_context
@click.argument('color_id', type=int)
@click.argument('part_num')
@object_print
def user_partlist_parts_delete(ctx, user_context, color_id, part_num):
    partlist = ctx.find_object(PartList)
    return user_context.api.users_partlists_parts_delete(user_token=user_context.token,
                                                         color_id=color_id,
                                                         list_id=partlist.id,
                                                         part_num=part_num)


@user_partlist_parts.command('list')
@pass_usercontext
@click.pass_context
@object_print
def user_partlist_parts_list(ctx, user_context):
    partlist = ctx.find_object(PartList)
    return user_context.api.users_partlists_parts_list(user_token=user_context.token, list_id=partlist.id)


@add_typed_subcommands(PartList)
@user_partlist.group('part')
@pass_usercontext
@click.pass_context
@click.argument('color_id', type=int)
@click.argument('part_num')
@get_or_push_context_obj
def user_partlist_part(ctx, user_context, color_id, part_num):
    partlist = ctx.find_object(PartList)
    return user_context.api.users_partlists_parts_read(user_token=user_context.token, color_id=color_id,
                                                       list_id=partlist.id,
                                                       part_num=part_num)


@user_partlist_part.command('update')
@pass_usercontext
@click.pass_context
@click.argument('quantity', type=int)
@object_print
def user_partlist_part_update(ctx, user_context, quantity):
    partlist = ctx.find_object(PartList)
    partlist_part = ctx.find_object(PartListPart)
    return user_context.api.users_partlists_parts_update(user_token=user_context.token, color_id=partlist_part.color.id,
                                                         list_id=partlist.id, part_num=partlist_part.part.part_num,
                                                         quantity=quantity)


@user_partlist.command('update')
@pass_usercontext
@click.pass_context
@click.argument('name')
@object_print
def user_partlist_update(ctx, user_context, name):
    partlist = ctx.find_object(PartList)
    return user_context.api.users_partlists_update(user_token=user_context.token, list_id=partlist.id, name=name)


@user.command('parts')
@pass_usercontext
@object_print
def user_parts(user_context):
    return user_context.api.users_parts_list(user_token=user_context.token)


@add_typed_subcommands(Profile)
@user.group('profile', invoke_without_command=True)
@pass_usercontext
@get_or_push_context_obj
def user_profile(user_context):
    return user_context.api.users_profile_list(user_token=user_context.token)


@user.group('setlists')
def user_setlists():
    pass


@user_setlists.command('list')
@pass_usercontext
@object_print
def user_setlists_list(user_context):
    return user_context.api.users_setlists_list(user_token=user_context.token)


@add_typed_subcommands(SetList)
@user.group('setlist')
@click.argument('list_id', type=int)
@pass_usercontext
@get_or_push_context_obj
def user_setlist(user_context, list_id):
    return user_context.api.users_setlists_read(user_token=user_context.token, list_id=list_id)


@user_setlists.command('create')
@pass_usercontext
@click.argument('name')
@object_print
def user_setlists_create(user_context, name):
    return user_context.api.users_setlists_create(user_token=user_context.token, name=name)


@user_setlist.command('delete')
@pass_usercontext
@click.pass_context
@object_print
def user_setlist_delete(ctx, user_context):
    setlist = ctx.find_object(SetList)
    return user_context.api.users_setlists_delete(user_token=user_context.token, list_id=setlist.id)


@user_setlist.group('partial')
def user_setlists_partial():
    pass


@user_setlist.command('update')
@pass_usercontext
@click.pass_context
@object_print
def user_setlist_partial_update(ctx, user_context):
    setlist = ctx.find_object(SetList)
    return user_context.api.users_setlists_partial_update(user_token=user_context.token, list_id=setlist.id)


@user_setlist.group('sets')
@pass_usercontext
def user_setlist_sets(ctx, user_context):
    pass


@user_setlist_sets.command('list')
@pass_usercontext
@click.pass_context
@object_print
def user_setlist_sets_list(ctx, user_context):
    setlist = ctx.find_object(SetList)
    return user_context.api.users_setlists_sets_list(user_token=user_context.token, list_id=setlist.id)


@add_typed_subcommands(SetListSet)
@user_setlist.group('set')
@pass_usercontext
@click.pass_context
@click.argument('set_num')
@get_or_push_context_obj
def user_setlist_set(ctx, user_context, set_num):
    setlist = ctx.find_object(SetList)
    return user_context.api.users_setlists_sets_read(user_token=user_context.token, list_id=setlist.id, set_num=set_num)


@user_setlist_sets.command('create')
@pass_usercontext
@click.pass_context
@click.argument('set_num')
@object_print
def user_setlist_sets_create(ctx, user_context, set_num):
    setlist = ctx.find_object(SetList)
    return user_context.api.users_setlists_sets_create(user_token=user_context.token,
                                                       list_id=setlist.id,
                                                       set_num=set_num)


@user_setlist_sets.command('delete')
@pass_usercontext
@click.pass_context
@object_print
def user_setlist_set_delete(ctx, user_context):
    setlist = ctx.find_object(SetList)
    setlistset = ctx.find_object(SetListSet)
    set_num = setlistset.set.set_num if setlistset.set else setlistset.set_num
    return user_context.api.users_setlists_sets_delete(user_token=user_context.token,
                                                       list_id=setlist.id,
                                                       set_num=set_num)


@user_setlist_sets.group()
def user_setlists_sets_partial():
    pass


@user_setlists_sets_partial.command('update')
@pass_usercontext
@click.pass_context
@click.argument('set_num')
@object_print
def user_setlist_set_partial_update(ctx, user_context, set_num):
    setlist = ctx.find_object(SetList)
    return user_context.api.users_setlists_sets_partial_update(user_token=user_context.token,
                                                               list_id=setlist.id,
                                                               set_num=set_num)


@user_setlist_sets.command('update')
@pass_usercontext
@click.pass_context
@object_print
def user_setlist_set_update(ctx, user_context):
    setlist = ctx.find_object(SetList)
    setlistset = ctx.find_object(SetListSet)
    set_num = setlistset.set.set_num if setlistset.set else setlistset.set_num
    return user_context.api.users_setlists_sets_update(user_token=user_context.token,
                                                       list_id=setlist.id,
                                                       set_num=set_num)


@user_setlist.command('update')
@pass_usercontext
@click.pass_context
@click.argument('name')
@object_print
def user_setlist_update(ctx, user_context, name):
    setlist = ctx.find_object(SetList)
    return user_context.api.users_setlists_update(user_token=user_context.token,
                                                  list_id=setlist.id,
                                                  name=name)


@user.group('sets')
def user_sets():
    pass


@user_sets.command('list')
@pass_usercontext
@click.option('--set_num', expose_value=False)
@click.option('--theme_id', expose_value=False)
@click.option('--min_year', expose_value=False)
@click.option('--max_year', expose_value=False)
@click.option('--min_parts', expose_value=False)
@click.option('--max_parts', expose_value=False)
@click.option('--search', expose_value=False)
@object_print
def user_sets_list(user_context, *args, **kwargs):
    return user_context.api.users_sets_list(user_token=user_context.token, *args, **kwargs)


@add_typed_subcommands(SetListSet)
@user.group('set')
@pass_usercontext
@click.argument('set_num')
@get_or_push_context_obj
def user_set(user_context, set_num):
    return user_context.api.users_sets_read(user_token=user_context.token, set_num=set_num)


@user_sets.command('create')
@pass_usercontext
@click.argument('set_num')
@object_print
def user_sets_create(user_context, set_num):
    try:
        return user_context.api.users_sets_create(user_token=user_context.token,
                                                  set_num=set_num)
    except ApiException as e:
        print('an error occured: %s, %s, %s' % (e.status, e.body, e.message))


@user_set.command('delete')
@pass_usercontext
@click.pass_context
@object_print
def user_set_delete(ctx, user_context):
    set = ctx.find_object(Set)
    try:
        return user_context.api.users_sets_delete(user_token=user_context.token, set_num=set.set_num)
    except ApiException as e:
        print('an error occured: %s, %s, %s' % (e.status, e.body, e.message))


@user_sets.command('sync')
@pass_usercontext
@click.option('--file', '-f', type=click.File('r'), default='-')
@object_print
def user_sets_sync(user_context, file):
    # Assume the file contains a json list of SetListSet
    file_content = file.read()
    array_of_set_list_sets = json.loads(file_content)
    return user_context.api.users_sets_sync_create(
        user_token=user_context.token, array_of_set_list_sets=array_of_set_list_sets)


@user_set.command('sync')
@pass_usercontext
@click.pass_context
@object_print
def user_set_update(ctx, user_context):
    set = ctx.find_object(Set)
    return user_context.api.users_sets_update(
        user_token=user_context.token, set_num=set.set_num)


@user.command('allparts')
@pass_usercontext
@object_print
def user_allparts(user_context):
    return user_context.api.users_allparts_list(user_token=user_context.token)


@add_typed_subcommands(Build)
@user.group('build')
@pass_usercontext
@click.argument('set_num')
@get_or_push_context_obj
def user_build(user_context, set_num):
    return user_context.api.users_build_read(user_token=user_context.token,
                                             set_num=set_num)


@user.group('lost_parts')
def user_lost_parts():
    pass


@user_lost_parts.command('create')
@pass_usercontext
@click.argument('inv_part_id', type=int)
@object_print
def user_lost_parts_create(user_context, inv_part_id):
    return user_context.api.users_lost_parts_create(user_token=user_context.token, inv_part_id=inv_part_id)


@user_lost_parts.command('delete')
@pass_usercontext
@click.argument('lost_part_id', type=int)
@object_print
def user_lost_parts_delete(user_context, lost_part_id):
    return user_context.api.users_lost_parts_delete(user_token=user_context.token, id=lost_part_id)


@user_lost_parts.command('list')
@pass_usercontext
@object_print
def user_lost_parts_list(user_context):
    return user_context.api.users_lost_parts_list(user_token=user_context.token)


@user.group('partlists')
def user_partlists():
    pass


@user_partlists.command('create')
@pass_usercontext
@click.argument('name')
@object_print
def user_partlists_create(user_context, name):
    return user_context.api.users_partlists_create(user_token=user_context.token,
                                                   name=name)


@user_partlists.command('list')
@pass_usercontext
@object_print
def user_partlists_list(user_context):
    return user_context.api.users_partlists_list(user_token=user_context.token)