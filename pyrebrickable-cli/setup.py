# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
import os

from setuptools import setup, find_packages  # noqa: H301

NAME = "pyrebrickable_cli"
VERSION = os.environ.get('TRAVIS_TAG', os.environ.get('TAG_NAME', 'dev'))
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["pyrebrickable_api",
            "click >=6"]

setup(
    name=NAME,
    version=VERSION,
    description="""This is rebrickable_cli, providing a CLI python wrapper around the Rebrickable API

It supports the v3 API through it's openAPI specification.
https://rebrickable.com/api/v3/swagger/?format=openapi

It uses the rebrickable_api package, which can be found independently in pyrebrickable_api 
The rebrickable_api package was auto-generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    Models for Part, Set, etc. have been manually added to provide meaningful results from HTTP responses

Some endpoints might not work, don't hesitate to file an issue""",
    author_email="",
    url="",
    keywords=["LEGO", "Rebrickable", "CLI"],
    entry_points={
        'console_scripts': [
            'rebrickable=rebrickable_cli.cli:main'
        ]
    },
    install_requires=REQUIRES,
    include_package_data=True,
    packages=find_packages()
)
