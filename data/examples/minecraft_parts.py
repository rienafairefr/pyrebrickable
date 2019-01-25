from pprint import pprint

import six
from sqlalchemy import not_, and_

from rebrickable_api import UsersApi
from rebrickable_cli.cli.main import get_api_client
from rebrickable_cli.cli.user import get_user_token
from rebrickable_data.database import Session
from rebrickable_data.models import Theme, Set, PartCategory

session = Session()


def get_parts():

    theme = session.query(Theme).filter_by(name='Minecraft').first()

    sets = session.query(Set).filter(Set.theme == theme, and_(not_(Set.name.contains('Micro')), not_(Set.name.contains('Skin Pack'))))

    pprint([s.name for s in sets])

    n_sets = sets.count()

    categories = ['Bricks', 'Plates', 'Plates Special', 'Bricks Special']

    part_categories = [e.id for e in
                session.query(PartCategory).filter(PartCategory.name.in_(categories)).order_by(PartCategory.name).all()]
    part_categories = [e.id for e in session.query(PartCategory).all()]

    parts = {}

    for set in sets:
        inventory = set.inventories[0]
        for inventory_part in inventory.parts:
            if inventory_part.part.part_cat_id in part_categories:
                key = (inventory_part.part, inventory_part.color)
                parts.setdefault(key, []).append(inventory_part.quantity)

    for k in parts:
        parts[k] = (round(100 * len(parts[k]) / n_sets), max(parts[k]))

    threshold = 20
    list_parts = [(k[0], k[1], v[0], v[1]) for (k, v) in six.iteritems(parts) if v[0] > threshold]

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
            return self.users_partlists_multiple_parts_create_with_http_info(user_token, list_id, parts_list, **kwargs)  # noqa: E501
        else:
            (data) = self.users_partlists_multiple_parts_create_with_http_info(user_token, list_id, parts_list, **kwargs)  # noqa: E501
            return data

    def users_partlists_multiple_parts_create_with_http_info(self, user_token, list_id, parts_list, **kwargs):  # noqa: E501
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
            raise ValueError("Missing the required parameter `user_token` when calling `users_partlists_parts_create`")  # noqa: E501
        # verify the required parameter 'list_id' is set
        if ('list_id' not in local_var_params or
                local_var_params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `users_partlists_parts_create`")  # noqa: E501
        # verify the required parameter 'parts_list' is set
        if ('parts_list' not in local_var_params or
                local_var_params['parts_list'] is None):
            raise ValueError("Missing the required parameter `parts_list` when calling `users_partlists_multiple_parts_create`")  # noqa: E501

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
user_token=get_user_token()

partlist = get_partlist_by_name('minecraft')

list_parts = get_parts()

partlist_parts = [
    {'part_num': row[0].part_num, 'color_id': row[1].id, 'quantity': row[2]}
    for row in list_parts
]

api.users_partlists_multiple_parts_create(user_token, partlist.id, parts_list=partlist_parts)
