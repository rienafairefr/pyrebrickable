#!/usr/bin/env python
import os

try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve
import json

swagger_url = "https://rebrickable.com/api/v3/swagger/?format=openapi"
swagger = 'swagger.json'
rebrickable = 'rebrickable.json'


def generate_swagger():
    # urlretrieve(swagger_url, "rerickable.json")

    with open(rebrickable, 'r') as rebrickable_file, \
            open(swagger, 'w') as swagger_file:
        api = json.load(rebrickable_file)

        for url, path in api['paths'].items():
            for method, method_dict in path.items():
                for i, param in enumerate(method_dict['parameters']):
                    if param['description'] is None:
                        api['paths'][url][method]['parameters'][i]['description'] = param['name']


        api.update(
            {
                "securityDefinitions": {
                    "ApiKey": {
                        "in": "header",
                        "type": "apiKey",
                        "name": "Authorization"
                    }
                },
                "security": [
                    {
                        "ApiKey": []
                    }
                ],
                "definitions": {}
            })

        def get_typedef_array(cls):
            if cls.endswith('y'):
                plural = cls[:-1] + 'ies'
            else:
                plural = cls + 's'
            array = 'ArrayOf%s' % plural

            return {
                array: {
                    "type": "object",
                    "properties": {
                        "count": Integer,
                        "results": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/%s" % cls
                            }
                        }
                    }
                }
            }

        def get_typedef(cls, properties):
            return {
                cls: {
                    "type": "object",
                    "properties": properties
                }
            }

        def ref(cls):
            return {'$ref': "#/definitions/%s" % cls}
        
        Integer = {'type': 'integer'}
        String = {'type': 'string'}
        Boolean = {'type': 'boolean'}
        Url = {'type': 'string', 'format': 'uri'}
        ArrayOfInteger = {'type': 'array', 'items': Integer}
        ArrayOfString = {'type': 'array', 'items': String}

        classes = {
            'Color': {
                "id": Integer,
                "name": String,
                "rgb": String,
                "is_trans": Boolean,
                'external_ids': ref('ExternalColorIds')
            },
            'Theme': {
                "id": Integer,
                "parent_id": Integer,
                "name": String,
            },
            'Set': {
                "set_num": String,
                "name": String,
                "year": Integer,
                "theme_id": Integer,
                "num_parts": Integer,
                "set_img_url": Url,
                "set_url": Url,
                "last_modified_dt": {"type": "string", "format": "date-time"}
            },
            'Part': {
                "part_num": String,
                "name": String,
                "part_cat_id": Integer,
                "year_from": Integer,
                "year_to": Integer,
                "part_url": Url,
                "part_img_url": Url,
                "prints": ArrayOfString,
                "molds": ArrayOfString,
                "alternates": ArrayOfString,
                "external_ids": ref('ExternalIds'),
            },
            'InventoryPart': {
                "id": Integer,
                "inv_part_id": Integer,
                "part": ref('Part'),
                "color": ref('Color')
            },
            'SetList': {
                "id": Integer,
                "is_buildable": Boolean,
                "name": String,
                "num_sets": Integer
            },
            'Moc': {
                "set_num": String,
                "name": String,
                "year": Integer,
                "theme_id": Integer,
                "num_parts": Integer,
                "moc_img_url": Url,
                "moc_url": Url,
                "designer_name": String,
                "designer_url": Url
            },
            'Badge': {
                "id": Integer,
                "code": String,
                "level": Integer,
                "name": String,
                "descr": String
            },
            'PartList': {
                "id": Integer,
                "is_buildable": Boolean,
                "name": String,
                "num_parts": Integer
            },
            'LostPart': {
                "lost_part_id": Integer,
                "lost_quantity": Integer,
                "inv_part": ref('InventoryPart')
            },
            'PartListPart': {
                "list_id": Integer,
                "quantity": Integer,
                "part": ref('Part'),
                "color": ref('Color')
            },
            'SetListSet': {
                "list_id": Integer,
                "quantity": Integer,
                "include_spares": Boolean,
                "set": ref('Set'),
                "set_num": String
            },
            'PartCategory': {
                "id": Integer,
                "name": String,
                "part_count": Integer
            },
            'Element': {
                "part": ref('Part'),
                "color": ref('Color'),
                "element_id": String,
                "design_id": String,
                "element_img_url": Url,
                "part_img_url": Url
            },
            'AllPart': {
                "quantity": Integer,
                "part": ref('Part'),
                "color": ref('Color')
            },
            'PartColorsList': {
                "num_sets": Integer,
                "elements": ArrayOfInteger,
                "num_set_parts": Integer,
                "color_id": Integer,
                "part_img_url": Url,
                "color_name": String
            },
            "PartColorsElement": {
                'num_sets': Integer,
                'elements': ArrayOfString,
                'num_set_parts': Integer,
                'year_from': Integer,
                'part_img_url': Url,
                'year_to': Integer
            }
        }
        non_array_classes = {
            'ExternalColorId': {
                'ext_ids': ArrayOfInteger,
                'ext_descrs': {'type': 'array', 'items': ArrayOfString}
            },
            'ExternalColorIds': {
                'BrickLink': ref('ExternalColorId'),
                'LEGO': ref('ExternalColorId'),
                'BrickOwl': ref('ExternalColorId'),
                'Peeron': ref('ExternalColorId'),
                'LDraw': ref('ExternalColorId')
            },
            'ExternalIds': {
                "BrickLink": ArrayOfString,
                "BrickOwl": ArrayOfString,
                "LDraw": ArrayOfString,
                "LEGO": ArrayOfString
            },
            'BuildOptions': {
                "ignore_minifigs": Boolean,
                "sort_by": Integer,
                "max_year": Integer,
                "inc_accessory": Boolean,
                "max_parts": Integer,
                "inc_official": Boolean,
                "inc_bmodels": Boolean,
                "inc_custom": Boolean,
                "color": Integer,
                "min_year": Integer,
                "min_parts": Integer,
                "ignore_altp": Boolean,
                "ignore_non_lego": Boolean,
                "inc_owned": Boolean,
                "ignore_print": Boolean,
                "inc_premium": Boolean,
                "theme": Integer,
                "ignore_mold": Boolean
            },
            'Build': {
                "num_owned_less_ignored": Integer,
                "total_parts": Integer,
                "total_parts_less_ignored": Integer,
                "pct_owned": {'type': 'number', 'format': 'float'},
                "num_ignored": Integer,
                "build_options": ref('BuildOptions'),
                "num_missing": Integer
            },
            'Rewards': {
                "badges": ArrayOfInteger,
                "points": Integer,
                "level": Integer
            },
            'Lego': {
                "lost_set_parts": Integer,
                "total_set_parts": Integer,
                "total_sets": Integer,
                "all_parts": Integer,
                "total_loose_parts": Integer
            },
            'Profile': {
                "user_id": Integer,
                "username": String,
                "email": String,
                "real_name": String,
                "last_activity": {'type': 'string', 'format': 'date-time'},
                "last_ip": String,
                "location": String,
                "rewards": ref('Rewards'),
                "lego": ref('Lego'),
                "avatar_img": String
            },
            'UsersTokenResponse': {
                "user_token": String
            },
            'PartListPartItem': {
                "quantity": Integer,
                "part_num": String,
                "color_id": Integer
            },
            'SetListSetItem': {
                "include_spares": Boolean,
                "set_num": String,
                "quantity": Integer
            },
            'UserSetItem': {
                "set_num": String,
                "quantity": Integer
            }
        }

        api['definitions'].update(
            {
                'ErrorMessage': {
                    "type": "array",
                    'items': {
                        'type': 'string'
                    }
                },
                'PartListParts': {
                    "type": 'array',
                    'items': ref('PartListPartItem')
                },
                'SetListSets': {
                    "type": 'array',
                    'items': ref('SetListSetItem')
                },
                'UserSets': {
                    "type": 'array',
                    'items': ref('UserSetItem')
                }
            })

        for cls in classes:
            api['definitions'].update(get_typedef_array(cls))
            api['definitions'].update(get_typedef(cls, classes[cls]))

        for cls in non_array_classes:
            api['definitions'].update(get_typedef(cls, non_array_classes[cls]))

        def set_schema(url, schema, code='200', method='get'):
            api['paths'][url][method]['responses'][code]['schema'] = schema

        set_schema('/api/v3/users/_token/', ref('UsersTokenResponse'), '201', 'post')
        set_schema('/api/v3/users/{user_token}/partlists/', ref('PartList'), '201', 'post')
        set_schema('/api/v3/lego/elements/{element_id}/', ref('Element'))

        set_schema('/api/v3/users/{user_token}/build/{set_num}/', ref('Build'))
        set_schema('/api/v3/users/{user_token}/profile/', ref('Profile'))

        # single element
        set_schema('/api/v3/lego/colors/{id}/', ref('Color'))
        set_schema('/api/v3/lego/themes/{id}/', ref('Theme'))
        set_schema('/api/v3/lego/mocs/{set_num}/', ref('Moc'))
        set_schema('/api/v3/lego/parts/{part_num}/', ref('Part'))
        set_schema('/api/v3/lego/parts/{part_num}/colors/{color_id}/', ref('PartColorsElement'))
        set_schema('/api/v3/lego/part_categories/{id}/', ref('PartCategory'))
        set_schema('/api/v3/lego/sets/{set_num}/', ref('Set'))
        set_schema('/api/v3/users/badges/{id}/', ref('Badge'))
        set_schema('/api/v3/users/{user_token}/sets/{set_num}/', ref('SetListSet'))
        set_schema('/api/v3/users/{user_token}/setlists/{list_id}/', ref('SetList'))
        set_schema('/api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/', ref('SetListSet'))
        set_schema('/api/v3/users/{user_token}/partlists/{list_id}/', ref('PartList'))
        set_schema('/api/v3/users/{user_token}/partlists/{list_id}/parts/{part_num}/{color_id}/', ref('PartListPart'))
        # list
        set_schema('/api/v3/lego/colors/', ref('ArrayOfColors'))
        set_schema('/api/v3/lego/themes/', ref('ArrayOfThemes'))
        set_schema('/api/v3/lego/mocs/{set_num}/parts/', ref('ArrayOfInventoryParts'))
        set_schema('/api/v3/lego/parts/', ref('ArrayOfParts'))
        set_schema('/api/v3/lego/parts/{part_num}/colors/', ref('ArrayOfPartColorsLists'))
        set_schema('/api/v3/lego/part_categories/', ref('ArrayOfPartCategories'))
        set_schema('/api/v3/lego/sets/', ref('ArrayOfSets'))
        set_schema('/api/v3/users/badges/', ref('ArrayOfBadges'))
        set_schema('/api/v3/users/{user_token}/sets/', ref('ArrayOfSetListSets'))
        set_schema('/api/v3/users/{user_token}/setlists/', ref('ArrayOfSetLists'))
        set_schema('/api/v3/users/{user_token}/setlists/{list_id}/sets/', ref('ArrayOfSetListSets'))
        set_schema('/api/v3/users/{user_token}/partlists/', ref('ArrayOfPartLists'))
        set_schema('/api/v3/users/{user_token}/partlists/{list_id}/parts/', ref('ArrayOfPartListParts'))

        # lists without corresponding single element
        set_schema('/api/v3/lego/parts/{part_num}/colors/{color_id}/sets/', ref('ArrayOfSets'))
        set_schema('/api/v3/lego/sets/{set_num}/parts/', ref('ArrayOfParts'))
        set_schema('/api/v3/lego/sets/{set_num}/sets/', ref('ArrayOfSets'))
        set_schema('/api/v3/lego/sets/{set_num}/alternates/', ref('ArrayOfMocs'))
        set_schema('/api/v3/users/{user_token}/sets/', ref('ArrayOfSetListSets'))
        set_schema('/api/v3/users/{user_token}/allparts/', ref('ArrayOfAllParts'))
        set_schema('/api/v3/users/{user_token}/lost_parts/', ref('ArrayOfParts'))
        set_schema('/api/v3/users/{user_token}/lost_parts/', ref('ArrayOfParts'))
        set_schema('/api/v3/users/{user_token}/lost_parts/', ref('ArrayOfLostParts'))
        set_schema('/api/v3/users/{user_token}/parts/', ref('ArrayOfPartListParts'))
        set_schema('/api/v3/users/{user_token}/sets/', ref('SetListSet'), '201', 'post')
        set_schema('/api/v3/users/{user_token}/setlists/', ref('SetList'), '201', 'post')

        # TODO
        # '/api/v3/users/{user_token}/lost_parts/', 'POST',
        # '/api/v3/users/{user_token}/lost_parts/{id}/', 'DELETE',
        # '/api/v3/users/{user_token}/partlists/', 'POST',
        # '/api/v3/users/{user_token}/partlists/{list_id}/', 'DELETE',
        # '/api/v3/users/{user_token}/partlists/{list_id}/', 'PATCH',
        # '/api/v3/users/{user_token}/partlists/{list_id}/parts/', 'POST',
        # '/api/v3/users/{user_token}/partlists/{list_id}/parts/{part_num}/{color_id}/', 'DELETE',
        # '/api/v3/users/{user_token}/partlists/{list_id}/parts/{part_num}/{color_id}/', 'PUT',
        # '/api/v3/users/{user_token}/partlists/{list_id}/', 'PUT',
        # '/api/v3/users/{user_token}/setlists/{list_id}/', 'DELETE',
        # '/api/v3/users/{user_token}/setlists/{list_id}/', 'PATCH',
        # '/api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/', 'DELETE',
        # '/api/v3/users/{user_token}/setlists/{list_id}/sets/', 'POST',
        # '/api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/', 'PATCH',
        # '/api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/', 'PUT',
        # '/api/v3/users/{user_token}/setlists/{list_id}/', 'PUT',
        # '/api/v3/users/{user_token}/sets/{set_num}/', 'DELETE',
        # '/api/v3/users/{user_token}/sets/sync/', 'POST',
        # '/api/v3/users/{user_token}/sets/{set_num}/', 'PUT',
        # '/api/v3/users/_token/', 'POST',

        api['info']['description'] = '''

'''

        json.dump(api, swagger_file, indent=True, sort_keys=True)


if __name__ == '__main__':
    generate_swagger()
