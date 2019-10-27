from pprint import pprint

import six
from sqlalchemy import not_, and_

from rebrickable.api import UsersApi
from rebrickable.cli.utils import get_api_client, get_user_token
from rebrickable.data.database import Session
from rebrickable.data.models import Theme, Set, PartCategory

session = Session()


def get_parts():
    theme = session.query(Theme).filter_by(name='Minecraft').first()

    sets = session.query(Set).filter(Set.theme == theme,
                                     and_(not_(Set.name.contains('Micro')), not_(Set.name.contains('Skin Pack'))))

    overworld = [
        ('The Cave', '21113-1'),
        ('The Farm', '21114-1'),
        ('The First Night', '21115-1'),
        ('Crafting Box', '21116-1'),
        ('The Dungeon', '21119-1'),
        ('The Snow Hideout', '21120-1'),
        ('The Desert Outpost', '21121-1'),
        ('The Iron Golem', '21123-1'),
        ('The Fortress', '21127-1'),
        ('The Village', '21128-1'),
        ('The Mushroom Island', '21129-1'),
        ('The Ice Spikes', '21131-1'),
        ('The Jungle Temple', '21132-1'),
        ('The Witch Hut', '21133-1'),
        ('The Waterfall Base', '21134-1'),
        ('The Crafting Box 2.0', '21135-1'),
        ('The Mountain Cave', '21137-1'),
        ('The Melon Farm', '21138-1'),
        ('The Chicken Coop', '21140-1'),
        ('The Zombie Cave', '21141-1'),
        ('The Polar Iglo', '21142-1'),
        ('The Farm Cottage', '21144-1'),
        ('The Bedrock Adventures', '21147-1'),
        ('The Skeleton Attack', '21146-1'),
        ('The Jungle Tree House', '21125-1'),
        ('The Mine', '21118-1'),
        ('The End Portal', '21124-1'),

        ('The Ocean Monument', '21136-1'),
    ]

    nether = [
        ('The Nether Fortress', '21122-1'),
        ('The Wither', '21126-1'),
        ('The Nether Railway', '21130-1'),
        ('The Nether Fight', '21139-1'),
        ('The Nether Portal', '21143-1'),
        ('The Skull Arena', '21145-1'),
    ]

    end = [
        ('The Ender Dragon', '21117-1'),

    ]

    set_nums = [s[1] for s in overworld]

    sets = sets.filter(Set.set_num.in_(set_nums))

    pprint([s.name for s in sets])

    n_sets = sets.count()

    excluded_categories = ['Minifigs', 'Tools', 'Minifig Accessories', 'Containers']

    part_categories = [e.id for e in
                       session.query(PartCategory).filter(not_(PartCategory.name.in_(excluded_categories))).all()]

    pprint([e.name for e in session.query(PartCategory)])

    parts = {}

    for set in sets:
        inventory = set.inventories[0]
        for inventory_part in inventory.parts:
            if inventory_part.part.part_cat_id in part_categories:
                key = (inventory_part.part, inventory_part.color)
                parts.setdefault(key, {})[set.set_num] = inventory_part.quantity

    for k in parts:
        parts[k] = (round(100 * len(parts[k]) / n_sets), max(parts[k].values()), parts[k])

    threshold = 20
    list_parts = [k + v for (k, v) in six.iteritems(parts) if v[0] > threshold]

    pprint(sorted(list_parts, key=lambda k: k[2], reverse=True))

    return list_parts


def get_partlist_by_name(name):
    partlists = api.users_partlists_list(user_token)
    for partlist in partlists.results:
        if partlist.name == name:
            api.users_partlists_delete(user_token, partlist.id)

    return api.users_partlists_create(user_token, name)


class CustomUsersApi(UsersApi):

    def users_partlists_multiple_parts_create(self, user_token, list_id, parts_list, **kwargs):  # noqa: E501
        """Add multiple Parts to the Part List.  # noqa: E501

        ### Multiple Parts To add multiple Parts, POST a JSON list of them (using a Content-Type header of 'application/json'). e.g: `[{\"part_num\":\"3001\", \"color_id\": 1, \"quantity\": 10}, {\"part_num\":\"3001\", \"color_id\": 2, \"quantity\": 20}, {\"part_num\":\"3002\", \"color_id\": 14, \"quantity\": 30}]` Returns a list of successfully added Parts. If the Part already exists or is unrecognised, it will be skipped.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_partlists_multiple_parts_create(user_token, list_id, parts_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[PartListPartItem] parts_list: parts_list (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.users_partlists_multiple_parts_create_with_http_info(user_token, list_id, parts_list,
                                                                             **kwargs)  # noqa: E501
        else:
            (data) = self.users_partlists_multiple_parts_create_with_http_info(user_token, list_id, parts_list,
                                                                               **kwargs)  # noqa: E501
            return data

    def users_partlists_multiple_parts_create_with_http_info(self, user_token, list_id, parts_list,
                                                             **kwargs):  # noqa: E501
        """Add one or more Parts to the Part List.  # noqa: E501

        Add one or more Parts to the Part List.  ### Single Part When adding a single Part, returns the successfully created Part (status 201) or details for why the Part could not be added. ### Multiple Parts To add multiple Parts, POST a JSON list of them (using a Content-Type header of 'application/json'). e.g: `[{\"part_num\":\"3001\", \"color_id\": 1, \"quantity\": 10}, {\"part_num\":\"3001\", \"color_id\": 2, \"quantity\": 20}, {\"part_num\":\"3002\", \"color_id\": 14, \"quantity\": 30}]` Returns a list of successfully added Parts. If the Part already exists or is unrecognised, it will be skipped.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_partlists_parts_create_with_http_info(user_token, list_id, part_num, quantity, color_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_token: user_token (required)
        :param str list_id: list_id (required)
        :param PartListParts parts_list: parts_list (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['user_token', 'list_id', 'parts_list']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_partlists_parts_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_token' is set
        if ('user_token' not in local_var_params or
                local_var_params['user_token'] is None):
            raise ValueError(
                "Missing the required parameter `user_token` when calling `users_partlists_parts_create`")  # noqa: E501
        # verify the required parameter 'list_id' is set
        if ('list_id' not in local_var_params or
                local_var_params['list_id'] is None):
            raise ValueError(
                "Missing the required parameter `list_id` when calling `users_partlists_parts_create`")  # noqa: E501
        # verify the required parameter 'parts_list' is set
        if ('parts_list' not in local_var_params or
                local_var_params['parts_list'] is None):
            raise ValueError(
                "Missing the required parameter `parts_list` when calling `users_partlists_multiple_parts_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_token' in local_var_params:
            path_params['user_token'] = local_var_params['user_token']  # noqa: E501
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = parts_list
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/users/{user_token}/partlists/{list_id}/parts/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)


api_client = get_api_client()
api = CustomUsersApi(api_client)
user_token = get_user_token()

partlist = get_partlist_by_name('minecraft')

list_parts = get_parts()

partlist_parts = [
    {'part_num': row[0].part_num, 'color_id': row[1].id, 'quantity': row[3]}
    for row in list_parts
]

api.users_partlists_multiple_parts_create(user_token, partlist.id, parts_list=partlist_parts)
