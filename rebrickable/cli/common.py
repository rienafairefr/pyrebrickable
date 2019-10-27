from functools import wraps

import click
import decorator
from click import get_current_context, Group


class State(object):
    def __init__(self, format=None, client=None, user_token=None,
                 list_id=None, part_num=None, color_id=None, set_num=None, api=None):
        self.format = format
        self.client = client

        self.api = api
        self.user_token = user_token
        self.list_id = list_id
        self.part_num = part_num
        self.color_id = color_id
        self.set_num = set_num


def oprint(obj):
    # print an object using the current configured output (json/yaml/py)
    get_current_context().find_object(State).format.output(obj)


def get_or_push(fun):
    @pass_state
    @click.pass_context
    @wraps(fun)
    def decorated(click_context, state, *args, **kwargs):
        for attr in kwargs:
            setattr(state, attr, kwargs[attr])
        try:
            current_obj = fun(*args, **kwargs)
        except:
            current_obj = fun(state, *args, **kwargs)
        if click_context.invoked_subcommand is None:
            oprint(current_obj)
        else:
            click_context.obj = current_obj

    return decorated


def object_print(fun):
    def object_print_decorator(fun, *args, **kwargs):
        obj = fun(*args, **kwargs)
        oprint(obj)

    return decorator.decorate(fun, object_print_decorator)


def add_typed_subcommands(type_):
    def add_fun(fun, attribute_name):
        @fun.command(name=attribute_name)
        @click.make_pass_decorator(type_)
        def type_cmd(obj):
            print(getattr(obj, attribute_name))

    def decorator(fun):
        for attribute_name, attribute_type in type_.openapi_types.items():
            add_fun(fun, attribute_name)

        setattr(fun, 'invoke_without_command', True)

        return fun

    return decorator


pass_state = click.make_pass_decorator(State)
