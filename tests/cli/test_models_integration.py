from __future__ import print_function

import json
from pprint import pprint

import pytest
import six
from jsondiff import diff

import rebrickable
from rebrickable.api import LegoApi, UsersApi
from docstring_parser import parse
from rebrickable.cli.common import State
from rebrickable.cli.utils import get_api_client, get_user_token

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
def users_context(api_client):
    return State(client=api_client, api=UsersApi(api_client), user_token=get_user_token())


def get_id(element):
    if callable(element):
        return element.__name__
    return str(element)


def remove_nulls(d):
    return {k: remove_nulls(v) if isinstance(v, dict) else v for k, v in six.iteritems(d) if v is not None}


@pytest.mark.parametrize(['func', 'kwargs'], [
    ('lego_colors_read', dict(id=7)),
    ('lego_colors_list', dict()),
    ('lego_elements_read', dict(element_id=4245295)),
    ('lego_part_categories_read', dict(id=42)),
    ('lego_part_categories_list', dict()),
    ('lego_parts_colors_read', dict(color_id=4, part_num='3004')),
    ('lego_parts_colors_list', dict(part_num='3004')),
    ('lego_parts_colors_sets_list', dict(color_id=4, part_num='3004')),
    ('lego_parts_read', dict(part_num='3004')),
    ('lego_parts_list', dict()),
    ('lego_parts_read', dict(part_num='4070')),
    ('lego_sets_alternates_list', dict(set_num='75192-1')),
    ('lego_sets_read', dict(set_num='75192-1')),
    ('lego_sets_read', dict(set_num='31027-1')),
    ('lego_sets_list', dict()),
    ('lego_sets_parts_list', dict(set_num='75192-1')),
    ('lego_sets_sets_list', dict(set_num='75192-1')),
    ('lego_themes_read', dict(id=99)),
    ('lego_themes_list', dict()),
], ids=get_id)
@pytest.mark.integration
def test_lego_objects_attributes(func, kwargs, lego_api, users_context):
    func = getattr(lego_api, func)
    do_test(func, kwargs, users_context)


@pytest.mark.parametrize(['func', 'kwargs'], [
    ('users_build_read', dict(set_num='75192-1')),
    ('users_partlists_parts_read', dict(list_id=229534, color_id=6, part_num='11110')),
    # user partlist 40476 part 1 3298p61
    ('users_partlists_read', dict(list_id=229534)),
    ('users_setlists_read', dict(list_id=462364)),
    ('users_sets_read', dict(set_num='7195-1')),
], ids=get_id)
@pytest.mark.integration
def test_objects_attributes(func, kwargs, users_context):
    func = getattr(users_context.api, func)
    kwargs['user_token'] = users_context.user_token
    do_test(func, kwargs, users_context)


@pytest.mark.integration
def test_users_badges_read_attributes(users_context):
    do_test(users_context.api.users_badges_read, dict(id=63), users_context)


def do_test(func, kwargs, state):
    # converted from API
    d = parse(func.__doc__)
    type_name = d.returns.description.splitlines()[0]
    klass = getattr(rebrickable.api.models, type_name)
    obj = state.client._ApiClient__deserialize_model(state.client.sanitize_for_serialization(func(**kwargs)), klass)
    # raw from API
    obj_no_preload = json.loads(func(_preload_content=False, **kwargs).data)

    def dict_equal(expected, actual):
        for k, v in actual.items():
            if v is None and k not in expected:
                # kinda nullable
                continue
            if isinstance(v, dict):
                dict_equal(expected[k], v)
            else:
                assert expected[k] == v

    #dict_equal(obj.to_dict(), obj_no_preload)

    ddiff = diff(obj_no_preload, obj, syntax='explicit')

    pprint(ddiff)
