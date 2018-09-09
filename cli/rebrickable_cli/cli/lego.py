import click

from rebrickable_api import LegoApi, Part, PartColorsElement, Color, Element, Moc, PartCategory, Set, Theme
from rebrickable_cli.cli.common import add_typed_subcommands, pass_state, get_or_push_context_obj, \
    object_print, oprint


@click.group(help='LEGO data (parts, sets, themes, etc.)')
@pass_state
def lego(ctx):
    ctx.api = LegoApi(ctx.client)


@lego.command('parts')
@pass_state
@object_print
def lego_parts(ctx):
    return ctx.api.lego_parts_list()


@add_typed_subcommands(Part)
@lego.group('part')
@pass_state
@get_or_push_context_obj(click.argument('part_num'))
def lego_part(ctx, part_num):
    return ctx.api.lego_parts_read(part_num=ctx.part_num)


@lego_part.command('colors')
@pass_state
@object_print
def lego_part_colors(ctx):
    return ctx.api.lego_parts_colors_list(part_num=ctx.part_num)


@add_typed_subcommands(PartColorsElement)
@lego_part.group('color')
@pass_state
@get_or_push_context_obj(click.argument('color_id', type=int))
def lego_part_color(ctx, color_id):
    return ctx.api.lego_parts_colors_read(color_id=color_id, part_num=ctx.part_num)


@lego_part_color.command('sets')
@pass_state
@object_print
def lego_part_color_sets(ctx):
    return ctx.api.lego_parts_colors_sets_list(color_id=ctx.color_id, part_num=ctx.part_num)


@lego.command('colors')
@pass_state
@object_print
def lego_colors(ctx):
    return ctx.api.lego_colors_list()


@add_typed_subcommands(Color)
@lego.group('color')
@pass_state
@get_or_push_context_obj(click.argument('color_id', type=int))
def lego_color(ctx, color_id):
    return ctx.api.lego_colors_read(id=color_id)


@add_typed_subcommands(Element)
@lego.group('element')
@pass_state
@get_or_push_context_obj(click.argument('element_id'))
def lego_element(ctx, element_id):
    return ctx.api.lego_elements_read(element_id=element_id)


@add_typed_subcommands(Moc)
@lego.group('moc')
@pass_state
@get_or_push_context_obj(click.argument('set_num'))
def lego_moc(ctx, set_num):
    return ctx.api.lego_mocs_read(set_num=set_num)


@lego_moc.command('parts')
@pass_state
@object_print
def lego_moc_parts(ctx):
    return ctx.api.lego_mocs_parts_list(set_num=ctx.set_num)


@lego.command('part_categories')
@pass_state
@object_print
def lego_part_categories(ctx):
    return ctx.api.lego_part_categories_list()


@add_typed_subcommands(PartCategory)
@lego.group('part_category')
@pass_state
@get_or_push_context_obj(click.argument('id', type=int))
def lego_part_category(ctx, id):
    return ctx.api.lego_part_categories_read(id=id)


@lego.command('sets')
@pass_state
def lego_sets(ctx):
    oprint(ctx.api.lego_sets_list())


@add_typed_subcommands(Set)
@lego.group('set')
@pass_state
@get_or_push_context_obj(click.argument('set_num'))
def lego_set(ctx, set_num):
    return ctx.api.lego_sets_read(set_num=set_num)


@lego_set.command('parts')
@pass_state
@object_print
def lego_set_parts(ctx):
    return ctx.api.lego_sets_parts_list(set_num=ctx.set_num)


@lego_set.command('alternates')
@pass_state
@object_print
def lego_set_alternates(ctx):
    return ctx.api.lego_sets_alternates_list(set_num=ctx.set_num)


@lego_set.command('sets')
@pass_state
@object_print
def lego_set_sets(ctx):
    return ctx.api.lego_sets_sets_list(set_num=ctx.set_num)


@lego.command('themes')
@pass_state
@object_print
def lego_themes(ctx):
    return ctx.api.lego_themes_list()


@add_typed_subcommands(Theme)
@lego.group('theme')
@pass_state
@get_or_push_context_obj(click.argument('theme_id'))
def lego_theme(ctx, theme_id):
    return ctx.api.lego_themes_read(id=theme_id)