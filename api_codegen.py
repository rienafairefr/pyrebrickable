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
            array = 'ArrayOf%ss' % cls
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
        }

        for cls in classes:
            api['definitions'].update(get_typedef_array(cls))
            api['definitions'].update(get_typedef(cls, classes[cls]))

        def ref(cls):
            return {'$ref': "#/definitions/%s" % cls}

        api['paths']['/api/v3/lego/colors/']['get']['responses']['200']['schema'] = ref('ArrayOfColors')
        api['paths']['/api/v3/lego/colors/{id}/']['get']['responses']['200']['schema'] = ref('Color')
        api['paths']['/api/v3/lego/themes/']['get']['responses']['200']['schema'] = ref('ArrayOfThemes')
        api['paths']['/api/v3/lego/themes/{id}/']['get']['responses']['200']['schema'] = ref('Theme')

        json.dump(api, swagger_file, indent=True, sort_keys=True)

    shutil.rmtree(os.path.join('rebrickable', 'api'), ignore_errors=True)
    shutil.rmtree(os.path.join('rebrickable', 'models'), ignore_errors=True)
    shutil.rmtree('docs', ignore_errors=True)

    os.system('docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local swaggerapi/swagger-codegen-cli'
              ' generate -i /local/swagger.json -l python -o /local -DprojectName=pyrebrickable -DpackageName=rebrickable')


if __name__ == '__main__':
    generate_swagger()
