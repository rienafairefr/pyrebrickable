from functools import wraps

import click
from click import get_current_context

from rebrickable_api import UsersApi, LegoApi
from rebrickable_cli.utils import get_data


class UserContext(object):
    def __init__(self, api, token):
        self.api = api
        self.token = token
        self.setlist = None


def oprint(obj):
    # print an object using the current configured output (json/yaml/py)
    get_current_context().find_object(GlobalContext).format.output(obj)


class GlobalContext(object):
    def __init__(self, format, client):
        self.format = format
        self.client = client



def get_or_push_context_obj(fun):
    @click.pass_context
    @wraps(fun)
    def decorated(ctx, *args, **kwargs):
        try:
            current_obj = fun(ctx, *args, **kwargs)
        except:
            current_obj = fun(*args, **kwargs)
        if ctx.invoked_subcommand is None:
            oprint(current_obj)
        else:
            ctx.obj = current_obj
        return current_obj

    return decorated


def object_print(fun):
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
pass_legoapi = click.make_pass_decorator(LegoApi)
pass_usercontext = click.make_pass_decorator(UserContext)
pass_usersapi = click.make_pass_decorator(UsersApi)