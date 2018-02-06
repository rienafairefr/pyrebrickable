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
VERSION = os.environ.get('TRAVIS_TAG', os.environ.get('TAG_NAME'))
if not VERSION:
    VERSION = 'dev'


def generate_swagger():
    # urlretrieve(swagger_url, "rerickable.json")

    with open(rebrickable, 'r') as rebrickable_file, \
            open(swagger, 'w') as swagger_file:
        api = json.load(rebrickable_file)

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
                        "count": {"type": "integer"},
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

        classes = {
            'Color': {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "rgb": {"type": "string"},
                "is_trans": {"type": "bool"},
            },
            'Theme': {
                "id": {"type": "integer"},
                "parent_id": {
                    "type": "integer",
                    "nullable": True
                },
                "name": {"type": "string"},
            },
            'Set': {
                "set_num": {"type": "string"},
                "name": {"type": "string"},
                "year": {"type": "integer"},
                "theme_id": {
                    "type": "integer",
                    "nullable": True
                },
                "num_parts": {"type": "integer"},
                "set_img_url": {"type": "string"},
                "set_url": {"type": "string"},
                "last_modified_dt": {"type": "string", "format": "date-time"}
            },
            'Part': {
                "part_num": {"type": "string"},
                "name": {"type": "string"},
                "part_cat_id": {"type": "integer"},
                "part_url": {"type": "string"},
                "part_img_url": {
                    "type": "string",
                    "nullable": True
                }
            },
            'InventoryPart': {
                "id": {'type': 'integer'},
                "inv_part_id": {'type': 'integer'},
                "part": ref('Part'),
                "color": ref('Color')
            },
            'SetList': {
                "id": {'type': 'integer'},
                "is_buildable": {'type': 'bool'},
                "name": {'type': 'string'},
                "num_sets": {'type': 'integer'}
            },
            'Moc': {
                "set_num": {"type": "string"},
                "name": {"type": "string"},
                "year": {"type": "integer"},
                "theme_id": {'type': 'integer'},
                "num_parts": {'type': 'integer'},
                "moc_img_url": {"type": "string"},
                "moc_url": {"type": "string"},
                "designer_name": {"type": "string"},
                "designer_url": {"type": "string"}
            },
            'Badge': {
                "id": {'type': 'integer'},
                "code": {'type': 'string'},
                "level": {'type': 'integer'},
                "name": {'type': 'string'},
                "descr": {'type': 'string'}
            },
            'PartList': {
                "id": {'type': 'integer'},
                "is_buildable": {'type': 'boolean'},
                "name": {'type': 'string'},
                "num_parts": {'type': 'integer'}
            },
            'LostPart': {
                "lost_part_id": {'type': 'integer'},
                "lost_quantity": {'type': 'integer'},
                "inv_part": ref('InventoryPart')
            },
            'PartListPart': {
                "list_id": {'type': 'integer'},
                "quantity": {'type': 'integer'},
                "part": ref('Part'),
                "color": ref('Color')
            },
            'SetListSet': {
                "list_id": {'type': 'integer'},
                "quantity": {'type': 'integer'},
                "include_spares": {'type': 'boolean'},
                "set": ref('Set'),
            },
            'PartCategory': {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "part_count": {"type": "integer"}
            },
            'Element':{
                "part": ref('Part'),
                "color": ref('Color'),
                "element_id": {'type': 'string'},
                "design_id": {'type': 'string'},
                "element_img_url": {'type': 'string'},
                "part_img_url": {'type': 'string'}
            },
            'AllPart':{
                "quantity": {'type': 'integer'},
                "part": ref('Part'),
                "color": ref('Color')
            }
        }
        non_array_classes = {
            'BuildOptions': {
                "ignore_minifigs": {'type': 'boolean'},
                "sort_by": {'type': 'integer'},
                "max_year": {'type': 'integer'},
                "inc_accessory": {'type': 'boolean'},
                "max_parts": {'type': 'integer'},
                "inc_official": {'type': 'boolean'},
                "inc_bmodels": {'type': 'boolean'},
                "inc_custom": {'type': 'boolean'},
                "color": {'type': 'integer'},
                "min_year": {'type': 'integer'},
                "min_parts": {'type': 'integer'},
                "ignore_altp": {'type': 'boolean'},
                "ignore_non_lego": {'type': 'boolean'},
                "inc_owned": {'type': 'boolean'},
                "ignore_print": {'type': 'boolean'},
                "inc_premium": {'type': 'boolean'},
                "ignore_mold": {'type': 'boolean'}
            },
            'Build': {
                "num_owned_less_ignored": {'type': 'integer'},
                "total_parts": {'type': 'integer'},
                "total_parts_less_ignored": {'type': 'integer'},
                "pct_owned": {'type': 'number', 'format': 'float'},
                "num_ignored": {'type': 'integer'},
                "build_options": ref('BuildOptions'),
                "num_missing": {'type': 'integer'}
            },
            'Rewards': {
                "badges": [56, 43, 39],
                "points": 0,
                "level": 0
            },
            'Lego': {
                "lost_set_parts": {'type': 'integer'},
                "total_set_parts": {'type': 'integer'},
                "total_sets": {'type': 'integer'},
                "all_parts": {'type': 'integer'},
                "total_loose_parts": {'type': 'integer'}
            },
            'Profile': {
                "user_id": {'type': 'integer'},
                "username": {'type': 'string'},
                "email": {'type': 'string'},
                "real_name": {'type': 'string'},
                "last_activity": {'type': 'string', 'format': 'date-time'},
                "last_ip": {'type': 'string'},
                "location": {'type': 'string'},
                "rewards": ref('Rewards'),
                "lego": ref('Lego'),
                "avatar_img": {'string': 'type'}
            },
            'UsersTokenResponse': {
                "user_token": {'type': 'string'}
            }
        }

        for cls in classes:
            api['definitions'].update(get_typedef_array(cls))
            api['definitions'].update(get_typedef(cls, classes[cls]))

        for cls in non_array_classes:
            api['definitions'].update(get_typedef(cls, non_array_classes[cls]))

        def set_schema(url, schema, code='200', method='get'):
            api['paths'][url][method]['responses'][code]['schema'] = schema


        set_schema('/api/v3/users/_token/', ref('UsersTokenResponse'), '201', 'post')
        set_schema('/api/v3/lego/elements/{element_id}/', ref('Element'))

        set_schema('/api/v3/users/{user_token}/build/{set_num}/', ref('Build'))
        set_schema('/api/v3/users/{user_token}/profile/', ref('Profile'))

        # single element
        set_schema('/api/v3/lego/colors/{id}/', ref('Color'))
        set_schema('/api/v3/lego/themes/{id}/', ref('Theme'))
        set_schema('/api/v3/lego/mocs/{set_num}/', ref('Moc'))
        set_schema('/api/v3/lego/parts/{part_num}/', ref('Part'))
        set_schema('/api/v3/lego/parts/{part_num}/colors/{color_id}/', ref('Color'))
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
        set_schema('/api/v3/lego/parts/{part_num}/colors/', ref('ArrayOfColors'))
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
        set_schema('/api/v3/users/{user_token}/sets/', ref('ArrayOfSets'))
        set_schema('/api/v3/users/{user_token}/allparts/', ref('ArrayOfAllParts'))
        set_schema('/api/v3/users/{user_token}/lost_parts/', ref('ArrayOfParts'))
        set_schema('/api/v3/users/{user_token}/lost_parts/', ref('ArrayOfParts'))
        set_schema('/api/v3/users/{user_token}/lost_parts/', ref('ArrayOfLostParts'))
        set_schema('/api/v3/users/{user_token}/parts/', ref('ArrayOfPartListParts'))




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
        # '/api/v3/users/{user_token}/setlists/', 'POST',
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