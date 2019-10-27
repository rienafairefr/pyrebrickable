from mock import patch, Mock

from rebrickable.api import ApiException
from rebrickable.cli.main import main
from tests.cli.test_main import mocked_data


@patch('rebrickable.cli.utils.get_api_client', new=Mock())
@mocked_data({'api_key': 'api_key_value'})
def test_users_login_no_username(runner):
    result = runner.invoke(main, ['users', 'login'])
    # no username
    assert result.exception is not None


@mocked_data({'api_key': 'api_key_value'})
def test_users_login(runner):
    def write_data(data):
        assert data == {'api_key': 'api_key_value',
                        'default_user': 'username',
                        'users': {
                            'username': {
                                'token': 'user_token'
                            }
                        }}

    with patch('rebrickable.cli.login.create_auth', return_value='user_token'), \
         patch('rebrickable.cli.utils.write_data', side_effect=write_data):
        result = runner.invoke(main, ['login', 'username'])

        assert result.exception is None


@mocked_data({'api_key': 'api_key_value'})
def test_users_login_other(runner):
    def write_data(data):
        assert data == {'api_key': 'api_key_value',
                        'users': {
                            'username': {
                                'token': 'user_token'
                            }
                        }}

    with patch('rebrickable.cli.login.create_auth', return_value='user_token'), \
         patch('rebrickable.cli.users.write_data', side_effect=write_data):
        result = runner.invoke(main, ['login', 'username'])

        assert result.exception is None


@mocked_data({'api_key': 'api_key_value'})
def test_users_login_invalid_login(runner):
    def create_auth(users_api, username):
        raise ApiException()

    with patch('rebrickable.cli.login.create_auth', side_effect=create_auth):
        result = runner.invoke(main, ['login', 'username'])

    assert result.exception is not None