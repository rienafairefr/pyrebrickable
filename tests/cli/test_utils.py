import json

import mock

from rebrickable.cli.utils import get_data, write_data, get_api_client, get_user_token

api_key = 'nice_api_key'
user_token = 'user_token'
other_user_token = 'other_user_token'
read_data_dict = {
    'api_key': api_key,
    'default_user': 'username',
    'users': {
        'username': {
            'token': user_token
        },
        'other_username': {
            'token': other_user_token
        }
    }
}


def test_data():
    m = mock.mock_open(read_data=json.dumps(read_data_dict))

    with mock.patch('{}.open'.format('rebrickable.cli.utils'), m, create=True):
        data = get_data()
        assert data == read_data_dict

        api_client = get_api_client()

        assert api_client.configuration.api_key['Authorization'] == api_key
        assert api_client.configuration.api_key_prefix['Authorization'] == 'key'


def test_invalid_data():
    m = mock.mock_open(read_data='bla')

    with mock.patch('{}.open'.format('rebrickable.cli.utils'), m, create=True):
        data = get_data()
        assert data == {}


def test_write_data(tmpdir):
    data = {'api_key': 'new_api_key'}

    p = tmpdir.join('.rebrickable').strpath

    write_data(data, p)

    data2 = get_data(p)

    assert data2.items() == data.items()


@mock.patch('rebrickable.cli.utils.get_data', return_value=read_data_dict)
def test_get_user_token(mocked):
    assert get_user_token() == user_token
    assert get_user_token('other_username') == other_user_token
