import json

import mock

from rebrickable_cli.cli.common import get_user_context
from rebrickable_cli.cli.main import get_api_client
from rebrickable_cli.utils import get_data, write_data


def test_data():
    api_key = 'nice_api_key'
    users_token = 'nice_users_token'
    read_data_dict = {
        'api_key': api_key,
        'users': {
            '%%default%%': {
                'token': users_token
            }
        }
    }

    m = mock.mock_open(read_data=json.dumps(read_data_dict))

    with mock.patch('{}.open'.format('rebrickable_cli.utils'), m, create=True):
        data = get_data()
        assert data == read_data_dict

        api_client = get_api_client()

        assert api_client.configuration.api_key['Authorization'] == api_key
        assert api_client.configuration.api_key_prefix['Authorization'] == 'key'

        users_context = get_user_context(api_client)

        assert users_context.user_token == users_token
        assert users_context.api.api_client == api_client


def test_invalid_data():
    m = mock.mock_open(read_data='bla')

    with mock.patch('{}.open'.format('rebrickable_cli.utils'), m, create=True):
        data = get_data()
        assert data == {}


def test_write_data(tmpdir):
    data = {'api_key': 'new_api_key'}

    p = tmpdir.join('.rebrickable').strpath

    write_data(data, p)

    data2 = get_data(p)

    assert data2.items() == data.items()
