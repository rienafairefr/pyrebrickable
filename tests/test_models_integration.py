import json
from pprint import pprint

import pytest
import six
from jsondiff import diff

from rebrickable_api import LegoApi, ApiClient
from rebrickable_cli.cli.common import get_user_context
from rebrickable_cli.cli.main import get_api_client

"""
assumes a working authentication 
and that the data doesn't change much
"""


@pytest.fixture(scope='module')
def api_client():
    return get_api_client()


@pytest.fixture
def lego_api(api_client):
    return LegoApi(api_client)


@pytest.fixture
def user_context(api_client):
    return get_user_context(api_client)


def get_id(element):
    if callable(element):
        return element.__name__
    return str(element)


def remove_nulls(d):
    return {k: remove_nulls(v) if isinstance(v, dict) else v for k, v in six.iteritems(d) if v is not None}


@pytest.mark.parametrize(['func', 'kwargs'], [
    ('lego_colors_read', dict(id=7)),
    ('lego_elements_read', dict(element_id=4245295)),
    ('lego_mocs_read', dict(set_num='MOC-5634')),
    ('lego_part_categories_read', dict(id=42)),
    ('lego_parts_colors_read', dict(color_id=4, part_num='3004')),
    ('lego_parts_read', dict(part_num='3004')),
    ('lego_parts_read', dict(part_num='4070')),
    ('lego_sets_read', dict(set_num='75192-1')),
    ('lego_sets_read', dict(set_num='31027-1')),
    ('lego_themes_read', dict(id=99)),
], ids=get_id)
@pytest.mark.integration
def test_objects_attributes(func, kwargs, lego_api, api_client):
    func = getattr(lego_api, func)
    do_test(func, kwargs, api_client)


@pytest.mark.parametrize(['func', 'kwargs'], [
    ('users_build_read', dict(set_num='75192-1')),
    ('users_partlists_parts_read', dict(list_id=40476, color_id=1, part_num='3298p61')), # user partlist 40476 part 1 3298p61
    ('users_partlists_read', dict(list_id=40476)),
    ('users_setlists_read', dict(list_id=221643)),
    ('users_sets_read', dict(set_num='8277-1')),
], ids=get_id)
@pytest.mark.integration
def test_objects_attributes(func, kwargs, user_context, api_client):
    func = getattr(user_context.api, func)
    kwargs['user_token'] = user_context.token
    do_test(func, kwargs, api_client)


@pytest.mark.integration
def test_users_badges_read_attributes(user_context, api_client):
    do_test(user_context.api.users_badges_read, dict(id=63), api_client)


def do_test(func, kwargs, api_client):
    obj = api_client.sanitize_for_serialization(func(**kwargs))
    obj_no_preload = json.loads(func(_preload_content=False, **kwargs).data)

    # ignore Set last_modified_dt (datetime format)
    if 'last_modified_dt' in obj:
        obj['last_modified_dt'] = obj_no_preload['last_modified_dt']
    if 'set' in obj:
        obj['set']['last_modified_dt'] = obj_no_preload['set']['last_modified_dt']

    ddiff = diff(obj_no_preload, obj)

    pprint(ddiff)
    assert ddiff == {}