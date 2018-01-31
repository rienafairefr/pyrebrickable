#!/usr/bin/env python
import os

try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve
import json
import shutil

swagger_url = "https://rebrickable.com/api/v3/swagger/?format=openapi"
swagger = 'swagger.json'
rebrickable = 'rebrickable.json'


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
            'Moc':{
                "set_num": {"type": "string"},
                "name": {"type": "string"},
                "year": {"type": "integer"},
                "theme_id": {'type':'integer'},
                "num_parts": {'type':'integer'},
                "moc_img_url": {"type": "string"},
                "moc_url": {"type": "string"},
                "designer_name": {"type": "string"},
                "designer_url": {"type": "string"}
            },
            'PartCategory': {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "part_count": {"type": "integer"}
            }
        }

        for cls in classes:
            api['definitions'].update(get_typedef_array(cls))
            api['definitions'].update(get_typedef(cls, classes[cls]))

        api['definitions'].update(get_typedef('UsersTokenResponse', {
                "user_token": {'type': 'string'}
            }))

        api['paths']['/api/v3/lego/colors/']['get']['responses']['200']['schema'] = ref('ArrayOfColors')
        api['paths']['/api/v3/lego/colors/{id}/']['get']['responses']['200']['schema'] = ref('Color')
        api['paths']['/api/v3/lego/themes/']['get']['responses']['200']['schema'] = ref('ArrayOfThemes')
        api['paths']['/api/v3/lego/themes/{id}/']['get']['responses']['200']['schema'] = ref('Theme')

        api['paths']['/api/v3/lego/sets/']['get']['responses']['200']['schema'] = ref('ArrayOfSets')
        api['paths']['/api/v3/lego/sets/{set_num}/']['get']['responses']['200']['schema'] = ref('Set')

        api['paths']['/api/v3/lego/parts/']['get']['responses']['200']['schema'] = ref('ArrayOfParts')
        api['paths']['/api/v3/lego/parts/{part_num}/']['get']['responses']['200']['schema'] = ref('Part')

        api['paths']['/api/v3/lego/part_categories/']['get']['responses']['200']['schema'] = ref(
            'ArrayOfPartCategories')
        api['paths']['/api/v3/lego/part_categories/{id}/']['get']['responses']['200']['schema'] = ref('PartCategory')

        api['paths']['/api/v3/lego/mocs/{set_num}/parts/']['get']['responses']['200']['schema'] = ref('ArrayOfInventoryParts')

        api['paths']['/api/v3/lego/mocs/{set_num}/']['get']['responses']['200']['schema'] = ref(
            'Moc')

        api['paths']['/api/v3/lego/parts/{part_num}/colors/']['get']['responses']['200']['schema'] = ref(
            'ArrayOfColors')

        api['paths']['/api/v3/lego/parts/{part_num}/colors/{color_id}/']['get']['responses']['200']['schema'] = ref(
            'Color')
        api['paths']['/api/v3/lego/parts/{part_num}/colors/{color_id}/sets/']['get']['responses']['200'][
            'schema'] = ref(
            'ArrayOfSets')

        api['paths']['/api/v3/lego/sets/{set_num}/parts/']['get']['responses']['200'][
            'schema'] = ref(
            'ArrayOfParts')

        api['paths']['/api/v3/lego/sets/{set_num}/sets/']['get']['responses']['200'][
            'schema'] = ref(
            'ArrayOfSets')

        api['paths']['/api/v3/lego/sets/{set_num}/alternates/']['get']['responses']['200'][
            'schema'] = ref(
            'ArrayOfMocs')

        # TODO
        # '/api/v3/lego/elements/{element_id}/', 'GET',

        api['paths']['/api/v3/users/_token/']['post']['responses']['200'] = {
            'schema': ref('UsersTokenResponse')}

        api['paths']['/api/v3/users/{user_token}/sets/']['get']['responses']['200'][
            'schema'] = ref(
            'ArrayOfSets')

        api['paths']['/api/v3/users/{user_token}/sets/{set_num}/']['get']['responses']['200'][
            'schema'] = ref(
            'Set')
        api['info']['description'] = '''
This is pyrebrickable, a python CLI wrapper around the Rebrickable API<br>
<br>
It supports the v3 API through it's openAPI specification.<br>
https://rebrickable.com/api/v3/swagger/?format=openapi<br>
Models for Part, Set, etc. have been manually added to provide meaningful results from HTTP responses<br>
<br>
Some endpoints might not work, don't hesitate to file an issue<br>
'''

        json.dump(api, swagger_file, indent=True, sort_keys=True)

    shutil.rmtree(os.path.join('rebrickable', 'api'), ignore_errors=True)
    shutil.rmtree(os.path.join('rebrickable', 'models'), ignore_errors=True)
    shutil.rmtree('docs', ignore_errors=True)

    os.system('docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local swaggerapi/swagger-codegen-cli'
              ' generate -i /local/swagger.json '
              '-t /local/templates '
              '--git-user-id rienafairefr '
              '--git-repo-id pyrebrickable '
              '-l python -o /local -DprojectName=pyrebrickable -DpackageName=rebrickable')


if __name__ == '__main__':
    generate_swagger()
