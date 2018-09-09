from functools import wraps

import click
from click import get_current_context, Group

from rebrickable_api import UsersApi
from rebrickable_cli.utils import get_data


class LegoContext(object):
    def __init__(self, api=None, part_num=None, set_num=None, color_id=None):
        self.api = api
        self.part_num = part_num
        self.set_num = set_num
        self.color_id = color_id


class UserContext(object):
    def __init__(self, api=None, user_token=None, list_id=None, part_num=None, color_id=None, set_num=None):
        self.api = api
        self.user_token = user_token
        self.list_id = list_id
        self.part_num = part_num
        self.color_id = color_id
        self.set_num = set_num


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


def get_or_push_context_obj(*decorators):
    def decorator(fun):
        @click.pass_obj
        @click.pass_context
        @wraps(fun)
        def decorated(ctx, obj, *args, **kwargs):
            for attr in kwargs:
                setattr(obj, attr, kwargs[attr])
            current_obj = fun(*args, **kwargs)
            if ctx.invoked_subcommand is None:
                oprint(current_obj)

        current = decorated
        for dec in decorators:
            current = dec(current)

        return  current
    return decorator


def object_print(fun):
    @wraps(fun)
    def decorated(*args, **kwargs):
        obj = fun(*args, **kwargs)
        oprint(obj)

    return decorated


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


def get_user_token(username='%%default%%'):
    data = get_data()
    return data['users'][username]['token']


pass_state = click.make_pass_decorator(State)


class StateGroup(Group):
    def group(self, *args, **kwargs):
        def decorated(fun):
            return pass_state(fun)
        return super(StateGroup, self).group(*args, **kwargs)(decorated)

    def command(self, *args, **kwargs):
        def decorated(fun):
            return pass_state(fun)
        return super(StateGroup, self).command(*args, **kwargs)(decorated)