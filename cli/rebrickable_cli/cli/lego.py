import click

from rebrickable_api import LegoApi, Part, PartColorsElement, Color, Element, Moc, PartCategory, Set, Theme
from rebrickable_cli.cli.common import pass_global, add_typed_subcommands, pass_legoapi, get_or_push_context_obj, \
    object_print, oprint


@click.group(help='LEGO data (parts, sets, themes, etc.)')
@pass_global
@click.pass_context
def lego(ctx, global_context):
    ctx.obj = LegoApi(global_context.client)


@lego.command('parts')
@pass_legoapi
@object_print
def lego_parts(api):
    return api.lego_parts_list()


@add_typed_subcommands(Part)
@lego.group('part')
@pass_legoapi
@click.argument('part_num')
@get_or_push_context_obj
def lego_part(api, part_num):
    return api.lego_parts_read(part_num=part_num)


@lego_part.command('colors')
@pass_legoapi
@click.pass_context
@object_print
def lego_part_colors(ctx, api):
    part = ctx.find_object(Part)
    return api.lego_parts_colors_list(part_num=part.part_num)


@add_typed_subcommands(PartColorsElement)
@lego_part.group('color')
@pass_legoapi
@click.pass_context
@click.argument('color_id', type=int)
@get_or_push_context_obj
def lego_part_color(ctx, api, color_id):
    part = ctx.find_object(Part)
    return api.lego_parts_colors_read(color_id=color_id, part_num=part.part_num)


@lego_part_color.command('sets')
@pass_legoapi
@click.pass_context
@object_print
def lego_part_color_sets(ctx, api):
    color = ctx.find_object(Color)
    part = ctx.find_object(Part)
    return api.lego_parts_colors_sets_list(color_id=color.id, part_num=part.part_num)


@lego.command('colors')
@pass_legoapi
@object_print
def lego_colors(api):
    return api.lego_colors_list()


@add_typed_subcommands(Color)
@lego.group('color')
@pass_legoapi
@click.argument('color_id', type=int)
@get_or_push_context_obj
def lego_color(api, color_id):
    return api.lego_colors_read(id=color_id)


@add_typed_subcommands(Element)
@lego.group('element')
@pass_legoapi
@click.argument('element_id')
@get_or_push_context_obj
def lego_element(api, element_id):
    return api.lego_elements_read(element_id=element_id)


@add_typed_subcommands(Moc)
@lego.group('moc')
@pass_legoapi
@click.argument('set_num')
@get_or_push_context_obj
def lego_moc(api, set_num):
    return api.lego_mocs_read(set_num=set_num)


@lego_moc.command('parts')
@pass_legoapi
@click.pass_context
@object_print
def lego_moc_parts(ctx, api):
    moc = ctx.find_object(Moc)
    return api.lego_mocs_parts_list(set_num=moc.set_num)


@lego.command('part_categories')
@pass_legoapi
@object_print
def lego_part_categories(api):
    return api.lego_part_categories_list()


@add_typed_subcommands(PartCategory)
@lego.group('part_category')
@pass_legoapi
@click.argument('id', type=int)
@object_print
def lego_part_category(api, id):
    return api.lego_part_categories_read(id=id)


@lego.command('sets')
@pass_legoapi
def lego_sets(api):
    oprint(api.lego_sets_list())


@add_typed_subcommands(Set)
@lego.group('set')
@pass_legoapi
@click.argument('set_num')
@get_or_push_context_obj
def lego_set(api, set_num):
    return api.lego_sets_read(set_num=set_num)


@lego_set.command('parts')
@pass_legoapi
@click.pass_context
@object_print
def lego_set_parts(ctx, api):
    set = ctx.find_object(Set)
    return api.lego_sets_parts_list(set_num=set.set_num)


@lego_set.command('alternates')
@pass_legoapi
@click.pass_context
@object_print
def lego_set_alternates(ctx, api):
    set = ctx.find_object(Set)
    return api.lego_sets_alternates_list(set_num=set.set_num)


@lego_set.command('sets')
@pass_legoapi
@click.pass_context
@object_print
def lego_set_sets(ctx, api):
    set = ctx.find_object(Set)
    return api.lego_sets_sets_list(set_num=set.set_num)


@lego.command('themes')
@pass_legoapi
@object_print
def lego_themes(api):
    return api.lego_themes_list()


@add_typed_subcommands(Theme)
@lego.group('theme')
@pass_legoapi
@click.argument('theme_id')
@get_or_push_context_obj
def lego_theme(api, theme_id):
    return api.lego_themes_read(id=theme_id)