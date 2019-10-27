import click

from rebrickable.api import LegoApi, Part, PartColorsElement, Color, Element, Moc, PartCategory, Set, Theme
from .common import add_typed_subcommands, pass_state, \
    object_print, oprint, get_or_push


@click.group(help='LEGO data (parts, sets, themes, etc.)')
@pass_state
def lego(state):
    state.api = LegoApi(state.client)


@lego.command('parts')
@pass_state
@object_print
def lego_parts(state):
    return state.api.lego_parts_list()


@add_typed_subcommands(Part)
@lego.group('part')
@pass_state
@get_or_push
@click.argument('part_num')
def lego_part(state, part_num):
    return state.api.lego_parts_read(part_num=state.part_num)


@lego_part.command('colors')
@pass_state
@object_print
def lego_part_colors(state):
    return state.api.lego_parts_colors_list(part_num=state.part_num)


@add_typed_subcommands(PartColorsElement)
@lego_part.group('color')
@pass_state
@get_or_push
@click.argument('color_id', type=int)
def lego_part_color(state, color_id):
    return state.api.lego_parts_colors_read(color_id=color_id, part_num=state.part_num)


@lego_part_color.command('sets')
@pass_state
@object_print
def lego_part_color_sets(state):
    return state.api.lego_parts_colors_sets_list(color_id=state.color_id, part_num=state.part_num)


@lego.command('colors')
@pass_state
@object_print
def lego_colors(state):
    return state.api.lego_colors_list()


@add_typed_subcommands(Color)
@lego.group('color')
@pass_state
@get_or_push
@click.argument('color_id', type=int)
def lego_color(state, color_id):
    return state.api.lego_colors_read(id=color_id)


@add_typed_subcommands(Element)
@lego.group('element')
@pass_state
@get_or_push
@click.argument('element_id')
def lego_element(state, element_id):
    return state.api.lego_elements_read(element_id=element_id)


@add_typed_subcommands(Moc)
@lego.group('moc')
@pass_state
@get_or_push
@click.argument('set_num')
def lego_moc(state, set_num):
    return state.api.lego_mocs_read(set_num=set_num)


@lego_moc.command('parts')
@pass_state
@object_print
def lego_moc_parts(state):
    return state.api.lego_mocs_parts_list(set_num=state.set_num)


@lego.command('part_categories')
@pass_state
@object_print
def lego_part_categories(state):
    return state.api.lego_part_categories_list()


@add_typed_subcommands(PartCategory)
@lego.group('part_category')
@pass_state
@get_or_push
@click.argument('id', type=int)
def lego_part_category(state, id):
    return state.api.lego_part_categories_read(id=id)


@lego.command('sets')
@pass_state
def lego_sets(state):
    oprint(state.api.lego_sets_list())


@add_typed_subcommands(Set)
@lego.group('set')
@pass_state
@get_or_push
@click.argument('set_num')
def lego_set(state, set_num):
    return state.api.lego_sets_read(set_num=set_num)


@lego_set.command('parts')
@pass_state
@object_print
def lego_set_parts(state):
    return state.api.lego_sets_parts_list(set_num=state.set_num)


@lego_set.command('alternates')
@pass_state
@object_print
def lego_set_alternates(state):
    return state.api.lego_sets_alternates_list(set_num=state.set_num)


@lego_set.command('sets')
@pass_state
@object_print
def lego_set_sets(state):
    return state.api.lego_sets_sets_list(set_num=state.set_num)


@lego.command('themes')
@pass_state
@object_print
def lego_themes(state):
    return state.api.lego_themes_list()


@add_typed_subcommands(Theme)
@lego.group('theme')
@pass_state
@get_or_push
@click.argument('theme_id')
def lego_theme(state, theme_id):
    return state.api.lego_themes_read(id=theme_id)
