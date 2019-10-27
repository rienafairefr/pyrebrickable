import click
from click import prompt

from rebrickable.api import UsersApi, ApiException
from .utils import get_data, write_data, DATA_PATH, get_api_client


@click.command(name='login', help='login a certain user (store its user token)')
@click.argument('username', required=False, type=click.prompt)
def login(username=None):
    try:
        if username is None:
            username = prompt('Username')
        client = get_api_client()
        users_api = UsersApi(client)
        users_token = create_auth(users_api, username)
        data = get_data()
        data['default_user'] = username
        data.setdefault('users', {}).setdefault(username, {})['token'] = users_token
        write_data(data)

        print('OK, saved users token into %s' % DATA_PATH)
    except ApiException as e:
        print('Login failed, response was %s' % e.body)
        raise click.Abort()


def create_auth(users_api, username):
    password = prompt('Password (not stored)', hide_input=True)
    return users_api.users_token_create(username, password).user_token
