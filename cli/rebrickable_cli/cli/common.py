from functools import wraps

import click
from click import get_current_context

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


def oprint(obj):
    # print an object using the current configured output (json/yaml/py)
    get_current_context().find_object(GlobalContext).format.output(obj)


class GlobalContext(object):
    def __init__(self, format, client):
        self.format = format
        self.client = client


def get_or_push_context_obj(*decorators):
    def decorator(fun):
        @click.pass_obj
        @click.pass_context
        @wraps(fun)
        def decorated(ctx, obj, *args, **kwargs):
            for attr in kwargs:
                setattr(obj, attr, kwargs[attr])
            try:
                current_obj = fun(obj, *args, **kwargs)
            except:
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


def get_user_context(client, username='%%default%%'):
    users_api = UsersApi(client)
    data = get_data()
    user_token = data['users'][username]['token']
    return UserContext(users_api, user_token)


pass_global = click.make_pass_decorator(GlobalContext)
pass_lego = click.make_pass_decorator(LegoContext)
pass_usercontext = click.make_pass_decorator(UserContext)
pass_usersapi = click.make_pass_decorator(UsersApi)